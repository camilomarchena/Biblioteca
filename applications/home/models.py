from tabnanny import check
from django.db import models

# Create your models here.


class Persona(models.Model):
    """Model definition for Persona."""

    full_name = models.CharField('Nombre', max_length=50)
    pais = models.CharField('País', max_length=50)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=50)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together = ['pais', 'apelativo']
        constraints = [models.CheckConstraint(
            check=models.Q(edad__gte=18), name='edad_mayor_18')]
        abstract = True

    def __str__(self):
        """Unicode representation of Persona."""
        return self.full_name


class Empleados(Persona):
    empleo = models.CharField('Empleo', max_length=50)
