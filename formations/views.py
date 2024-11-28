from django.shortcuts import render, get_object_or_404
from .models import Formation

def liste_formations(request):
    formations = Formation.objects.all()
    return render(request, 'formations/liste_formations.html', {'formations': formations})

def formation_detail(request, formation_id):
    # On récupère la formation en fonction de son ID
    formation = get_object_or_404(Formation, pk=formation_id)
    return render(request, 'formations/formation_detail.html', {'formation': formation})