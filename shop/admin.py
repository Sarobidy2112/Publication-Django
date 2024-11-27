from django.contrib import admin
from .models import Category, Product, Commande, CommandeItem

class AdminCategory(admin.ModelAdmin):
    list_display = ("name", "date_added")

class AdminProduct(admin.ModelAdmin):
    list_display = ("title", "price", "category", "date_added")

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Commande)
admin.site.register(CommandeItem)

# admin.site.register(Commande, AdminCommande)
# admin.site.register(CommandeItem, AdminCommandeItem)

