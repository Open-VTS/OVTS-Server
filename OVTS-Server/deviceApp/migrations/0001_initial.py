# Generated by Django 2.2.4 on 2019-08-30 07:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.FloatField()),
                ('plugged', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CenterAddressModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_data_url', models.CharField(max_length=100)),
                ('center_commands_url', models.CharField(max_length=100)),
                ('device_report_url', models.CharField(max_length=100)),
                ('ping_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CenterParamsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.CharField(max_length=100)),
                ('number2', models.CharField(blank=True, max_length=100, null=True)),
                ('number3', models.CharField(blank=True, max_length=100, null=True)),
                ('center_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.CenterAddressModel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomFieldModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='DataSelectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps_enable', models.IntegerField()),
                ('imu_enable', models.IntegerField()),
                ('relay_enable', models.IntegerField()),
                ('input_sensor_enable', models.IntegerField()),
                ('sim_balance_enable', models.IntegerField()),
                ('battery_enable', models.IntegerField()),
                ('signal_quality_enable', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('device_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('version', models.CharField(blank=True, max_length=100, null=True)),
                ('details', models.CharField(blank=True, max_length=512, null=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='GPSModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('speed', models.FloatField()),
                ('altitude', models.FloatField()),
                ('course', models.FloatField()),
                ('hdop', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IMUModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ax', models.FloatField()),
                ('ay', models.FloatField()),
                ('az', models.FloatField()),
                ('gx', models.FloatField()),
                ('gy', models.FloatField()),
                ('gz', models.FloatField()),
                ('mx', models.FloatField()),
                ('my', models.FloatField()),
                ('mz', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ReportSetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SleepSetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_send', models.IntegerField()),
                ('network_receive', models.IntegerField()),
                ('sms_send', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SetCenterParamsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('center_params', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deviceApp.CenterParamsModel')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceRawDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.PositiveIntegerField()),
                ('b64_data', models.CharField(max_length=1024)),
                ('is_valid', models.BooleanField(default=False)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('device_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deviceApp.DeviceInfo')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceParamsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_type', models.IntegerField()),
                ('data_select', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deviceApp.DataSelectModel')),
                ('timer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deviceApp.TimerModel')),
            ],
        ),
        migrations.CreateModel(
            name='CenterCommandsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relay', models.IntegerField(blank=True, null=True)),
                ('received', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('b64_data', models.CharField(max_length=2048)),
                ('custom_field', models.ManyToManyField(blank=True, to='deviceApp.CustomFieldModel')),
                ('device_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deviceApp.DeviceInfo')),
                ('device_params', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.DeviceParamsModel')),
                ('device_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.ReportSetModel')),
                ('device_sleep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.SleepSetModel')),
                ('set_center_params', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.SetCenterParamsModel')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceCenterCommandsModel',
            fields=[
                ('center_command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='deviceApp.CenterCommandsModel')),
                ('device_id', models.PositiveIntegerField()),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceDataModel',
            fields=[
                ('raw_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='deviceApp.DeviceRawDataModel')),
                ('time', models.IntegerField()),
                ('relay', models.IntegerField(blank=True, null=True)),
                ('input_sensor', models.IntegerField(blank=True, null=True)),
                ('sim_balance', models.IntegerField(blank=True, null=True)),
                ('signal_quality', models.IntegerField(blank=True, null=True)),
                ('battery_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.BatteryModel')),
                ('center_params', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.CenterParamsModel')),
                ('custom_field', models.ManyToManyField(blank=True, to='deviceApp.CustomFieldModel')),
                ('device_params', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.DeviceParamsModel')),
                ('gps_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.GPSModel')),
                ('imu_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deviceApp.IMUModel')),
            ],
        ),
    ]
