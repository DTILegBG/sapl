# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-11 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0034_delete_frenteparlamentar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parlamentar',
            name='ativo',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], db_index=True, default=False, verbose_name='Ativo na Casa?'),
        ),
    ]
