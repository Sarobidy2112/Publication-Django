from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import generer_facture_pdf

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produit_id>/', views.detail, name='detail'),
    path('checkout', views.checkout, name='checkout'),
    path('factures/', views.mes_factures, name='mes_factures'),
    path('factures/<int:commande_id>/', views.facture_detail, name='facture_detail'),
    path('factures/<int:commande_id>/pdf/', generer_facture_pdf, name='generer_facture_pdf'),
    path('factures/<int:commande_id>/annuler/', views.annuler_commande, name='annuler_commande'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
