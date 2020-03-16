from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Categoriecours)
admin.site.register(models.Cours)
admin.site.register(models.Commentaire)
admin.site.register(models.Tag)

