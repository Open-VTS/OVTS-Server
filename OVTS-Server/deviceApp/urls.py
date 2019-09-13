from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('server/add_device/', AddDeviceView.as_view()),
    path('server/device_data/', DeviceDataView.as_view()),
    path('server/center_commands/', CenterCommandsView.as_view()),
    path('device/data/', DeviceRawDataView.as_view()),
    path('device/commands/', CenterCommandsDeviceView.as_view()),
    path('device/time/', TimeView.as_view()),
    path('device/reports/', DeviceReportView.as_view()),
    path('ping/', PingView.as_view()),
    path('', PingView.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)
