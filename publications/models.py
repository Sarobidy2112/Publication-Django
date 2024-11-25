from django.db import models
from django.contrib.auth.models import User

class Publication(models.Model):
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='publications/', null=True, blank=True)

    def nombre_likes(self):
        return self.like_set.count()

    def nombre_commentaires(self):
        return self.commentaire_set.count()
    
    def __str__(self):
        return f"Publication par {self.auteur.username} ({self.date_pub})"

class Commentaire(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('publication', 'utilisateur')
