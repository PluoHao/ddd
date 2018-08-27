# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-21 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=50, verbose_name='收货人')),
                ('ads', models.CharField(max_length=300, verbose_name='地址')),
                ('phone', models.CharField(max_length=11, verbose_name='手机')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo')),
            ],
        ),
    ]