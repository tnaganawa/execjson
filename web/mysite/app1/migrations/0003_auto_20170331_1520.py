# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20170330_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_id_jsons',
            name='saveid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='user_id_jsons',
            unique_together=set([('user', 'saveid')]),
        ),
    ]