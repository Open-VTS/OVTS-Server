from rest_framework.test import APITestCase, APITransactionTestCase, APISimpleTestCase
from rest_framework import status
from ..proto import OVTSProto_pb2
from time import time
import base64
import random
from io import BytesIO
import gzip
from time import sleep

from ..models import DeviceInfo, DeviceRawDataModel, CenterCommandsModel


class TestDeviceData(APITestCase):
    """
    Test Device Data Methods
    """
    @classmethod
    def setUpTestData(cls):
        # add a new test device for other tests
        cls.device_object = DeviceInfo.objects.create(
            device_id=1, version="1", details="Test Device")

    def test_create_device(self):
        response = self.client.post(
            '/server/add_device/', data={"device_id": 2, "version": "1", "details": "Test Device"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check the new device exists
        self.assertTrue(DeviceInfo.objects.filter(device_id=2).exists())

    @staticmethod
    def generate_device_data():
        device_data = OVTSProto_pb2.DeviceData()
        device_data.device_id = 1
        device_data.time = int(time())
        device_data.gps_data.lat = random.uniform(1, 60)
        device_data.gps_data.lng = random.uniform(1, 60)
        device_data.gps_data.speed = random.randint(0, 200)
        device_data.gps_data.altitude = random.randint(1, 100)
        device_data.gps_data.course = random.randint(0, 365)
        device_data.gps_data.hdop = random.uniform(0, 2)
        device_data.relay = random.randint(0, 1)
        device_data.input_sensor = random.randint(0, 1)
        device_data.signal_quality = random.randint(0, 5)

        device_data.center_params.center_address.device_data_url = "hello.com"
        device_data.center_params.center_address.center_commands_url = "hello.com"
        device_data.center_params.center_address.device_report_url = "hello.com"
        device_data.center_params.center_address.ping_url = "hello.com"
        device_data.center_params.number1 = "+981234567"

        device_data_encoded = device_data.SerializeToString()
        return base64.b64encode(device_data_encoded).decode()

    def test_DeviceData(self):

        # print(device_data_b64)
        device_data_b64 = self.generate_device_data()
        response = self.client.post(
            '/device/data/', data={'device_id': 1, 'data': device_data_b64})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # device_object = DeviceInfo.objects.get(device_id=1)
        self.assertTrue(DeviceRawDataModel.objects.filter(
            device_object=self.device_object, b64_data=device_data_b64).exists())


class TestCenterCommands(APITestCase):
    """
    Test Center Command Method
    """
    @classmethod
    def setUpTestData(cls):
        # add a new test device for other tests
        cls.device_object = DeviceInfo.objects.create(
            device_id=1, version="1", details="Test Device")

    def test_CenterCommands(self):
        self.SetCenterCommands()
        response = self.client.post(
            '/device/commands/', data={'device_id': '1'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CenterCommandsModel.objects.filter(
            device_object=self.device_object, b64_data=response.content.decode().strip('"')).exists())

        # get command again
        response = self.client.post(
            '/device/commands/', data={'device_id': '1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode().strip('"'), "Tm90Rm91bmQ=")

    def SetCenterCommands(self):
        data = {
            "relay": 1,
            "device_object": 1,
            "set_center_params":
            {
                "key": "Mykey",
                "center_params": {
                    "center_address":
                    {
                        "device_data_url": "hello.com",
                        "center_commands_url": "hello.com",
                        "device_report_url": "hello.com",
                        "ping_url": "hello.com"
                    },
                    "number1": "+98",
                    "number2": "123"
                }
            },

            "device_params": {
                "timer":
                {
                    "network_send": 100,
                    "network_receive": 200,
                    "sms_send": 300
                },
                "data_select":
                {
                    "gps_enable": 1,
                    "imu_enable": 1,
                    "relay_enable": 0,
                    "input_sensor_enable": 1,
                    "sim_balance_enable": 0,
                    "battery_enable": 0,
                    "signal_quality_enable": 0
                },
                "connection_type": 1
            },
            "device_report": {
                "start": 100,
                "end": 100
            },
        }

        response = self.client.post(
            '/server/center_commands/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestDeviceReport(APITestCase):
    """
    Test Device Report Method
    """
    @classmethod
    def setUpTestData(cls):
        # add a new test device for other tests
        cls.device_object = DeviceInfo.objects.create(
            device_id=1, version="1", details="Test Device")

    def test_Report(self):
        # generate device data
        device_data = ''
        for i in range(10):
            device_data += TestDeviceData.generate_device_data() + '\n'

        buf = BytesIO()
        compressed = gzip.GzipFile(fileobj=buf, mode="wb")
        compressed.write(device_data.encode())
        compressed.close()
        b64data = base64.b64encode(buf.getvalue()).decode()
        data = {
            "device_id": 1,
            "report_data": b64data
        }
        response = self.client.post(
            '/device/reports/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.content.decode().strip('"'), "T0s=")
