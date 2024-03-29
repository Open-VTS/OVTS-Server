# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OVTSProto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='OVTSProto.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0fOVTSProto.proto\"+\n\rcustom_struct\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"V\n\x13\x64\x65vice_timer_struct\x12\x14\n\x0cnetwork_send\x18\x01 \x02(\x05\x12\x17\n\x0fnetwork_receive\x18\x02 \x02(\x05\x12\x10\n\x08sms_send\x18\x03 \x02(\x05\"\xc9\x01\n\x19\x64\x65vice_data_select_struct\x12\x12\n\ngps_enable\x18\x01 \x02(\x05\x12\x12\n\nimu_enable\x18\x02 \x02(\x05\x12\x14\n\x0crelay_enable\x18\x03 \x02(\x05\x12\x1b\n\x13input_sensor_enable\x18\x04 \x02(\x05\x12\x1a\n\x12sim_balance_enable\x18\x05 \x02(\x05\x12\x16\n\x0e\x62\x61ttery_enable\x18\x06 \x02(\x05\x12\x1d\n\x15signal_quality_enable\x18\x07 \x02(\x05\"\x85\x01\n\x14\x64\x65vice_params_struct\x12#\n\x05timer\x18\x01 \x02(\x0b\x32\x14.device_timer_struct\x12/\n\x0b\x64\x61ta_select\x18\x02 \x02(\x0b\x32\x1a.device_data_select_struct\x12\x17\n\x0f\x63onnection_type\x18\x03 \x02(\x05\"z\n\x15\x63\x65nter_address_struct\x12\x17\n\x0f\x64\x65vice_data_url\x18\x01 \x02(\t\x12\x1b\n\x13\x63\x65nter_commands_url\x18\x02 \x02(\t\x12\x19\n\x11\x64\x65vice_report_url\x18\x03 \x02(\t\x12\x10\n\x08ping_url\x18\x04 \x02(\t\"y\n\x14\x63\x65nter_params_struct\x12.\n\x0e\x63\x65nter_address\x18\x01 \x01(\x0b\x32\x16.center_address_struct\x12\x0f\n\x07number1\x18\x02 \x02(\t\x12\x0f\n\x07number2\x18\x03 \x01(\t\x12\x0f\n\x07number3\x18\x04 \x01(\t\"\xb1\x05\n\nDeviceData\x12\x11\n\tdevice_id\x18\x01 \x02(\x05\x12\x0c\n\x04time\x18\x02 \x02(\x03\x12-\n\x08gps_data\x18\x03 \x01(\x0b\x32\x1b.DeviceData.gps_data_struct\x12-\n\x08imu_data\x18\x04 \x01(\x0b\x32\x1b.DeviceData.imu_data_struct\x12\r\n\x05relay\x18\x05 \x01(\x05\x12\x14\n\x0cinput_sensor\x18\x06 \x01(\x05\x12\x13\n\x0bsim_balance\x18\x07 \x01(\x05\x12\x30\n\x0c\x62\x61ttery_data\x18\x08 \x01(\x0b\x32\x1a.DeviceData.battery_struct\x12\x16\n\x0esignal_quality\x18\t \x01(\x05\x12,\n\rcenter_params\x18\n \x01(\x0b\x32\x15.center_params_struct\x12,\n\rdevice_params\x18\x0b \x01(\x0b\x32\x15.device_params_struct\x12$\n\x0c\x63ustom_field\x18\x0c \x03(\x0b\x32\x0e.custom_struct\x1a}\n\x0fimu_data_struct\x12\n\n\x02\x61x\x18\x01 \x02(\x02\x12\n\n\x02\x61y\x18\x02 \x02(\x02\x12\n\n\x02\x61z\x18\x03 \x02(\x02\x12\n\n\x02gx\x18\x04 \x02(\x02\x12\n\n\x02gy\x18\x05 \x02(\x02\x12\n\n\x02gz\x18\x06 \x02(\x02\x12\n\n\x02mx\x18\x07 \x02(\x02\x12\n\n\x02my\x18\x08 \x02(\x02\x12\n\n\x02mz\x18\t \x02(\x02\x1aj\n\x0fgps_data_struct\x12\x0b\n\x03lat\x18\x01 \x02(\x02\x12\x0b\n\x03lng\x18\x02 \x02(\x02\x12\r\n\x05speed\x18\x03 \x02(\x01\x12\x10\n\x08\x61ltitude\x18\x04 \x02(\x01\x12\x0e\n\x06\x63ourse\x18\x05 \x02(\x01\x12\x0c\n\x04hdop\x18\x06 \x02(\x01\x1a\x33\n\x0e\x62\x61ttery_struct\x12\x10\n\x08\x63\x61pacity\x18\x01 \x02(\x02\x12\x0f\n\x07plugged\x18\x02 \x02(\x05\"\xe5\x03\n\x0e\x43\x65nterCommands\x12\x11\n\tdevice_id\x18\x01 \x02(\x05\x12\x43\n\x11set_center_params\x18\x02 \x01(\x0b\x32(.CenterCommands.set_center_params_struct\x12,\n\rdevice_params\x18\x03 \x01(\x0b\x32\x15.device_params_struct\x12\x34\n\rdevice_report\x18\x04 \x01(\x0b\x32\x1d.CenterCommands.report_struct\x12\x32\n\x0c\x64\x65vice_sleep\x18\x05 \x01(\x0b\x32\x1c.CenterCommands.sleep_struct\x12\r\n\x05relay\x18\x06 \x01(\x05\x12$\n\x0c\x63ustom_field\x18\x07 \x03(\x0b\x32\x0e.custom_struct\x1a+\n\rreport_struct\x12\r\n\x05start\x18\x01 \x02(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x02(\x03\x1a*\n\x0csleep_struct\x12\r\n\x05start\x18\x01 \x02(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x02(\x03\x1aU\n\x18set_center_params_struct\x12\x0b\n\x03key\x18\x01 \x02(\t\x12,\n\rcenter_params\x18\x02 \x02(\x0b\x32\x15.center_params_struct')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CUSTOM_STRUCT = _descriptor.Descriptor(
  name='custom_struct',
  full_name='custom_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='custom_struct.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='custom_struct.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=62,
)


