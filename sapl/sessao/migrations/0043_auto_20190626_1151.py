# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-26 14:51
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


def congirura_tramitacoes_pautas(apps, schema_editor):
    ExpedienteMateria = apps.get_model('sessao', 'ExpedienteMateria')
    OrdemDia = apps.get_model('sessao', 'OrdemDia')

    for expediente in ExpedienteMateria.objects.all():
        expediente.tramitacao = expediente.materia.tramitacao_set.first()
        expediente.save()

    for ordemdia in OrdemDia.objects.all():
        ordemdia.tramitacao = ordemdia.materia.tramitacao_set.first()
        ordemdia.save()


class Migration(migrations.Migration):
    dependencies = [
        ('materia', '0050_auto_20190521_1148'),
        ('sessao', '0042_merge_20190612_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='expedientemateria',
            name='tramitacao',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='materia.Tramitacao'),
        ),
        migrations.AddField(
            model_name='ordemdia',
            name='tramitacao',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='materia.Tramitacao'),
        ),

        migrations.RunPython(congirura_tramitacoes_pautas),
    ]
