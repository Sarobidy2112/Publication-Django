from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_publications, name='liste_publications'),
    path('ajouter/', views.ajouter_publication, name='ajouter_publication'),
    path('commenter/<int:id>/', views.commenter_publication, name='commenter_publication'),
    path('aimer/<int:id>/', views.aimer_publication, name='aimer_publication'),
]