_DEVICE_TIMER_STRUCT = _descriptor.Descriptor(
  name='device_timer_struct',
  full_name='device_timer_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_send', full_name='device_timer_struct.network_send', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='network_receive', full_name='device_timer_struct.network_receive', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sms_send', full_name='device_timer_struct.sms_send', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=150,
)


_DEVICE_DATA_SELECT_STRUCT = _descriptor.Descriptor(
  name='device_data_select_struct',
  full_name='device_data_select_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gps_enable', full_name='device_data_select_struct.gps_enable', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imu_enable', full_name='device_data_select_struct.imu_enable', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relay_enable', full_name='device_data_select_struct.relay_enable', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_sensor_enable', full_name='device_data_select_struct.input_sensor_enable', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sim_balance_enable', full_name='device_data_select_struct.sim_balance_enable', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_enable', full_name='device_data_select_struct.battery_enable', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal_quality_enable', full_name='device_data_select_struct.signal_quality_enable', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=354,
)


_DEVICE_PARAMS_STRUCT = _descriptor.Descriptor(
  name='device_params_struct',
  full_name='device_params_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timer', full_name='device_params_struct.timer', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_select', full_name='device_params_struct.data_select', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connection_type', full_name='device_params_struct.connection_type', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=490,
)


_CENTER_ADDRESS_STRUCT = _descriptor.Descriptor(
  name='center_address_struct',
  full_name='center_address_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_data_url', full_name='center_address_struct.device_data_url', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center_commands_url', full_name='center_address_struct.center_commands_url', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_report_url', full_name='center_address_struct.device_report_url', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping_url', full_name='center_address_struct.ping_url', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=614,
)


_CENTER_PARAMS_STRUCT = _descriptor.Descriptor(
  name='center_params_struct',
  full_name='center_params_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='center_address', full_name='center_params_struct.center_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number1', full_name='center_params_struct.number1', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number2', full_name='center_params_struct.number2', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number3', full_name='center_params_struct.number3', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=616,
  serialized_end=737,
)


