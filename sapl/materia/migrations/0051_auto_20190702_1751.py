# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-02 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0050_auto_20190521_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tramitacao',
            options={
                'ordering': ['-id', '-timestamp', '-data_tramitacao'],
                'verbose_name': 'Tramitação',
                'verbose_name_plural': 'Tramitações'
            },
        ),
    ]
