# Generated by Django 3.0.3 on 2020-04-30 16:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0007_auto_20200430_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminfo',
            name='post_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 22, 27, 50, 410214), null=True),
        ),
        migrations.AlterField(
            model_name='iteminfo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
