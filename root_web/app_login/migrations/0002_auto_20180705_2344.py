# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-05 23:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfoli_site',
            new_name='portfolio_site',
        ),
    ]
