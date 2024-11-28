from django.contrib import admin
from .models import Category, Product, Commande, CommandeItem

class AdminCategory(admin.ModelAdmin):
    list_display = ("name", "date_added")

class AdminProduct(admin.ModelAdmin):
    list_display = ("title", "price", "category", "date_added")

class AdminCommande(admin.ModelAdmin):
    list_display = ("id","user", "total_price", "is_paid", "status")

class AdminCommandeItem(admin.ModelAdmin):
    list_display = ("commande_id", "product", "quantity")

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Commande, AdminCommande)
admin.site.register(CommandeItem, AdminCommandeItem)



