from django.contrib import admin
from .models import Publication, Commentaire, Like

class AdminCommentaire(admin.ModelAdmin):
    list_display = ("auteur", "publication")

class AdminPublication(admin.ModelAdmin):
    list_display = ("auteur", "contenu")

admin.site.register(Publication, AdminPublication)
admin.site.register(Commentaire, AdminCommentaire)
admin.site.register(Like)