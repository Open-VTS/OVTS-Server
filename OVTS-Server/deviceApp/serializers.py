from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class DeviceDataRawSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceRawDataModel
        fields = '__all__'
        read_only_fields = ('created_time', 'ip',)


class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceDataModel
        fields = '__all__'


class DeviceCenterCommandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCenterCommandsModel
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    device_id = serializers.SlugRelatedField(
        queryset=DeviceInfo.objects.all(),
        slug_field='device_id',
    )

    class Meta:
        model = DeviceInfo
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSetModel
        fields = '__all__'


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepSetModel
        fields = '__all__'


class CenterAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterAddressModel
        fields = '__all__'


class CenterParamsSerializer(serializers.ModelSerializer):
    center_address = CenterAddressSerializer(required=False, allow_null=True)

    class Meta:
        model = CenterParamsModel
        fields = '__all__'


class SetCenterParamsSerializer(serializers.ModelSerializer):
    center_params = CenterParamsSerializer(required=False, allow_null=True)

    class Meta:
        model = SetCenterParamsModel
        fields = '__all__'


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerModel
        fields = '__all__'


class DataSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSelectModel
        fields = '__all__'


class DeviceParamsSerializer(serializers.ModelSerializer):
    timer = TimerSerializer()
    data_select = DataSelectSerializer()

    class Meta:
        model = DeviceParamsModel
        fields = '__all__'


class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFieldModel
        fields = '__all__'


class CenterCommandsSerializer(serializers.ModelSerializer):
    device_object = serializers.SlugRelatedField(
        queryset=DeviceInfo.objects.all(),
        slug_field='device_id',
    )

    set_center_params = SetCenterParamsSerializer(
        required=False, allow_null=True)
    device_params = DeviceParamsSerializer(required=False, allow_null=True)
    device_report = ReportSerializer(required=False, allow_null=True)
    device_sleep = SleepSerializer(required=False, allow_null=True)
    custom_field = CustomFieldSerializer(
        required=False, allow_null=True, many=True)

    class Meta:
        model = CenterCommandsModel
        fields = '__all__'
        read_only_fields = ('b64_data', 'received')

    def create(self, validated_data):
        # print(validated_data)

        set_center_params = validated_data.pop('set_center_params', None)
        device_params = validated_data.pop('device_params', None)

        device_report_data = validated_data.pop('device_report', None)
        device_sleep_data = validated_data.pop('device_sleep', None)
        custom_field_data = validated_data.pop('custom_field', None)

        if set_center_params:
            center_address = set_center_params['center_params'].pop(
                'center_address', None)
            if center_address:
                set_center_params['center_params']['center_address'], _ = CenterAddressModel.objects.get_or_create(
                    **center_address)

            set_center_params['center_params'], _ = CenterParamsModel.objects.get_or_create(
                **set_center_params['center_params'])

            validated_data['set_center_params'], _ = SetCenterParamsModel.objects.get_or_create(
                **set_center_params)

        if device_params:
            device_params['timer'], _ = TimerModel.objects.get_or_create(
                **device_params['timer'])
            device_params['data_select'], _ = DataSelectModel.objects.get_or_create(
                **device_params['data_select'])

            validated_data['device_params'], _ = DeviceParamsModel.objects.get_or_create(
                **device_params)

        if device_sleep_data:
            validated_data['device_sleep'], _ = SleepSetModel.objects.get_or_create(
                **device_sleep_data)

        if device_report_data:
            validated_data['device_report'], _ = ReportSetModel.objects.get_or_create(
                **device_report_data)

        center_command = CenterCommandsModel.objects.create(
            **validated_data)

        if custom_field_data:
            custom_field_objs = []
            for field in custom_field_data:
                custom_field_obj = CustomFieldModel.objects.get_or_create(
                    **field)
                custom_field_objs.append(custom_field_obj)

            center_command.custom_field.add(*custom_field_objs)

        return center_command


class AddDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = '__all__'
        read_only_fields = ('created_time',)


class DeviceReportSerializer(serializers.ModelSerializer):
    device_id = serializers.SlugRelatedField(
        queryset=DeviceInfo.objects.all(),
        slug_field='device_id',
    )

    class Meta:
        model = DeviceReportModel
        fields = '__all__'
        read_only_fields = ('created_time', 'ip', 'device_datas')
