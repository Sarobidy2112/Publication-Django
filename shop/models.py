from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name

    
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category,related_name="categorie", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title