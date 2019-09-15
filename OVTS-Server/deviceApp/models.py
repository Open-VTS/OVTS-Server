from django.db import models
from django.utils import timezone


class DeviceInfo(models.Model):
    """
    The Model for each device
    device_id: ID of device
    version: Version of firmware uploaded to device
    details: More info about device
    """
    device_id = models.PositiveIntegerField(primary_key=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    details = models.CharField(max_length=512, blank=True, null=True)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.device_id)


class IMUModel(models.Model):
    """
    Model of IMU 9-axis Sensor
    a. : Accelerometer
    g. : Gyroscope
    m. : Magnometer
    """
    ax = models.FloatField()
    ay = models.FloatField()
    az = models.FloatField()
    gx = models.FloatField()
    gy = models.FloatField()
    gz = models.FloatField()
    mx = models.FloatField()
    my = models.FloatField()
    mz = models.FloatField()


class GPSModel(models.Model):
    """
    GPS Data Model
    lat: Latitude
    lng: Longitude
    speed: Speed
    altitude: Altitude
    course: Course (0 to 360)
    hdop: HDOP Accuracy
    """
    lat = models.FloatField()
    lng = models.FloatField()
    speed = models.FloatField()
    altitude = models.FloatField()
    course = models.FloatField()
    hdop = models.FloatField()


class BatteryModel(models.Model):
    """
    Battery Data Model
    capacity: Capacity of built-in battery percentage
    plugged: Is Device plugged into charger (1 Plugged, -1 Unplugged)
    """
    capacity = models.FloatField()
    plugged = models.IntegerField()


class TimerModel(models.Model):
    """
    Device Timer Model (seconds)
    network_send: Interval for send requests to server (Device Data)
    network_receive: Interval for get commands (Center Commands)
    sms_send: Interval for send sms messages (Device Data)
    """
    network_send = models.IntegerField()
    network_receive = models.IntegerField()
    sms_send = models.IntegerField()


class DataSelectModel(models.Model):
    """
    Data Enable Models
    Enable each field to receive that data from device
    1: Enable
    -1: Disable
    """
    gps_enable = models.IntegerField()
    imu_enable = models.IntegerField()
    relay_enable = models.IntegerField()
    input_sensor_enable = models.IntegerField()
    sim_balance_enable = models.IntegerField()
    battery_enable = models.IntegerField()
    signal_quality_enable = models.IntegerField()


class DeviceParamsModel(models.Model):
    """
    Device Parameter Model
    connection_type: Device Connection Type selector
    1: Network
    2: SMS
    3: DUAL Mode
    """
    timer = models.ForeignKey(TimerModel, on_delete=models.CASCADE)
    data_select = models.ForeignKey(DataSelectModel, on_delete=models.CASCADE)
    connection_type = models.IntegerField()


class CustomFieldModel(models.Model):
    """
    Custom Key Value pair data
    """
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=1024)


class CenterAddressModel(models.Model):
    """
    Center (Server) Address Model
    device_data_url: Device Data URL
    center_commands_url: Center Commands URL
    device_report_url: Device Report URL
    ping_url: Center Ping URL
    """
    device_data_url = models.CharField(max_length=100)
    center_commands_url = models.CharField(max_length=100)
    device_report_url = models.CharField(max_length=100)
    ping_url = models.CharField(max_length=100)


class CenterParamsModel(models.Model):
    """
    number(1..3): Center Phone Number for SMS
    """
    center_address = models.ForeignKey(
        CenterAddressModel, on_delete=models.CASCADE, blank=True, null=True)
    number1 = models.CharField(max_length=100)
    number2 = models.CharField(max_length=100, blank=True, null=True)
    number3 = models.CharField(max_length=100, blank=True, null=True)


class ReportSetModel(models.Model):
    """
    Get Manual Report Model
    start: from time (timestamp)
    end: to time (timestamp)
    """
    start = models.IntegerField()
    end = models.IntegerField()


class SleepSetModel(models.Model):
    """
    Device Set Sleep Model
    start: from time (timestamp)
    end: to time (timestamp)
    """
    start = models.IntegerField()
    end = models.IntegerField()


class SetCenterParamsModel(models.Model):
    """
    Device Set Center Params Model
    key: Device Authentication key
    """
    key = models.CharField(max_length=64)
    center_params = models.ForeignKey(
        CenterParamsModel, on_delete=models.CASCADE)


class DeviceRawDataModel(models.Model):
    """
    Device Raw Data Model
    b64_data: Base64 Device Data raw value
    ip: IP Address of HTTP request
    """
    device_object = models.ForeignKey(
        DeviceInfo, on_delete=models.CASCADE)
    b64_data = models.CharField(max_length=2048)
    ip = models.GenericIPAddressField()
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('device_object', 'b64_data',)

    def __str__(self):
        return self.b64_data


