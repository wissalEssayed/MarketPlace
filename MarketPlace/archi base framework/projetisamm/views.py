from django.shortcuts import render,redirect,HttpResponse,render_to_response
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from django.contrib.auth import login, authenticate, logout
from .models import Personne,User,Message,Article,Panier, Boutique, Favoris, Evaluation
import smtplib
import random 
from datetime import datetime
from django.views.generic import *
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models.signals import post_save
from .forms import ArticleForm , BoutiqueForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def loginP(request):
	article=Article.objects.all()
	if request.method == 'POST':
	    msgAuth="Verifier Votre identifiant et mot de passe"
	    nom = request.POST.get('nom')
	    password = request.POST.get('password')
	    user = authenticate(username=nom, password=password)
	    

	    if user is not None and user.is_active :
	    	
	        login(request, user)
	        pers =Personne.objects.get(user=request.user).role

	    	if pers == "acheteur":
	    		
	        	return render(request,'opac/indexA.html')
	        else:
				u=User.objects.get(username=request.user.username,password=request.user.password)
				personne=Personne.objects.get(user=u).idpersonne
				t=Boutique.objects.filter(idpersonne=personne).count()
				if t == 0:
					return render(request,'opac/AjouterBoutique.html')
				else:
					return indexV(request)	        	
	 	
	    return render(request,'opac/index.html',{'msgAuth': msgAuth,'article': article})
	else:
		return render(request,'opac/index.html',{'msgAuth':'','article': article})
def deconnexion(request):
	logout(request)
	return render(request,'opac/index.html')
def inscription(request):

    nom = request.POST.get("nom")
    prenom = request.POST.get("prenom")
    email = request.POST.get("email")
    password = request.POST.get("password")
    adresse = request.POST.get("adresse")
    role = request.POST.get("role")

    d="Utilisateur existe deja"
    if request.method == 'POST': 
        z=User.objects.all()
        for f in z:
            if nom == f.username:
                return render(request,'opac/index.html',{'etat':d})
        
        #u=User.objects.create(username=nom,password=password)
        user, created = User.objects.get_or_create(username=nom)
        user.set_password(password)
        user.save()

        Personne.objects.create(nom=nom,prenom=prenom,email=email,password=password,adresse=adresse,role=role,user=user)
        return render(request, 'opac/index.html')
   
    return render(request,'opac/index.html',{'etat':''}) 
	  	

def indexA(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u).role	  
	article=Article.objects.all()
	out=categorieFiltre(request)
	return render(request,'opac/indexA.html',{'article':article , 'out':out})


