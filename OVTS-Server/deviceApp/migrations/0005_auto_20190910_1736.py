# Generated by Django 2.2.4 on 2019-09-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deviceApp', '0004_auto_20190910_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicerawdatamodel',
            name='b64_data',
            field=models.CharField(max_length=1024, unique=True),
        ),
    ]