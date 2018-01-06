# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('idarticle', models.AutoField(serialize=False, primary_key=True)),
                ('Nom_article', models.CharField(max_length=15, null=True, blank=True)),
                ('avatar', models.FileField(upload_to=b'')),
                ('categorie', models.CharField(max_length=50, null=True, blank=True)),
                ('prix', models.CharField(max_length=50, null=True, blank=True)),
                ('Description_Article', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'ordering': ['idarticle'],
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Boutique',
            fields=[
                ('idboutique', models.AutoField(serialize=False, primary_key=True)),
                ('Nom_boutique', models.CharField(max_length=15, null=True, blank=True)),
                ('Adresse_boutique', models.CharField(max_length=50, null=True, blank=True)),
                ('telephone', models.CharField(max_length=50, null=True, blank=True)),
                ('avatrB', models.FileField(upload_to=b'')),
            ],
            options={
                'ordering': ['idboutique'],
                'verbose_name': 'Boutique',
                'verbose_name_plural': 'Boutiques',
            },
        ),
        migrations.CreateModel(
            name='Favoris',
            fields=[
                ('idfavoris', models.AutoField(serialize=False, primary_key=True)),
                ('idarticle', models.ForeignKey(to='projetisamm.Article')),
            ],
            options={
                'ordering': ['idfavoris'],
                'verbose_name': 'Favoris',
                'verbose_name_plural': 'Favoris',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=150, null=True, blank=True)),
                ('objet', models.CharField(max_length=50, null=True, blank=True)),
                ('destination', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'ordering': ['message'],
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('idpanier', models.AutoField(serialize=False, primary_key=True)),
                ('idarticle', models.ForeignKey(to='projetisamm.Article')),
            ],
            options={
                'ordering': ['idpanier'],
                'verbose_name': 'Panier',
                'verbose_name_plural': 'Paniers',
            },
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('idpersonne', models.AutoField(serialize=False, primary_key=True)),
                ('nom', models.CharField(max_length=15, null=True, blank=True)),
                ('prenom', models.CharField(max_length=50, null=True, blank=True)),
                ('password', models.CharField(max_length=50, null=True, blank=True)),
                ('adresse', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('role', models.CharField(max_length=50, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['idpersonne'],
                'verbose_name': 'Personne',
                'verbose_name_plural': 'Personnes',
            },
        ),
        migrations.AddField(
            model_name='panier',
            name='idpersonne',
            field=models.ForeignKey(to='projetisamm.Personne'),
        ),
        migrations.AddField(
            model_name='message',
            name='emetteur',
            field=models.ForeignKey(to='projetisamm.Personne'),
        ),
        migrations.AddField(
            model_name='favoris',
            name='idpersonne',
            field=models.ForeignKey(to='projetisamm.Personne'),
        ),
        migrations.AddField(
            model_name='boutique',
            name='idpersonne',
            field=models.ForeignKey(to='projetisamm.Personne'),
        ),
        migrations.AddField(
            model_name='article',
            name='idboutique',
            field=models.ForeignKey(to='projetisamm.Boutique'),
        ),
    ]
