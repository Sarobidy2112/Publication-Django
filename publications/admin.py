from django.contrib import admin
from .models import Publication, Commentaire, Like

admin.site.register(Publication)
admin.site.register(Commentaire)
admin.site.register(Like)