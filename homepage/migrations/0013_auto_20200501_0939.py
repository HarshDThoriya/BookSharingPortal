# Generated by Django 3.0.3 on 2020-05-01 04:09

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0012_auto_20200430_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminfo',
            name='post_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 9, 39, 35, 892325), null=True),
        ),
        migrations.RemoveField(
            model_name='iteminfo',
            name='user',
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
