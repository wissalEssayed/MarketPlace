from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.utils.html import strip_tags
from .models import Article, Boutique
from django.utils import timezone
from django.forms import ModelForm
import sys
import random 
from django.conf import settings
import os

class ArticleForm(forms.Form):
   Nom_article= forms.CharField(max_length=500)
   avatar= forms.FileField()
   categorie = forms.CharField(max_length=500)
   prix = forms.CharField(max_length=500)
   Description_Article = forms.CharField(max_length=500)

class BoutiqueForm(forms.Form):
   Nom_boutique= forms.CharField(max_length=15)
   avatrB= forms.FileField()
   Adresse_boutique = forms.CharField(max_length=100)
   telephone = forms.CharField(max_length=50)