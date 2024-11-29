from django.shortcuts import render, get_object_or_404
from .models import Formation

def liste_formations(request):
    # Récupérer le paramètre de filtre depuis la requête GET
    type_filtre = request.GET.get('type', None)
    if type_filtre in ['PDF', 'VIDEO']:
        formations = Formation.objects.filter(type=type_filtre)
    else:
        formations = Formation.objects.all()
    
    return render(request, 'formations/liste_formations.html', {
        'formations': formations,
        'type_filtre': type_filtre,  # Passer le filtre actuel pour le rendre actif dans le front-end
    })


def formation_detail(request, formation_id):
    # On récupère la formation en fonction de son ID
    formation = get_object_or_404(Formation, pk=formation_id)
    return render(request, 'formations/formation_detail.html', {'formation': formation})