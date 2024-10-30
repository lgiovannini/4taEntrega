from django.db import models

class Ropa(models.Model):
    tipo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    fecha = models.DateField(null=True)
    descripcion = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return f'{self.tipo} - {self.marca}'