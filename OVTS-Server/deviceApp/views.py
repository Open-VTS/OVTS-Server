# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.utils import timezone
from ipware import get_client_ip
from django.core.files.base import ContentFile
import os
import gzip
import threading
from queue import Queue
import base64
import binascii
from time import sleep
from google.protobuf.json_format import MessageToDict
from protobuf_to_dict import protobuf_to_dict
from .models import *
from .serializers import *
from .proto import OVTSProto_pb2


OK_RESPOND = "T0s="
NOT_FOUND = "Tm90Rm91bmQ="


class AddDeviceView(generics.ListCreateAPIView):
    queryset = DeviceInfo.objects.all()
    serializer_class = AddDeviceSerializer


class DeviceDataHandler:
    @staticmethod
    def b64decode(b64data):
        try:
            return base64.b64decode(b64data.encode())
        except binascii.Error as err:
            print("DeviceData: B64 Decode Failed with {}!".format(err), b64data)

    @staticmethod
    def save_data(device_object, request_ip, b64data, is_report):
        raw_data, created = DeviceRawDataModel.objects.get_or_create(
            device_object=device_object, b64_data=b64data, defaults={'ip': request_ip})
        # if the raw_data already exist so we need to return the equivalent DeviceDataModel or DeviceDataReportModel
        if not created:
            if is_report:
                return DeviceDataReportModel.objects.get(raw_data=raw_data)
            else:
                return DeviceDataModel.objects.get(raw_data=raw_data)
        # decode data to a dict object
        device_data = OVTSProto_pb2.DeviceData()
        encoded_data = base64.b64decode(raw_data.b64_data)

        try:
            device_data.ParseFromString(encoded_data)
            # device_data = MessageToDict(device_data_proto)
        except Exception:
            print("DeviceData: Proto Decode Failed!")
            return False

        # create dict object from device_data
        device_data_dict = protobuf_to_dict(device_data)
        # remove device_id from device_data_dict
        device_data_dict.pop("device_id", None)
        # save data into models
        if device_data.HasField('gps_data'):
            gps_data, _ = GPSModel.objects.get_or_create(
                **device_data_dict['gps_data'])
            device_data_dict["gps_data"] = gps_data

        if device_data.HasField('imu_data'):
            imu_data, _ = IMUModel.objects.get_or_create(
                **device_data_dict['imu_data'])
            device_data_dict["imu_data"] = imu_data

        if device_data.HasField('battery_data'):
            battery_data, _ = BatteryModel.objects.get_or_create(
                **device_data_dict['battery_data'])
            device_data_dict["battery_data"] = battery_data

        if device_data.HasField('center_params'):
            center_address_obj, _ = CenterAddressModel.objects.get_or_create(
                **device_data_dict['center_params']['center_address'])

            device_data_dict['center_params'].pop('center_address', None)
            center_params, _ = CenterParamsModel.objects.get_or_create(center_address=center_address_obj,
                                                                       **device_data_dict['center_params'])
            device_data_dict['center_params'] = center_params

        if device_data.HasField('device_params'):

            timer, _ = TimerModel.objects.get_or_create(
                **device_data_dict['device_params']['timer'])

            data_select, _ = DataSelectModel.objects.get_or_create(
                **device_data_dict['device_params']['data_select'])

            device_params, _ = DeviceParamsModel.objects.get_or_create(timer=timer, data_select=data_select,
                                                                       connection_type=device_data_dict['device_params']['connection_type'])
            device_data_dict['device_params'] = device_params

        if device_data.custom_field:
            custom_field, _ = CustomFieldModel.objects.get_or_create(
                **device_data_dict['custom_field'])
            device_data_dict["custom_field"] = custom_field

        if is_report:
            device_data_model, _ = DeviceDataReportModel.objects.get_or_create(
                raw_data=raw_data, **device_data_dict)
        else:
            device_data_model, _ = DeviceDataModel.objects.get_or_create(
                raw_data=raw_data, **device_data_dict)
        return device_data_model


class DeviceRawDataView(generics.ListCreateAPIView):
    queryset = DeviceRawDataModel.objects.all()
    serializer_class = DeviceDataRawSerializer

    def post(self, request):
        req = request.data.copy()
        # print("request:", req)
        # check id
        #TODO: fix this with slug field in serilizer
        if ('device_id' not in req) or (not DeviceInfo.objects.filter(device_id=req['device_id']).exists()):
            print("Posted DeviceData for ID {} doesn't exists!".format(
                req['device_id']))
            return Response(NOT_FOUND, status=status.HTTP_400_BAD_REQUEST)
        device_id = req['device_id']
        device_info = DeviceInfo.objects.get(device_id=device_id)
        # Fix padding (replace " " with "+")
        req['data'] = req['data'].replace(" ", "+")
        request_ip, _ = get_client_ip(request)
        # save data in model
        DeviceDataHandler.save_data(
            device_info, request_ip, req['data'], False)

        return Response(OK_RESPOND, status=status.HTTP_201_CREATED)


class DeviceDataView(generics.ListAPIView):
    queryset = DeviceDataModel.objects.all()
    serializer_class = DeviceDataSerializer


class CenterCommandsDeviceView(generics.ListCreateAPIView):
    queryset = DeviceCenterCommandsModel.objects.all()
    serializer_class = DeviceCenterCommandsSerializer

    def post(self, request, *args, **kwargs):
        req = request.data
        # print("request:", req)
        # check id
        if ('device_id' not in req) or (not DeviceInfo.objects.filter(device_id=req['device_id']).exists()):
            return Response(NOT_FOUND, status=status.HTTP_400_BAD_REQUEST)
        device_id = req['device_id']
        request_ip, _ = get_client_ip(request)
        device_object = DeviceInfo.objects.get(device_id=device_id)
        # if id found and an unreceived record found in
        if (CenterCommandsModel.objects.filter(device_object=device_object).exists() and CenterCommandsModel.objects.filter(device_object=device_object, received=False).exists()):
            center_command = CenterCommandsModel.objects.filter(
                device_object=device_object, received=False).latest('created_time')

            # save DeviceCenterCommands
            DeviceCenterCommandsModel.objects.create(device_object=device_object, center_command=center_command,
                                                     ip=request_ip)
            # set center_command 's received to True
            center_command.received = True
            center_command.received_time = timezone.now()
            center_command.save()
            return Response(str(center_command.b64_data), status=status.HTTP_201_CREATED)

        else:
            return Response(NOT_FOUND, status=status.HTTP_200_OK)


class CenterCommandsView(generics.ListCreateAPIView):
    queryset = CenterCommandsModel.objects.all()
    serializer_class = CenterCommandsSerializer

    def generate_b64_cc(self, center_command):
        # convert object to dict
        center_commands_dict = CenterCommandsSerializer(center_command).data
        center_command_pb = OVTSProto_pb2.CenterCommands()
        center_command_pb.device_id = center_command.device_object.device_id

        if center_command.set_center_params:
            center_command_pb.set_center_params.key = center_command.set_center_params.key
            center_command_pb.set_center_params.center_params.center_address.device_data_url = center_command.set_center_params.center_params.center_address.device_data_url
            center_command_pb.set_center_params.center_params.center_address.center_commands_url = center_command.set_center_params.center_params.center_address.center_commands_url
            center_command_pb.set_center_params.center_params.center_address.device_report_url = center_command.set_center_params.center_params.center_address.device_report_url
            center_command_pb.set_center_params.center_params.center_address.ping_url = center_command.set_center_params.center_params.center_address.ping_url
            center_command_pb.set_center_params.center_params.number1 = center_command.set_center_params.center_params.number1
            if center_command.set_center_params.center_params.number2:
                center_command_pb.set_center_params.center_params.number2 = center_command.set_center_params.center_params.number2
            if center_command.set_center_params.center_params.number3:
                center_command_pb.set_center_params.center_params.number3 = center_command.set_center_params.center_params.number3

        if center_command.device_params:
            center_command_pb.device_params.timer.network_send = center_command.device_params.timer.network_send
            center_command_pb.device_params.timer.network_receive = center_command.device_params.timer.network_receive
            center_command_pb.device_params.timer.sms_send = center_command.device_params.timer.sms_send

            center_command_pb.device_params.data_select.gps_enable = center_command.device_params.data_select.gps_enable
            center_command_pb.device_params.data_select.imu_enable = center_command.device_params.data_select.imu_enable
            center_command_pb.device_params.data_select.relay_enable = center_command.device_params.data_select.relay_enable
            center_command_pb.device_params.data_select.input_sensor_enable = center_command.device_params.data_select.input_sensor_enable
            center_command_pb.device_params.data_select.sim_balance_enable = center_command.device_params.data_select.sim_balance_enable
            center_command_pb.device_params.data_select.battery_enable = center_command.device_params.data_select.battery_enable
            center_command_pb.device_params.data_select.signal_quality_enable = center_command.device_params.data_select.signal_quality_enable

            center_command_pb.device_params.connection_type = center_command.device_params.connection_type

        if center_command.device_report:
            center_command_pb.device_report.start = center_command.device_report.start
            center_command_pb.device_report.end = center_command.device_report.end

        if center_command.device_sleep:
            center_command_pb.device_sleep.start = center_command.device_sleep.start
            center_command_pb.device_sleep.end = center_command.device_sleep.end

        if center_command.relay:
            center_command_pb.relay = center_command.relay

        if center_command.custom_field:
            for custom_field in center_command.custom_field.all():
                custom_field_pb = OVTSProto_pb2.custom_struct()
                custom_field_pb.key = custom_field.key
                custom_field_pb.value = custom_field.value

                center_command_pb.custom_field.append(custom_field_pb)

        ce_bytes = center_command_pb.SerializeToString()
        return base64.b64encode(ce_bytes).decode()

    def post(self, request, *args, **kwargs):
        new_request = request.data
        serializer = CenterCommandsSerializer(data=new_request)
        if serializer.is_valid():
            center_command = serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        center_command.b64_data = self.generate_b64_cc(center_command)
        center_command.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PingView(APIView):
    def get(self, request):
        return Response(OK_RESPOND, status=status.HTTP_200_OK)

    def post(self, request):
        return Response(OK_RESPOND, status=status.HTTP_200_OK)


class TimeView(APIView):
    def get(self, request):
        return Response(str(int(timezone.now().timestamp())), status=status.HTTP_200_OK)


class DeviceReportHandler:
    ReportQueue = Queue()

    @staticmethod
    def save_datas(device_object, request_ip, b64datas):
        device_data_models = []
        threads = []
        for b64data in b64datas:
            if DeviceDataHandler.b64decode(b64data):
                DeviceDataHandler.save_data(
                    device_object, request_ip, b64data, True)
        # get results
        for thread in threads:
            thread.wait()
            device_data_models.append(thread.get())
        return device_data_models

    @classmethod
    def Check(cls):
        while(True):
            if not cls.ReportQueue.empty():
                report = cls.ReportQueue.get()
                decompressedFile = gzip.decompress(
                    report['report_data']).decode()

                # split data to a list of b64data
                b64datas = list(filter(None, decompressedFile.split('\n')))
                report_model = DeviceReportModel(
                    device_id=report['device_object'], ip=report['request_ip'])
                report_model.report_file.save(
                    "Report_{}.txt.gz".format(timezone.now()), ContentFile(report['report_data']))

                device_data_models = cls.save_datas(
                    report['device_object'], report['request_ip'], b64datas)
                report_model.device_datas.set(device_data_models)
                report_model.save()
                print("Report {} Processed!".format(report_model))
            sleep(.1)

    @classmethod
    def run(cls):
        thr = threading.Thread(target=cls.Check)
        thr.daemon = True
        thr.start()


class DeviceReportView(generics.ListCreateAPIView):
    queryset = DeviceReportModel.objects.all()
    serializer_class = DeviceReportSerializer
    DeviceReportHandler.run()

    def post(self, request):
        if ('device_id' not in request.data) or (not DeviceInfo.objects.filter(device_id=request.data['device_id']).exists()):
            return Response(NOT_FOUND, status=status.HTTP_400_BAD_REQUEST)
        device_object = DeviceInfo.objects.get(
            device_id=request.data['device_id'])
        request_ip, _ = get_client_ip(request)
        report_data_b64 = request.data['report_data'].replace(" ", "+")
        report_data_bytes = DeviceDataHandler.b64decode(
            report_data_b64)
        report = {
            'device_object': DeviceInfo.objects.get(device_id=request.data['device_id']),
            'request_ip': request_ip,
            'report_data': report_data_bytes if report_data_bytes else b'',
        }
        # add request to ReportQueue
        DeviceReportHandler.ReportQueue.put(report)
        return Response(OK_RESPOND, status.HTTP_201_CREATED)
