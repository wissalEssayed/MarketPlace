# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetisamm', '0006_auto_20171229_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='panier',
            name='quantity',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
