from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre =models.CharField(max_length=50)
    nacionalidad =models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Autor"
