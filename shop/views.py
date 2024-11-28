from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Commande, CommandeItem

# Vue pour la page d'accueil
def index(request):
    produits = Product.objects.all()
    search_itemName = request.GET.get('search-item-name')
    message = ""

    if search_itemName:
        produits = Product.objects.filter(title__icontains=search_itemName)
        if not produits:
            message = "Aucun résultat trouvé."

    return render(request, 'shop/index.html', {
        'produits': produits,
        'message': message,
    })

# Vue pour afficher les détails d'un produit
def detail(request, produit_id):
    produit = get_object_or_404(Product, id=produit_id)
    return render(request, 'shop/detail.html', {
        'produit': produit,
    })

# Vue pour le checkout (finalisation de la commande)
@login_required
def checkout(request):
    commande = []
    if request.method == "POST":
        user = request.user
        panier = request.POST.get('panier', None)  # Le panier transmis via POST
        if panier:
            panier_data = eval(panier)  # Convertir la chaîne JSON en dictionnaire Python
            commande = Commande.objects.create(user=user)  # Créer une nouvelle commande

            for produit_id, item in panier_data.items():
                produit = get_object_or_404(Product, id=produit_id)
                CommandeItem.objects.create(
                    commande=commande,
                    product=produit,
                    quantity=item[0]
                )

            # Calculer le total de la commande
            commande.total_price = sum(
                item.product.price * item.quantity for item in commande.items.all()
            )
            commande.save()

            return redirect('index')

    return render(request, 'shop/checkout.html', {
        'commande' : commande
    })
