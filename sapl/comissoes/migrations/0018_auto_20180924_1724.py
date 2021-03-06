# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-24 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissoes', '0017_auto_20180717_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargocomissao',
            name='unico',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Único'),
        ),
        migrations.AlterField(
            model_name='comissao',
            name='unidade_deliberativa',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Unidade Deliberativa'),
        ),
    ]
