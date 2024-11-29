from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Commande, CommandeItem, Category
from django.db.models import F, Sum
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
import os


# Vue pour la page d'accueil
def index(request):
    produits = Product.objects.all()
    categories = Category.objects.all()  # Récupérer toutes les catégories
    selected_category = request.GET.get('category')  # Récupérer la catégorie sélectionnée
    search_itemName = request.GET.get('search-item-name')
    message = ""

    # Filtrer par catégorie si une catégorie est sélectionnée
    if selected_category:
        produits = produits.filter(category_id=selected_category)

    # Filtrer par recherche de nom si un terme est saisi
    if search_itemName:
        produits = produits.filter(title__icontains=search_itemName)
        if not produits:
            message = "Aucun résultat trouvé."

    return render(request, 'shop/index.html', {
        'produits': produits,
        'categories': categories,
        'selected_category': selected_category,
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

@login_required
def mes_factures(request):
    # Récupérer les commandes non payées de l'utilisateur connecté
    commandes_non_payees = Commande.objects.filter(user=request.user, is_paid=False)
    commandes_payees = Commande.objects.filter(user=request.user, is_paid=True)

    return render(request, 'shop/factures.html', {
        'commandes_non_payees': commandes_non_payees,
        'commandes_payees': commandes_payees,
    })


@login_required
def facture_detail(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id, user=request.user, is_paid=False)

    # Calcul des totaux pour chaque produit et total général
    items_with_total = commande.items.annotate(
        total_price=F('quantity') * F('product__price')
    )
    total_general = items_with_total.aggregate(Sum('total_price'))['total_price__sum']

    if request.method == "POST":
        commande.is_paid = True
        commande.save()
        return redirect('mes_factures')

    return render(request, 'shop/facture_detail.html', {
        'commande': commande,
        'items_with_total': items_with_total,
        'total_general': total_general,
    })


def generer_facture_pdf(request, commande_id):
    # Récupérer la commande et ses articles
    commande = get_object_or_404(Commande, id=commande_id)
    items = commande.items.all()  # Utilisation de 'items' pour accéder aux articles de la commande
    total_general = sum(item.quantity * item.product.price for item in items)

    # Préparer les données pour le template
    context = {
        "commande": commande,
        "items_with_total": [
            {
                "product": item.product,
                "quantity": item.quantity,
                "total_price": item.quantity * item.product.price,
            }
            for item in items
        ],
        "total_general": total_general,
    }

    # Rendre le template HTML
    html_string = render_to_string("shop/facture_pdf.html", context)

    # Convertir le HTML en PDF
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()

    # Créer la réponse HTTP avec le fichier PDF
    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="facture_{commande.id}.pdf"'

    return response

@login_required
def annuler_commande(request, commande_id):
    # Récupérer la commande
    commande = get_object_or_404(Commande, id=commande_id, user=request.user)

    # Vérifier si la commande est non payée
    if commande.is_paid:
        # Si la commande est déjà payée, on redirige ou on affiche un message d'erreur
        return redirect('mes_factures')  # Redirige vers la liste des factures

    # Si la commande n'est pas payée, on peut la supprimer
    commande.delete()

    # Rediriger vers la page des factures
    return redirect('mes_factures')