from django.urls import path
from .views import (
    ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    CategoriaListView, CategoriaDetailView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
)

app_name = "clientes"

urlpatterns = [
    # Clientes
    path("", ClienteListView.as_view(), name="cliente_list"),
    path("cliente/<int:pk>/", ClienteDetailView.as_view(), name="cliente_detail"),
    path("cliente/crear/", ClienteCreateView.as_view(), name="cliente_create"),
    path("cliente/editar/<int:pk>/", ClienteUpdateView.as_view(), name="cliente_update"),
    path("cliente/eliminar/<int:pk>/", ClienteDeleteView.as_view(), name="cliente_delete"),
    # Categorías
    path("categoria/", CategoriaListView.as_view(), name="categoria_list"),
    path("categoria/<int:pk>/", CategoriaDetailView.as_view(), name="categoria_detail"),
    path("categoria/crear/", CategoriaCreateView.as_view(), name="categoria_create"),
    path("categoria/editar/<int:pk>/", CategoriaUpdateView.as_view(), name="categoria_update"),
    path("categoria/eliminar/<int:pk>/", CategoriaDeleteView.as_view(), name="categoria_delete"),
]