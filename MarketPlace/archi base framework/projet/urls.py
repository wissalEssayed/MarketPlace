"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



admin.autodiscover()
#import permission; permission.autodiscover()

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        #'document_root': settings.MEDIA_ROOT}))
        
urlpatterns = [
url(r'^loginP/', 'projetisamm.views.loginP',name='loginP'),
url(r'^deconnexion/', 'projetisamm.views.deconnexion',name='deconnexion'),
url(r'^messageR/', 'projetisamm.views.messageR',name='messageR'),
url(r'^messageRv/', 'projetisamm.views.messageRv',name='messageRv'),
url(r'^achat/', 'projetisamm.views.achat',name='achat'),
url(r'^ArticleSelonLieu/(?P<f>\w+)$', 'projetisamm.views.ArticleSelonLieu',name='ArticleSelonLieu'),
url(r'^messageConf/(?P<g>\w+)$', 'projetisamm.views.messageConf',name='messageConf'),
url(r'^messageConfv/(?P<g>\w+)$', 'projetisamm.views.messageConfv',name='messageConfv'),
url(r'^ArticlePrix1/', 'projetisamm.views.ArticlePrix1',name='ArticlePrix1'),
url(r'^ArticlePrix2/', 'projetisamm.views.ArticlePrix2',name='ArticlePrix2'),
url(r'^ArticlePrix3/', 'projetisamm.views.ArticlePrix3',name='ArticlePrix3'),
url(r'^RechAv/', 'projetisamm.views.RechAv',name='RechAv'),
url(r'^ModifProfileAcheteur/', 'projetisamm.views.ModifProfileAcheteur',name='ModifProfileAcheteur'),
url(r'^ListeArticle/', 'projetisamm.views.ListeArticle',name='ListeArticle'),
url(r'^ListeMessage/', 'projetisamm.views.ListeMessage',name='ListeMessage'),
url(r'^ListeMessageV/', 'projetisamm.views.ListeMessageV',name='ListeMessageV'),
url(r'^panier/', 'projetisamm.views.panier',name='panier'),
url(r'^deletePanier/', 'projetisamm.views.deletePanier',name='deletePanier'),
url(r'^ListePanier/', 'projetisamm.views.ListePanier',name='ListePanier'),
url(r'^RechercheArticle/', 'projetisamm.views.RechercheArticle',name='RechercheArticle'),
url(r'^inscription/', 'projetisamm.views.inscription',name='inscription'),
url(r'^message/', 'projetisamm.views.message',name='message'),
url(r'^messageV/', 'projetisamm.views.messageV',name='messageV'),
url(r'^indexA/', 'projetisamm.views.indexA',name='indexA'),
url(r'^indexV/', 'projetisamm.views.indexV',name='indexV'),
url(r'^categorieBoutique/(?P<categorie>\w+)$', 'projetisamm.views.categorieBoutique',name='categorieBoutique'),
url(r'^categorieBoutique/', 'projetisamm.views.categorieBoutique',name='categorieBoutique'),
url(r'^categorieArticle/(?P<categorieA>\w+)$', 'projetisamm.views.categorieArticle',name='categorieArticle'),
url(r'^categorieArticle/', 'projetisamm.views.categorieArticle',name='categorieArticle'),
url(r'^create_product/', 'projetisamm.views.create_product',name='create_product'),
url(r'^AddProduct/', 'projetisamm.views.AddProduct',name='AddProduct'),
url(r'^AllProductV/', 'projetisamm.views.AllProductV',name='AllProductV'),
url(r'^detailProduct/(?P<idarticle>\w+)$', 'projetisamm.views.detailProduct',name='detailProduct'),
url(r'^detailProduct/', 'projetisamm.views.detailProduct',name='detailProduct'),
url(r'^detailProductAcheteur/(?P<idarticle>\w+)$', 'projetisamm.views.detailProductAcheteur',name='detailProductAcheteur'),
url(r'^detailProductAcheteur/', 'projetisamm.views.detailProductAcheteur',name='detailProductAcheteur'),
url(r'^favoriteProduct/(?P<idarticle>\w+)$', 'projetisamm.views.favoriteProduct',name='favoriteProduct'),
url(r'^favoriteProduct/', 'projetisamm.views.favoriteProduct',name='favoriteProduct'),
url(r'^deleteProduct/(?P<idarticle>\w+)$', 'projetisamm.views.deleteProduct',name='deleteProduct'),
url(r'^deleteProduct/', 'projetisamm.views.deleteProduct',name='deleteProduct'),
url(r'^update_product/', 'projetisamm.views.update_product',name='update_product'),
url(r'^ListeFavoriteProduct/', 'projetisamm.views.ListeFavoriteProduct',name='ListeFavoriteProduct'),
url(r'^ListeBoutique/', 'projetisamm.views.ListeBoutique',name='ListeBoutique'),
url(r'^detailBoutique/', 'projetisamm.views.detailBoutique',name='detailBoutique'),
url(r'^create_store/', 'projetisamm.views.create_store',name='create_store'),
url(r'^rating/', 'projetisamm.views.rating',name='rating'),
url(r'^addpanier/', 'projetisamm.views.addpanier',name='addpanier'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


