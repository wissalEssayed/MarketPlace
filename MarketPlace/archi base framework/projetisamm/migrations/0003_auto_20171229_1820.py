# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetisamm', '0002_commentaire_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Description_Article',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
