# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetisamm', '0003_auto_20171229_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Description_Article',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='Nom_article',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
