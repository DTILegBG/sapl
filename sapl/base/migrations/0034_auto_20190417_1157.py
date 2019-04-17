# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 14:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0033_auto_20190415_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaBrancaVotacao',
            fields=[
                ('ip', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='IP')),
                ('data_hora', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data/Hora')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Lista Branca para Votação',
                'ordering': ('ip',),
                'verbose_name': 'Lista Branca para Votação',
            },
        )
    ]