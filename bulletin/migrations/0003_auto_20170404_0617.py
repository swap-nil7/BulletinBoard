# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 00:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0002_auto_20170402_0349'),
    ]

    operations = [
        migrations.CreateModel(
            name='CNlink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin.Category')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin.Notice')),
            ],
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='sus_since',
            new_name='subs_since',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='suscribed',
        ),
    ]
