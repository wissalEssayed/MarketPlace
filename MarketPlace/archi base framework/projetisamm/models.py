from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Personne(models.Model):
    """
    Class provides more information according the system's users
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    idpersonne = models.AutoField(primary_key=True)
    nom= models.CharField(max_length=15, null=True, blank=True)
    prenom = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    adresse = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    



    def __unicode__(self):
        return self.nom


    class Meta:
        
        ordering = ['idpersonne']
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"


class Boutique(models.Model):
    """
    Class provides more information according the system's users
    """
    idboutique = models.AutoField(primary_key=True)
    Nom_boutique= models.CharField(max_length=15, null=True, blank=True)
    Adresse_boutique = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    avatrB=models.FileField()
    idpersonne = models.ForeignKey('Personne')

    



    def __unicode__(self):
        return self.Nom_boutique


    class Meta:
        
        ordering = ['idboutique']
        verbose_name = "Boutique"
        verbose_name_plural = "Boutiques"

class Article(models.Model):
    """
    Class provides more information according the system's users
    """
    idarticle = models.AutoField(primary_key=True)
    Nom_article= models.CharField(max_length=500, null=True, blank=True)
    avatar= models.FileField()
    categorie = models.CharField(max_length=500, null=True, blank=True)
    prix = models.CharField(max_length=500, null=True, blank=True)
    Description_Article = models.CharField(max_length=500, null=True, blank=True)
    idboutique  = models.ForeignKey('Boutique')

    



    def __unicode__(self):
        return self.Nom_article


    class Meta:
        
        ordering = ['idarticle']
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Message(models.Model):

    message= models.CharField(max_length=150, null=True, blank=True)
    objet = models.CharField(max_length=50, null=True, blank=True)
    destination  = models.CharField(max_length=50, null=True, blank=True)
    emetteur  = models.ForeignKey('Personne')

    


    class Meta:
        
        ordering = ['message']
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Panier(models.Model):

    idpanier = models.AutoField(primary_key=True)
    quantity  = models.CharField(max_length=50, null=True, blank=True)
    idarticle  = models.ForeignKey('Article')
    idpersonne  = models.ForeignKey('Personne')

    

    class Meta:
        
        ordering = ['idpanier']
        verbose_name = "Panier"
        verbose_name_plural = "Paniers"


class Evaluation(models.Model):

    idevaluation = models.AutoField(primary_key=True)
    idarticle  = models.ForeignKey('Article')
    note = models.CharField(max_length=50, null=True, blank=True)
    idpersonne  = models.ForeignKey('Personne')
    

    class Meta:
        
        ordering = ['idevaluation']
        verbose_name = "Evaluation"
        verbose_name_plural = "Evaluations"

class Commentaire(models.Model):

    idcommentaire = models.AutoField(primary_key=True)
    idarticle  = models.ForeignKey('Article')
    commentaire = models.CharField(max_length=50, null=True, blank=True)
    idpersonne  = models.ForeignKey('Personne')
    

    class Meta:
        
        ordering = ['idcommentaire']
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

class Favoris(models.Model):

    idfavoris = models.AutoField(primary_key=True)
    idarticle  = models.ForeignKey('Article')
    idpersonne  = models.ForeignKey('Personne')


    class Meta:
        
        ordering = ['idfavoris']
        verbose_name = "Favoris"
        verbose_name_plural = "Favoris"