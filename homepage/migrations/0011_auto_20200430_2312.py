# Generated by Django 3.0.3 on 2020-04-30 17:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0010_auto_20200430_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminfo',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='iteminfo',
            name='post_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 23, 12, 24, 380867), null=True),
        ),
    ]