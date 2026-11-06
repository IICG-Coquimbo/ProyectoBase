from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Cliente, Categoria


class ClienteListView(ListView):
    model = Cliente
    template_name = "clientes/cliente_list.html"
    context_object_name = "clientes"
    paginate_by = 10


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "clientes/cliente_detail.html"
    context_object_name = "cliente"


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ("rut", "nombre", "telefono", "categoria")
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy("clientes:cliente_list")


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ("rut", "nombre", "telefono", "categoria")
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy("clientes:cliente_list")


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "clientes/cliente_confirm_delete.html"
    success_url = reverse_lazy("clientes:cliente_list")


class CategoriaListView(ListView):
    model = Categoria
    template_name = "clientes/categoria_list.html"
    context_object_name = "categorias"


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "clientes/categoria_detail.html"
    context_object_name = "categoria"


class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ("nombre", "descripcion")
    template_name = "clientes/categoria_form.html"
    success_url = reverse_lazy("clientes:categoria_list")


class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ("nombre", "descripcion")
    template_name = "clientes/categoria_form.html"
    success_url = reverse_lazy("clientes:categoria_list")


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "clientes/categoria_confirm_delete.html"
    success_url = reverse_lazy("clientes:categoria_list")