from django.db import models
from django.core.exceptions import ValidationError


class Cabana(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    capacidad = models.PositiveIntegerField("Capacidad")
    precio_noche = models.DecimalField("Precio por noche", max_digits=10, decimal_places=2)
    disponible = models.BooleanField("Disponible", default=True)
    foto = models.ImageField("Foto", upload_to="cabanas/photos/", blank=True, null=True)

    class Meta:
        verbose_name = "Cabana"
        verbose_name_plural = "Cabañas"

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    cabana = models.ForeignKey(
        "Cabana",
        on_delete=models.CASCADE,
        related_name="reservas",
    )
    cliente = models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.CASCADE,
        related_name="reservas",
    )
    fecha_entrada = models.DateField("Fecha de entrada")
    fecha_salida = models.DateField("Fecha de salida")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reserva {self.pk} - {self.cabana}"

    def clean(self):
        if self.fecha_salida <= self.fecha_entrada:
            raise ValidationError("La fecha de salida debe ser posterior a la fecha de entrada")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
