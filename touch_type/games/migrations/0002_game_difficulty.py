# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='difficulty',
            field=models.CharField(choices=[('SMP', 'Simple'), ('ESY', 'Easy'), ('MDM', 'Medium'), ('HRD', 'Hard'), ('EXE', 'Extreme')], default='SMP', max_length=7),
        ),
    ]