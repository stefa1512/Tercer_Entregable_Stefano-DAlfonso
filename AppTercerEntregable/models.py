from django.db import models

# Create your models here.
class Celular(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    almacenamiento = models.IntegerField()
    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.almacenamiento}"


class Tablet(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    almacenamiento = models.IntegerField()
    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.almacenamiento}"


class Laptop(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    almacenamiento = models.IntegerField()
    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.almacenamiento}"
