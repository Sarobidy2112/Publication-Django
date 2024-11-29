# home/views.py
from django.shortcuts import render

def home(request):
    context = {}
    if request.user.is_authenticated:
        # Si l'utilisateur est connecté, on affiche son nom et un bouton de déconnexion
        context['user'] = request.user
    return render(request, 'home/home.html', context)

from django.shortcuts import render

def gestion_utilisateurs(request):
    return render(request, 'gestion_utilisateurs.html')

from django.shortcuts import render

def profil(request):
    # Logique pour récupérer les données du profil de l'utilisateur
    return render(request, 'profil.html')