class DeviceDataModel(models.Model):
    """
    Device Data Model
    time: current timestamp of DeviceData
    relay: Current Relay Value (1: Enable, -1: Disable)
    input_sensor: Current state of input voltage sensor (1: Enable, -1: Disable)
    sim_balance: Simcard balance value.
    signal_quality: Signal quality of Modem in the Device (range between 0 to 5)
    center_params: Center Parameters of device
    device_params: Device Parameters
    custom_field: Custom field Key/Value pair
    """
    raw_data = models.OneToOneField(
        DeviceRawDataModel, on_delete=models.CASCADE, primary_key=True)
    time = models.IntegerField()
    gps_data = models.ForeignKey(
        GPSModel, on_delete=models.CASCADE, blank=True, null=True)
    imu_data = models.ForeignKey(
        IMUModel, on_delete=models.CASCADE, blank=True, null=True)
    battery_data = models.ForeignKey(
        BatteryModel, on_delete=models.CASCADE, blank=True, null=True)
    relay = models.IntegerField(blank=True, null=True)
    input_sensor = models.IntegerField(blank=True, null=True)
    sim_balance = models.IntegerField(blank=True, null=True)
    signal_quality = models.IntegerField(blank=True, null=True)
    center_params = models.ForeignKey(
        CenterParamsModel, on_delete=models.CASCADE, blank=True, null=True)
    device_params = models.ForeignKey(
        DeviceParamsModel, on_delete=models.CASCADE, blank=True, null=True)
    custom_field = models.ManyToManyField(
        CustomFieldModel, blank=True)

    def __str__(self):
        return str(self.raw_data)


class DeviceDataReportModel(models.Model):
    """
    Device Data that comes from device report file
    Same as DeviceDataModel
    """
    raw_data = models.OneToOneField(
        DeviceRawDataModel, on_delete=models.CASCADE, primary_key=True)
    time = models.IntegerField()
    gps_data = models.ForeignKey(
        GPSModel, on_delete=models.CASCADE, blank=True, null=True)
    imu_data = models.ForeignKey(
        IMUModel, on_delete=models.CASCADE, blank=True, null=True)
    battery_data = models.ForeignKey(
        BatteryModel, on_delete=models.CASCADE, blank=True, null=True)
    relay = models.IntegerField(blank=True, null=True)
    input_sensor = models.IntegerField(blank=True, null=True)
    sim_balance = models.IntegerField(blank=True, null=True)
    signal_quality = models.IntegerField(blank=True, null=True)
    center_params = models.ForeignKey(
        CenterParamsModel, on_delete=models.CASCADE, blank=True, null=True)
    device_params = models.ForeignKey(
        DeviceParamsModel, on_delete=models.CASCADE, blank=True, null=True)
    custom_field = models.ManyToManyField(
        CustomFieldModel, blank=True)

    def __str__(self):
        return str(self.raw_data)


class DeviceReportModel(models.Model):
    """
    Device Report Model
    report_file: Device Report uploaded file
    device_datas: DeviceData extracted from report_file
    """
    device_id = models.ForeignKey(
        DeviceInfo, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    created_time = models.DateTimeField(default=timezone.now)
    report_file = models.FileField(upload_to="DeviceReport")
    device_datas = models.ManyToManyField(DeviceDataReportModel)

    def __str__(self):
        return str(self.id)

## Center Params


class CenterCommandsModel(models.Model):
    """
    Center Commands Model
    set_center_params: Set Center params
    device_params: Set Device params
    device_report: Set Device report value to get reports manually
    device_sleep: Set sleep timer for device
    relay: Set relay value for device (1: Enable, -1: Disable)
    custom_field: Set Custom Field command for device
    received: Will be set to true if device already received the current center command 
    received_time: Will be set to the time that device received the center command
    b64_data: Base64 of the data that return to the device
    """
    device_object = models.ForeignKey(
        DeviceInfo, on_delete=models.CASCADE)
    set_center_params = models.ForeignKey(
        SetCenterParamsModel, on_delete=models.CASCADE, blank=True, null=True)
    device_params = models.ForeignKey(
        DeviceParamsModel, on_delete=models.CASCADE, blank=True, null=True)
    device_report = models.ForeignKey(
        ReportSetModel, on_delete=models.CASCADE, blank=True, null=True)
    device_sleep = models.ForeignKey(
        SleepSetModel, on_delete=models.CASCADE, blank=True, null=True)
    relay = models.IntegerField(blank=True, null=True)
    custom_field = models.ManyToManyField(
        CustomFieldModel, blank=True)
    received = models.BooleanField(default=False)
    received_time = models.DateTimeField(blank=True, null=True)
    created_time = models.DateTimeField(default=timezone.now)
    b64_data = models.CharField(max_length=2048)

    def __str__(self):
        return str(self.id)


class DeviceCenterCommandsModel(models.Model):
    """
    Device Center Commands Model
    center_command: Center Command that needs to be returned to device
    """
    center_command = models.OneToOneField(
        CenterCommandsModel, on_delete=models.CASCADE, primary_key=True)
    device_object = models.ForeignKey(
        DeviceInfo, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.center_command)
