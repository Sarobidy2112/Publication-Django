# home/views.py
from django.shortcuts import render

def home(request):
    context = {}
    if request.user.is_authenticated:
        # Si l'utilisateur est connecté, on affiche son nom et un bouton de déconnexion
        context['user'] = request.user
    return render(request, 'home/home.html', context)