_DEVICEDATA_IMU_DATA_STRUCT = _descriptor.Descriptor(
  name='imu_data_struct',
  full_name='DeviceData.imu_data_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ax', full_name='DeviceData.imu_data_struct.ax', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ay', full_name='DeviceData.imu_data_struct.ay', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='az', full_name='DeviceData.imu_data_struct.az', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gx', full_name='DeviceData.imu_data_struct.gx', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gy', full_name='DeviceData.imu_data_struct.gy', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gz', full_name='DeviceData.imu_data_struct.gz', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mx', full_name='DeviceData.imu_data_struct.mx', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='my', full_name='DeviceData.imu_data_struct.my', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mz', full_name='DeviceData.imu_data_struct.mz', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1143,
  serialized_end=1268,
)

_DEVICEDATA_GPS_DATA_STRUCT = _descriptor.Descriptor(
  name='gps_data_struct',
  full_name='DeviceData.gps_data_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='DeviceData.gps_data_struct.lat', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lng', full_name='DeviceData.gps_data_struct.lng', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed', full_name='DeviceData.gps_data_struct.speed', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='DeviceData.gps_data_struct.altitude', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='course', full_name='DeviceData.gps_data_struct.course', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hdop', full_name='DeviceData.gps_data_struct.hdop', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1270,
  serialized_end=1376,
)

_DEVICEDATA_BATTERY_STRUCT = _descriptor.Descriptor(
  name='battery_struct',
  full_name='DeviceData.battery_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capacity', full_name='DeviceData.battery_struct.capacity', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plugged', full_name='DeviceData.battery_struct.plugged', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1378,
  serialized_end=1429,
)

_DEVICEDATA = _descriptor.Descriptor(
  name='DeviceData',
  full_name='DeviceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='DeviceData.device_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='DeviceData.time', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_data', full_name='DeviceData.gps_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imu_data', full_name='DeviceData.imu_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relay', full_name='DeviceData.relay', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_sensor', full_name='DeviceData.input_sensor', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sim_balance', full_name='DeviceData.sim_balance', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery_data', full_name='DeviceData.battery_data', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal_quality', full_name='DeviceData.signal_quality', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center_params', full_name='DeviceData.center_params', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_params', full_name='DeviceData.device_params', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_field', full_name='DeviceData.custom_field', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEDATA_IMU_DATA_STRUCT, _DEVICEDATA_GPS_DATA_STRUCT, _DEVICEDATA_BATTERY_STRUCT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=740,
  serialized_end=1429,
)


_CENTERCOMMANDS_REPORT_STRUCT = _descriptor.Descriptor(
  name='report_struct',
  full_name='CenterCommands.report_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='CenterCommands.report_struct.start', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='CenterCommands.report_struct.end', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1743,
  serialized_end=1786,
)

_CENTERCOMMANDS_SLEEP_STRUCT = _descriptor.Descriptor(
  name='sleep_struct',
  full_name='CenterCommands.sleep_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='CenterCommands.sleep_struct.start', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='CenterCommands.sleep_struct.end', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1788,
  serialized_end=1830,
)

_CENTERCOMMANDS_SET_CENTER_PARAMS_STRUCT = _descriptor.Descriptor(
  name='set_center_params_struct',
  full_name='CenterCommands.set_center_params_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='CenterCommands.set_center_params_struct.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='center_params', full_name='CenterCommands.set_center_params_struct.center_params', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1832,
  serialized_end=1917,
)

_CENTERCOMMANDS = _descriptor.Descriptor(
  name='CenterCommands',
  full_name='CenterCommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='CenterCommands.device_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_center_params', full_name='CenterCommands.set_center_params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_params', full_name='CenterCommands.device_params', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_report', full_name='CenterCommands.device_report', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_sleep', full_name='CenterCommands.device_sleep', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relay', full_name='CenterCommands.relay', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_field', full_name='CenterCommands.custom_field', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CENTERCOMMANDS_REPORT_STRUCT, _CENTERCOMMANDS_SLEEP_STRUCT, _CENTERCOMMANDS_SET_CENTER_PARAMS_STRUCT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1432,
  serialized_end=1917,
)

