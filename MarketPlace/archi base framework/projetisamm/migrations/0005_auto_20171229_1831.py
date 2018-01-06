# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetisamm', '0004_auto_20171229_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Description_Article',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='Nom_article',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='prix',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
