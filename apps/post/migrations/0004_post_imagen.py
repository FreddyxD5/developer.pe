# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-04 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]