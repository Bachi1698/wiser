from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    telephone = models.IntegerField()
    logo = models.ImageField("images/SiteInfo")
    slogan = models.CharField(max_length=255)
    couriel = models.URLField()
    adresse = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "site info"
        verbose_name_plural = "sites infos"
    
    def __str__(self):
        return self.couriel
    
class Presentation(models.Model):
    video = models.URLField()
    titre = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "titre"
        verbose_name_plural = "titres"
    
    def __str__(self):
        return self.titre

class SocialCount(models.Model):
    ICONES = [
        ('facebook','fa-facebook-f'),
        ('instagram','fa-instagram'),
        ('google-plus','fa-google-plus-g'),
        ('linkedin','fa-linkedin-in'),
        
    ] 
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icone = models.CharField(choices=ICONES,max_length=20)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "social count"
        verbose_name_plural = "socials counts"

    def __str__(self):
        return self.nom











