# Generated by Django 2.2.4 on 2019-09-10 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deviceApp', '0003_devicereportmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicereportmodel',
            old_name='device_object',
            new_name='device_id',
        ),
    ]
