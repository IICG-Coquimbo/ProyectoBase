import re

from django.core.exceptions import ValidationError
from django.db import models


def validate_rut(value):
    pattern = r"^\d{6,7}-[0-9K]$"
    if not re.match(pattern, value.upper()):
        raise ValidationError(
            "El RUT debe tener formato: 6 o 7 dígitos seguidos de '-' y un dígito o K (ej: 1234567-9 o 1234567-K)"
        )


class Cliente(models.Model):
    rut = models.CharField(
        "RUT", max_length=10, unique=True, validators=[validate_rut]
    )
    nombre = models.CharField("Nombre", max_length=100)
    telefono = models.CharField("Teléfono", max_length=10)
    categoria = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="Categoria",
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField("Nombre", max_length=8, unique=True)
    descripcion = models.TextField("Descripción", blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre
