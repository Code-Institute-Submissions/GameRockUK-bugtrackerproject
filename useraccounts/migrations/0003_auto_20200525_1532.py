# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-25 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0002_auto_20200524_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='budget',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='country',
            field=models.CharField(choices=[('united kingdom', 'UNITED KINGDOM'), ('united states', 'UNITED STATES'), ('ireland', 'IRELAND'), ('france', 'FRANCE'), ('australia', 'AUSTRALIA')], max_length=40),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254),
        ),
    ]