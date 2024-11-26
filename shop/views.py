from django.shortcuts import render
from .models import Product


def index(request):
    produits = Product.objects.all()
    search_itemName = request.GET.get('search-item-name')
    message = ""

    if search_itemName != '' and search_itemName is not None:
        produits = Product.objects.filter(title__icontains=search_itemName)

        if not produits:
            message = "Aucun resultat"

    return render(request, 'shop/index.html', {
        'produits': produits,
        'message' : message
    })


def detail(request, produit_id):
    produit = Product.objects.get(id=produit_id)

    return render(request, 'shop/detail.html', {
        'produit': produit
    })