# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-24 13:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', models.CharField(choices=[('united kingdom', 'UNITED KINGDOM'), ('united states', 'UNITED STATES'), ('ireland', 'IRELAND'), ('france', 'FRANCE'), ('austrailia', 'AUSTRAILIA')], max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]