from django.contrib import admin

from .models import Cabana, Reserva


@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "precio_noche", "disponible", "foto")
    list_filter = ("disponible",)
    search_fields = ("nombre",)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cabana", "cliente", "fecha_entrada", "fecha_salida")
    list_filter = ("cabana", "fecha_entrada")
    search_fields = ("cabana__nombre", "cliente__rut")
