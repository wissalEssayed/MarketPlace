# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetisamm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('idcommentaire', models.AutoField(serialize=False, primary_key=True)),
                ('commentaire', models.CharField(max_length=50, null=True, blank=True)),
                ('idarticle', models.ForeignKey(to='projetisamm.Article')),
                ('idpersonne', models.ForeignKey(to='projetisamm.Personne')),
            ],
            options={
                'ordering': ['idcommentaire'],
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('idevaluation', models.AutoField(serialize=False, primary_key=True)),
                ('note', models.CharField(max_length=50, null=True, blank=True)),
                ('idarticle', models.ForeignKey(to='projetisamm.Article')),
                ('idpersonne', models.ForeignKey(to='projetisamm.Personne')),
            ],
            options={
                'ordering': ['idevaluation'],
                'verbose_name': 'Evaluation',
                'verbose_name_plural': 'Evaluations',
            },
        ),
    ]
