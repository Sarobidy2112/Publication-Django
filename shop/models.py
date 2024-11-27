from django.db import models
from django.contrib.auth.models import User  # Pour associer les commandes aux utilisateurs

# Modèle pour les catégories
class Category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name


# Modèle pour les produits
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="categorie", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


# Modèle pour les commandes
class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Client ayant passé la commande
    products = models.ManyToManyField(
        Product, through='CommandeItem', related_name='commandes'
    )  # Relation avec les produits via une table intermédiaire
    total_price = models.FloatField(default=0.0)  # Prix total de la commande
    date_ordered = models.DateTimeField(auto_now_add=True)  # Date de la commande
    is_paid = models.BooleanField(default=False)  # Indique si la commande est payée
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'En attente'),
            ('Processing', 'En cours de traitement'),
            ('Completed', 'Complétée'),
            ('Cancelled', 'Annulée'),
        ],
        default='Pending'
    )  # Statut de la commande

    class Meta:
        ordering = ['-date_ordered']

    def __str__(self):
        return f"Commande #{self.id} - {self.user.username if self.user else 'Anonyme'}"


# Modèle pour les articles d'une commande
class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Quantité d'un produit spécifique

    def __str__(self):
        return f"{self.product.title} (x{self.quantity})"
