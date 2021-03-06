from abc import abstractclassmethod
from dataclasses import field, fields
from tabnanny import verbose
from django.db import models
from .managers import AutorManager

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellido', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50)
    edad = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre + ' ' + self.apellidos


class Autor(Persona):

    seudonimo = models.CharField('Seudonimo', max_length=50, blank=True)
    objects = AutorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
