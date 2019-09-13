from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(DeviceInfo)
admin.site.register(DeviceRawDataModel)
admin.site.register(IMUModel)
admin.site.register(GPSModel)
admin.site.register(BatteryModel)
admin.site.register(TimerModel)
admin.site.register(DeviceParamsModel)
admin.site.register(CustomFieldModel)
admin.site.register(CenterAddressModel)
admin.site.register(DeviceDataModel)
admin.site.register(CenterCommandsModel)
admin.site.register(DeviceCenterCommandsModel)
admin.site.register(SetCenterParamsModel)
admin.site.register(SleepSetModel)
admin.site.register(ReportSetModel)
admin.site.register(CenterParamsModel)
admin.site.register(DataSelectModel)
admin.site.register(DeviceReportModel)