_DEVICE_PARAMS_STRUCT.fields_by_name['timer'].message_type = _DEVICE_TIMER_STRUCT
_DEVICE_PARAMS_STRUCT.fields_by_name['data_select'].message_type = _DEVICE_DATA_SELECT_STRUCT
_CENTER_PARAMS_STRUCT.fields_by_name['center_address'].message_type = _CENTER_ADDRESS_STRUCT
_DEVICEDATA_IMU_DATA_STRUCT.containing_type = _DEVICEDATA
_DEVICEDATA_GPS_DATA_STRUCT.containing_type = _DEVICEDATA
_DEVICEDATA_BATTERY_STRUCT.containing_type = _DEVICEDATA
_DEVICEDATA.fields_by_name['gps_data'].message_type = _DEVICEDATA_GPS_DATA_STRUCT
_DEVICEDATA.fields_by_name['imu_data'].message_type = _DEVICEDATA_IMU_DATA_STRUCT
_DEVICEDATA.fields_by_name['battery_data'].message_type = _DEVICEDATA_BATTERY_STRUCT
_DEVICEDATA.fields_by_name['center_params'].message_type = _CENTER_PARAMS_STRUCT
_DEVICEDATA.fields_by_name['device_params'].message_type = _DEVICE_PARAMS_STRUCT
_DEVICEDATA.fields_by_name['custom_field'].message_type = _CUSTOM_STRUCT
_CENTERCOMMANDS_REPORT_STRUCT.containing_type = _CENTERCOMMANDS
_CENTERCOMMANDS_SLEEP_STRUCT.containing_type = _CENTERCOMMANDS
_CENTERCOMMANDS_SET_CENTER_PARAMS_STRUCT.fields_by_name['center_params'].message_type = _CENTER_PARAMS_STRUCT
_CENTERCOMMANDS_SET_CENTER_PARAMS_STRUCT.containing_type = _CENTERCOMMANDS
_CENTERCOMMANDS.fields_by_name['set_center_params'].message_type = _CENTERCOMMANDS_SET_CENTER_PARAMS_STRUCT
_CENTERCOMMANDS.fields_by_name['device_params'].message_type = _DEVICE_PARAMS_STRUCT
_CENTERCOMMANDS.fields_by_name['device_report'].message_type = _CENTERCOMMANDS_REPORT_STRUCT
_CENTERCOMMANDS.fields_by_name['device_sleep'].message_type = _CENTERCOMMANDS_SLEEP_STRUCT
_CENTERCOMMANDS.fields_by_name['custom_field'].message_type = _CUSTOM_STRUCT
DESCRIPTOR.message_types_by_name['custom_struct'] = _CUSTOM_STRUCT
DESCRIPTOR.message_types_by_name['device_timer_struct'] = _DEVICE_TIMER_STRUCT
DESCRIPTOR.message_types_by_name['device_data_select_struct'] = _DEVICE_DATA_SELECT_STRUCT
DESCRIPTOR.message_types_by_name['device_params_struct'] = _DEVICE_PARAMS_STRUCT
DESCRIPTOR.message_types_by_name['center_address_struct'] = _CENTER_ADDRESS_STRUCT
DESCRIPTOR.message_types_by_name['center_params_struct'] = _CENTER_PARAMS_STRUCT
DESCRIPTOR.message_types_by_name['DeviceData'] = _DEVICEDATA
DESCRIPTOR.message_types_by_name['CenterCommands'] = _CENTERCOMMANDS

custom_struct = _reflection.GeneratedProtocolMessageType('custom_struct', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOM_STRUCT,
  __module__ = 'OVTSProto_pb2'
  # @@protoc_insertion_point(class_scope:custom_struct)
  ))
_sym_db.RegisterMessage(custom_struct)

device_timer_struct = _reflection.GeneratedProtocolMessageType('device_timer_struct', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE_TIMER_STRUCT,
  __module__ = 'OVTSProto_pb2'
  # @@protoc_insertion_point(class_scope:device_timer_struct)
  ))
_sym_db.RegisterMessage(device_timer_struct)

device_data_select_struct = _reflection.GeneratedProtocolMessageType('device_data_select_struct', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE_DATA_SELECT_STRUCT,
  __module__ = 'OVTSProto_pb2'
  # @@protoc_insertion_point(class_scope:device_data_select_struct)
  ))
_sym_db.RegisterMessage(device_data_select_struct)

device_params_struct = _reflection.GeneratedProtocolMessageType('device_params_struct', (_message.Message,), dict(
  DESCRIPTOR = _DEVICE_PARAMS_STRUCT,
  __module__ = 'OVTSProto_pb2'
  # @@protoc_insertion_point(class_scope:device_params_struct)
  ))
