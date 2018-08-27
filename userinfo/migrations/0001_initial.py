# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-21 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50, verbose_name='用户名')),
                ('upassworld', models.CharField(max_length=200, verbose_name='密码')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='注册时间')),
                ('isben', models.BooleanField(default=False, verbose_name='禁用')),
                ('isdelete', models.BooleanField(default=False, verbose_name='删除')),
            ],
        ),
    ]