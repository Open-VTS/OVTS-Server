# Generated by Django 2.2.4 on 2019-09-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deviceApp', '0011_remove_devicerawdatamodel_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='centercommandsmodel',
            name='received_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