_sym_db.RegisterMessage(device_params_struct)

center_address_struct = _reflection.GeneratedProtocolMessageType('center_address_struct', (_message.Message,), dict(
  DESCRIPTOR = _CENTER_ADDRESS_STRUCT,
  __module__ = 'OVTSProto_pb2'
  # @@protoc_insertion_point(class_scope:center_address_struct)
  ))
_sym_db.RegisterMessage(center_address_struct)

center_params_struct = _reflection.GeneratedProtocolMessageType('center_params_struct', (_message.Message,), dict(
  DESCRIPTOR = _CENTER_PARAMS_STRUCT,
  __module__ = 'OVTSProto_pb2'
  # @@protoc_insertion_point(class_scope:center_params_struct)
  ))
_sym_db.RegisterMessage(center_params_struct)

DeviceData = _reflection.GeneratedProtocolMessageType('DeviceData', (_message.Message,), dict(

  imu_data_struct = _reflection.GeneratedProtocolMessageType('imu_data_struct', (_message.Message,), dict(
    DESCRIPTOR = _DEVICEDATA_IMU_DATA_STRUCT,
    __module__ = 'OVTSProto_pb2'
    # @@protoc_insertion_point(class_scope:DeviceData.imu_data_struct)
    ))
  ,

  gps_data_struct = _reflection.GeneratedProtocolMessageType('gps_data_struct', (_message.Message,), dict(
    DESCRIPTOR = _DEVICEDATA_GPS_DATA_STRUCT,
    __module__ = 'OVTSProto_pb2'
    # @@protoc_insertion_point(class_scope:DeviceData.gps_data_struct)
    ))
  ,

  battery_struct = _reflection.GeneratedProtocolMessageType('battery_struct', (_message.Message,), dict(
    DESCRIPTOR = _DEVICEDATA_BATTERY_STRUCT,
    __module__ = 'OVTSProto_pb2'
    # @@protoc_insertion_point(class_scope:DeviceData.battery_struct)
    ))
  ,
  DESCRIPTOR = _DEVICEDATA,
  __module__ = 'OVTSProto_pb2'
  # @@protoc_insertion_point(class_scope:DeviceData)
  ))
_sym_db.RegisterMessage(DeviceData)
_sym_db.RegisterMessage(DeviceData.imu_data_struct)
_sym_db.RegisterMessage(DeviceData.gps_data_struct)
_sym_db.RegisterMessage(DeviceData.battery_struct)

CenterCommands = _reflection.GeneratedProtocolMessageType('CenterCommands', (_message.Message,), dict(

  report_struct = _reflection.GeneratedProtocolMessageType('report_struct', (_message.Message,), dict(
    DESCRIPTOR = _CENTERCOMMANDS_REPORT_STRUCT,
    __module__ = 'OVTSProto_pb2'
    # @@protoc_insertion_point(class_scope:CenterCommands.report_struct)
    ))
  ,

  sleep_struct = _reflection.GeneratedProtocolMessageType('sleep_struct', (_message.Message,), dict(
    DESCRIPTOR = _CENTERCOMMANDS_SLEEP_STRUCT,
    __module__ = 'OVTSProto_pb2'
    # @@protoc_insertion_point(class_scope:CenterCommands.sleep_struct)
    ))
  ,

  set_center_params_struct = _reflection.GeneratedProtocolMessageType('set_center_params_struct', (_message.Message,), dict(
    DESCRIPTOR = _CENTERCOMMANDS_SET_CENTER_PARAMS_STRUCT,
    __module__ = 'OVTSProto_pb2'
    # @@protoc_insertion_point(class_scope:CenterCommands.set_center_params_struct)
    ))
  ,
  DESCRIPTOR = _CENTERCOMMANDS,
  __module__ = 'OVTSProto_pb2'
  # @@protoc_insertion_point(class_scope:CenterCommands)
  ))
_sym_db.RegisterMessage(CenterCommands)
_sym_db.RegisterMessage(CenterCommands.report_struct)
_sym_db.RegisterMessage(CenterCommands.sleep_struct)
_sym_db.RegisterMessage(CenterCommands.set_center_params_struct)


# @@protoc_insertion_point(module_scope)