def ModifProfileAcheteur(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')

	if request.method == 'POST':

		nom = request.POST.get("nom")
		prenom = request.POST.get("prenom")
		email = request.POST.get("email")
		password = request.POST.get("password")
		adresse = request.POST.get("adresse")
		u=User.objects.get(username=request.user.username,password=request.user.password)
		personne=Personne.objects.get(user=u)
		Personne.objects.filter(idpersonne=personne.idpersonne).update(nom =nom,prenom=prenom,email=email,password=password,adresse=adresse)
		article=Article.objects.all()
		return render(request,'opac/indexA.html',{'article':article})

	return render(request,'opac/indexA.html')
	    
	    

def message(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	msg="votre message a ete envoye"

	if request.method == 'POST' and request.POST.get("destinataire")!='':

		destinataire = request.POST.get("destinataire")
		objet = request.POST.get("objet")
		message = request.POST.get("message")
		u=User.objects.get(username=request.user.username,password=request.user.password)
		personne=Personne.objects.get(user=u)
		Message.objects.create(destination=destinataire,objet=objet,message=message,emetteur=personne)
		return render(request,'opac/message.html',{'msg':msg})
		
	return render(request,'opac/message.html')

def messageV(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	msg="votre message a ete envoye"

	if request.method == 'POST' and request.POST.get("destinataire")!='':

		destinataire = request.POST.get("destinataire")
		objet = request.POST.get("objet")
		message = request.POST.get("message")
		out= categorieFiltreBoutique(request,article)
		u=User.objects.get(username=request.user.username,password=request.user.password)
		Message.objects.create(destination=destinataire,objet=objet,message=message,emetteur=personne)
		return render(request,'opac/messageV.html',{'msg':msg})
		
	return render(request,'opac/messageV.html')
def ListeMessageV(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u).email
	pers=Message.objects.filter(destination=personne)
	return render(request,'opac/ListeMessageV.html',{'pers':pers})

def messageR(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	if request.method == 'POST':
		dest = request.POST.get("destination")
		return render(request,'opac/message.html',{'dest':dest})
def messageRv(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	if request.method == 'POST':
		dest = request.POST.get("destination")
		return render(request,'opac/messageV.html',{'dest':dest})
def messageConf(request,g):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	email=Personne.objects.get(idpersonne=g).email
	dest = email
	return render(request,'opac/message.html',{'dest':dest})
def messageConfv(request,g):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	email=Personne.objects.get(idpersonne=g).email
	dest = email
	return render(request,'opac/messageV.html',{'dest':dest})
def	ArticlePrix1(request):
	lieu=lieuFiltre(request)
	boutique=Boutique.objects.all()
	article=Article.objects.filter(prix__in=range(0,101))
	return render(request,'opac/RechAv.html',{'boutique':boutique,'article':article,'lieu':lieu})

def	ArticlePrix2(request):
	lieu=lieuFiltre(request)
	boutique=Boutique.objects.all()
	article=Article.objects.filter(prix__in=range(101,500))
	return render(request,'opac/RechAv.html',{'boutique':boutique,'article':article,'lieu':lieu})
def	ArticlePrix3(request):
	lieu=lieuFiltre(request)
	boutique=Boutique.objects.all()
	article=Article.objects.filter(prix__in=range(500,6000))
	return render(request,'opac/RechAv.html',{'boutique':boutique,'article':article,'lieu':lieu})
def lieuFiltre(request):
	listes = []
	output = []
	seen = set()
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	boutique=Boutique.objects.all()
	listes[:] = []
	output[:] = []
	for f in boutique:
		h=len(listes)+1
		listes.insert(h,f.Adresse_boutique)

	for value in listes:
		if value not in seen:
			output.insert(len(output)+1,value)
			seen.add(value)
	#return render(request,'opac/AllProductByCategoryAcheteur.html',{'categorie':categorie , 'articleC':articleC , 'article':article})		  
	return output

	#return render(request,'opac/AllProductByCategoryAcheteur.html',{'categorie':categorie , 'articleC':articleC , 'article':article})		  
	return output
def ArticleSelonLieu(request,f):

	lieu=lieuFiltre(request)
	lieub = f
	boutique=Boutique.objects.filter(Adresse_boutique=lieub)
	article=Article.objects.filter(idboutique=boutique)
	return render(request,'opac/RechAv.html',{'article':article,'lieu':lieu})

def achat(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u)
	boutique=Boutique.objects.filter(idpersonne=personne)
	article=Article.objects.filter(idboutique=boutique)
	panier=Panier.objects.filter(idarticle=article)
	return render(request,'opac/achat.html',{'panier':panier})

def RechAv(request):
	article=Article.objects.all()
	lieu=lieuFiltre(request)
	return render(request,'opac/RechAv.html',{'article':article,'lieu':lieu})


def indexV(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u)
	idP=Personne.objects.get(user=u).idpersonne
	boutique=Boutique.objects.filter(idpersonne=idP)
	article=Article.objects.filter(idboutique=boutique)
	out= categorieFiltreBoutique(request,article)
	return render(request,'opac/indexV.html',{'boutique': boutique, 'article':article , 'out':out})

def create_store(request):
    if not request.user.is_authenticated():
        return render(request, 'opac/index.html')
    else:
        form = BoutiqueForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            boutique = Boutique()
            u=User.objects.get(username=request.user.username,password=request.user.password)
            idP=Personne.objects.get(user=u).idpersonne
            boutique.Nom_boutique = form.cleaned_data["Nom_boutique"]
            boutique.telephone = form.cleaned_data["telephone"]
            boutique.Adresse_boutique = form.cleaned_data["Adresse_boutique"]
            boutique.avatrB = form.cleaned_data["avatrB"]
            boutique.idpersonne=Personne.objects.get(user=u)
            boutique.save()
            return render(request,'opac/index.html')
        return render(request, 'opac/AjouterBoutique.html')     

def create_product(request):
    if not request.user.is_authenticated():
        return render(request, 'opac/index.html')
    else:
        form = ArticleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            article = Article()
            u=User.objects.get(username=request.user.username,password=request.user.password)
            idP=Personne.objects.get(user=u).idpersonne
            boutique=Boutique.objects.filter(idpersonne=idP)
            article.Nom_article = form.cleaned_data["Nom_article"]
            article.Description_Article = form.cleaned_data["Description_Article"]
            article.categorie = form.cleaned_data["categorie"]
            article.prix = form.cleaned_data["prix"]
            article.avatar = form.cleaned_data["avatar"]
            for f in boutique:
            	article.idboutique = f
            article.save()
            return AllProductV(request)
        return render(request, 'opac/AjouterProduit.html')

def AddProduct(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	idP=Personne.objects.get(user=u).idpersonne
	boutique=Boutique.objects.filter(idpersonne=idP)
	article=Article.objects.filter(idboutique=boutique)
	out= categorieFiltreBoutique(request,article)
	return render(request,'opac/AjouterProduit.html',{'out':out})

def AllProductV(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	idP=Personne.objects.get(user=u).idpersonne
	boutique=Boutique.objects.filter(idpersonne=idP)
	article=Article.objects.filter(idboutique=boutique)
	out= categorieFiltreBoutique(request,article)
	return render(request,'opac/AllProductV.html',{'out':out , 'article':article})

def categorieBoutique(request, categorie):

	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	categorie = categorie
	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u)
	idP=Personne.objects.get(user=u).idpersonne
	boutique=Boutique.objects.filter(idpersonne=idP)
	article=Article.objects.filter(idboutique=boutique)
	out= categorieFiltreBoutique(request,article)
	articleC=Article.objects.filter(idboutique=boutique , categorie=categorie)
	return render(request,'opac/AllProductByCategory.html',{'categorie':categorie , 'articleC':articleC , 'out':out})		  

def categorieArticle(request, categorieA):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	categorie = categorieA
	article=Article.objects.all()
	articleC=Article.objects.filter(categorie=categorie)
	out=categorieFiltre(request)
	return render(request,'opac/AllProductByCategoryAcheteur.html',{'categorie':categorie , 'articleC':articleC , 'article':article , 'out':out})		  

def categorieFiltre(request):
	listes = []
	output = []
	seen = set()
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	article=Article.objects.all()
	listes[:] = []
	output[:] = []
	for f in article:
		h=len(listes)+1
		listes.insert(h,f.categorie)

	for value in listes:
		if value not in seen:
			output.insert(len(output)+1,value)
			seen.add(value)
	#return render(request,'opac/AllProductByCategoryAcheteur.html',{'categorie':categorie , 'articleC':articleC , 'article':article})		  
	return output

def categorieFiltreBoutique(request,articleB):
	listes = []
	output = []
	seen = set()
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	article=articleB
	listes[:] = []
	output[:] = []
	for f in article:
		h=len(listes)+1
		listes.insert(h,f.categorie)

	for value in listes:
		if value not in seen:
			output.insert(len(output)+1,value)
			seen.add(value)
	#return render(request,'opac/AllProductByCategoryAcheteur.html',{'categorie':categorie , 'articleC':articleC , 'article':article})		  
	return output
def detailProduct(request, idarticle):
	notep=0
	nbrtt=0	
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	idarticle = idarticle
	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u)
	idP=Personne.objects.get(user=u).idpersonne
	boutique=Boutique.objects.filter(idpersonne=idP)
	article=Article.objects.filter(idboutique=boutique)
	out= categorieFiltreBoutique(request,article)
	detail=Article.objects.filter(idarticle=idarticle)

	##################### rating people##########################

	toutesp=Evaluation.objects.filter(idarticle=idarticle)
	nbrtt=len(toutesp)
	for k in toutesp:
		notep=(notep+int(k.note))
	if notep != 0:
		notep=notep/int(nbrtt)
	############################################################	
	return render(request,'opac/detailProduct.html',{'detail':detail , 'out':out , 'notep':notep , 'nbrtt':nbrtt})

def detailProductAcheteur(request, idarticle):
	notep=0
	nbrtt=0
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')

	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u)
	idP=Personne.objects.get(user=u).idpersonne	
	idarticle = idarticle
	art=Article.objects.get(idarticle=idarticle)
	detail=Article.objects.filter(idarticle=idarticle)

	if request.method == 'POST':
		rate = request.POST['your_awesome_parameter']
		Evaluation.objects.create(idarticle=art , idpersonne=personne , note=rate)
	##################### rating people##########################

	toutesp=Evaluation.objects.filter(idarticle=idarticle)
	nbrtt=len(toutesp)
	for k in toutesp:
		notep=(notep+int(k.note))
	if notep != 0:
		notep=notep/int(nbrtt)
	t=Evaluation.objects.filter(idarticle=idarticle , idpersonne=personne).count()
	if t == 0:
		formDiv="visible"
		readDiv="hidden"
		note=0
	else:
		n=Evaluation.objects.get(idarticle=idarticle , idpersonne=personne).note
		note=int(n)
		formDiv="hidden"
		readDiv="visible"		

	outt=categorieFiltre(request)
	#return HttpResponse(out)
	return render(request,'opac/detailProductAcheteur.html',{'detail':detail, 'notep':notep , 'nbrtt':nbrtt, 'outt':outt , 'formDiv':formDiv , 'readDiv':readDiv, 'note':note})	  

def rating(request):

	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	if request.method == 'POST':
		rate = request.POST['your_awesome_parameter']
	return HttpResponse(rate)

def deleteProduct(request, idarticle):

	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	idarticle = idarticle
	Article.objects.filter(idarticle=idarticle).delete()
	Favoris.objects.filter(idarticle=idarticle).delete()
	Evaluation.objects.filter(idarticle=idarticle).delete()
	return AllProductV(request)

def update_product(request):

	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	if request.method == 'POST':
		idA = request.POST['idarticle']
		prix = request.POST.get("prix")
		cat = request.POST.get("categorie")
		desc = request.POST.get("Description_Article")
		nom = request.POST.get("Nom_article")
		if len(request.FILES) != 0:
			form = ArticleForm(request.POST or None, request.FILES or None)
			if form.is_valid():
				articleUP=Article.objects.get(idarticle=idA)
        		articleUP.Nom_article = form.cleaned_data["Nom_article"]
        		articleUP.Description_Article = form.cleaned_data["Description_Article"]
        		articleUP.categorie = form.cleaned_data["categorie"]
        		articleUP.prix = form.cleaned_data["prix"]
        		articleUP.avatar = form.cleaned_data["avatar"]
        		articleUP.save()
		else:
			Article.objects.filter(idarticle=idA).update(Nom_article =nom,prix=prix,categorie=cat,Description_Article=desc)	
	return AllProductV(request)

      		
def ListeMessage(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u).email
	pers=Message.objects.filter(destination=personne)
	return render(request,'opac/ListeMessage.html',{'pers':pers})

def deletePanier(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	if request.method == 'POST':
		idpanier = request.POST.get("idpanier")
		Panier.objects.filter(idpanier=idpanier).delete()
		u=User.objects.get(username=request.user.username,password=request.user.password)
		personne=Personne.objects.get(user=u).idpersonne
		pers=Panier.objects.filter(idpersonne=personne)
		return render(request,'opac/panier.html',{'pers':pers})

def favoriteProduct(request, idarticle):

	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	idarticle = idarticle
	u=User.objects.get(username=request.user.username,password=request.user.password)
	idP=Personne.objects.get(user=u).idpersonne

	personne=Personne.objects.get(user=u)
	art=Article.objects.get(idarticle=idarticle)
	test=Favoris.objects.filter(idarticle=idarticle , idpersonne=idP).count()

	if test != 0:
		msgAuth="Verifier"
	else:
		Favoris.objects.create(idarticle=art , idpersonne=personne)

	return indexA(request)

def ListeFavoriteProduct(request):

	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	idP=Personne.objects.get(user=u).idpersonne
	lst=Favoris.objects.filter(idpersonne=idP)
	out=categorieFiltre(request)
	return render(request,'opac/listeFavorite.html',{'out':out , 'lst':lst})

def ListeBoutique(request):

	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	boutique=Boutique.objects.all()
	out=categorieFiltre(request)
	return render(request,'opac/listeBoutique.html',{'out':out , 'boutique':boutique})

def detailBoutique(request):

	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	out=categorieFiltre(request)
	if request.method == 'POST':
		idboutique = request.POST.get("idboutique")
		boutique=Boutique.objects.get(idboutique=idboutique)
		boutiqueee=Boutique.objects.filter(idboutique=idboutique)
		articleB=Article.objects.filter(idboutique=boutique)
		outB=categorieFiltreBoutique(request,articleB)
	#return HttpResponse(outB)	
	return render(request,'opac/detailBoutique.html',{'out':out , 'boutique':boutiqueee ,'articleB':articleB ,'outB':outB})

def ListePanier(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	u=User.objects.get(username=request.user.username,password=request.user.password)
	personne=Personne.objects.get(user=u).idpersonne
	pers=Panier.objects.filter(idpersonne=personne)
	return render(request,'opac/panier.html',{'pers':pers})

def ListeArticle(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	article=Article.objects.all()
	return render(request,'opac/indexA.html',{'article':article})

def addpanier(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	if request.method == 'POST':
		idarticle = request.POST.get("idarticle")
		quantityID = request.POST.get("quantityID")	
	return HttpResponse(quantityID)
def panier(request):
	if not request.user.is_authenticated():
	    return render(request,'opac/index.html')
	if request.method == 'POST':
		idarticle = request.POST.get("idarticle")
		u=User.objects.get(username=request.user.username,password=request.user.password)
		personne=Personne.objects.get(user=u).idpersonne
		quantity = request.POST.get("quantityID")
		Panier.objects.create(idarticle=Article.objects.get(idarticle=idarticle),quantity=quantity,idpersonne=Personne.objects.get(idpersonne=personne))
		article=Article.objects.all()
	return render(request,'opac/indexA.html',{'article':article})

def RechercheArticle(request):

	if request.method == 'POST':

		categorie = request.POST.get("categorie")
		art=Article.objects.filter(categorie=categorie)

	return render(request,'opac/products1.html',{'article':art})