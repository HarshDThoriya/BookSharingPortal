# Generated by Django 3.0.3 on 2020-04-30 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20200430_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteminfo',
            name='user',
        ),
        migrations.AlterField(
            model_name='iteminfo',
            name='post_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 23, 3, 47, 624451), null=True),
        ),
    ]
