from django.contrib import admin

from .models import Cliente, Categoria


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("rut", "nombre", "telefono", "categoria")
    search_fields = ("rut", "nombre")
    list_filter = ("categoria",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
