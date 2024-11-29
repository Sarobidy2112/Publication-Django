from django.db import models

class Formation(models.Model):
    TYPE_CHOICES = [
        ('PDF', 'Document PDF'),
        ('VIDEO', 'Vidéo'),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='formations/', blank=True, null=True)
    lien_video = models.CharField(max_length=200, null=True, blank=True)  # Rendre ce champ optionnel
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre