# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class capitulo(models.Model):
    orden=models.PositiveIntegerField()
    ruta_contenido=models.CharField(max_length=200)

class colorProgreso(models.Model):
    progreso=models.PositiveIntegerField(primary_key=True)
    color = models.CharField()

class ProgresoCapitulo(models.Model):
    id_usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    id_capitulo=models.ForeignKey(capitulo, on_delete=models.CASCADE)
    progreso=models.ForeignKey(colorProgreso, on_delete=models.CASCADE)

    class Meta: 
        unique_together =("id_usuario", "id_capitulo")

class modulo(models.Model):
    id_capitulo=models.ForeignKey(capitulo, on_delete=models.CASCADE)
    orden=models.PositiveIntegerField()
    ruta_modulo=models.CharField(max_length=200)

class resulatadoPrueba(models.Model):
    id_usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    id_modulo=models.ForeignKey(modulo, on_delete=models.CASCADE)
    resultado=models.PositiveIntegerField()

    class Meta:
        unique_together = ("id_usuario", "id_modulo")


