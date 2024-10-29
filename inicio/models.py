from django.db import models

class Ropa(models.Model):
    tipo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    talle = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.tipo} - {self.marca}'