# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-22 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(upload_to='images/goods', verbose_name='商品图片路径'),
        ),
    ]