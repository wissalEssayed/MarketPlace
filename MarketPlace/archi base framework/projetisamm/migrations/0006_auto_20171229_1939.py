# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetisamm', '0005_auto_20171229_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boutique',
            name='Adresse_boutique',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
