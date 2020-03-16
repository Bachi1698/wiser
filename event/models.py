from django.db import models

# Create your models here.
class Evenement(models.Model):
    date = models.DateTimeField()
    heure = models.TimeField()
    lieu = models.CharField(max_length=255)
    image = models.ImageField("images/Evenement")
    description = models.TextField(max_length=255)
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

     class Meta:
        verbose_name = 'evenement'
        verbose_name_plural = 'evenements'
    
    def __str__(self):
        return self.nom

class Demande(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.URLField()
    motivation = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

     class Meta:
        verbose_name = 'demande'
        verbose_name_plural = 'demandes'
    
    def __str__(self):
        return self.nom


