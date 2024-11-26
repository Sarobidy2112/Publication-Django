# mon_projet/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Inclure l'URL de l'application 'home' pour la page d'accueil
    path('accounts/', include('accounts.urls')),  # Routes pour l'application 'accounts'
    path('publications/', include('publications.urls')),
    path('shop/', include('shop.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)