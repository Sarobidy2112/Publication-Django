from django.shortcuts import render, get_object_or_404, redirect
from .models import Publication, Commentaire, Like
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import PublicationForm


def liste_publications(request):
    # Récupération de toutes les publications avec des optimisations de requêtes
    publications_list = Publication.objects.all().select_related('auteur').prefetch_related('commentaire_set', 'like_set').order_by('-date_pub')
    
    # Pagination : 5 publications par page
    paginator = Paginator(publications_list, 5)
    page_number = request.GET.get('page')
    publications = paginator.get_page(page_number)

    # Ajouter une propriété 'liked_by_user' pour chaque publication
    if request.user.is_authenticated:
        for publication in publications:
            publication.liked_by_user = publication.like_set.filter(utilisateur=request.user).exists()

    return render(request, 'publications/liste_publications.html', {'publications': publications})


@login_required
def commenter_publication(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == "POST":
        contenu = request.POST.get('contenu')
        if contenu.strip():  # Vérifie que le contenu n'est pas vide
            Commentaire.objects.create(publication=publication, auteur=request.user, contenu=contenu)
    return redirect('liste_publications')


@login_required
def aimer_publication(request, id):
    publication = get_object_or_404(Publication, id=id)
    like, created = Like.objects.get_or_create(publication=publication, utilisateur=request.user)
    if not created:
        like.delete()  # Si le like existe déjà, on le supprime
    # Redirection vers la liste des publications ou vers l'URL précédente
    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'liste_publications'))
    return redirect(next_url)


@login_required
def ajouter_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)  # Inclure les fichiers pour gérer les images
        if form.is_valid():
            publication = form.save(commit=False)
            publication.auteur = request.user  # Associe la publication à l'utilisateur connecté
            publication.save()
            return redirect('liste_publications')  # Redirige vers la liste des publications
    else:
        form = PublicationForm()
    return render(request, 'publications/ajouter_publication.html', {'form': form})
