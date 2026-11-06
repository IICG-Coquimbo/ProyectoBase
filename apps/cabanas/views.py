from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Cabana, Reserva


class CabanaListView(ListView):
    model = Cabana
    template_name = "cabanas/cabana_list.html"
    context_object_name = "cabanas"
    paginate_by = 10


class CabanaDetailView(DetailView):
    model = Cabana
    template_name = "cabanas/cabana_detail.html"
    context_object_name = "cabana"


class CabanaCreateView(CreateView):
    model = Cabana
    fields = ("nombre", "capacidad", "precio_noche", "disponible", "foto")
    template_name = "cabanas/cabana_form.html"
    success_url = reverse_lazy("cabanas:cabana_list")


class CabanaUpdateView(UpdateView):
    model = Cabana
    fields = ("nombre", "capacidad", "precio_noche", "disponible", "foto")
    template_name = "cabanas/cabana_form.html"
    success_url = reverse_lazy("cabanas:cabana_list")


class CabanaDeleteView(DeleteView):
    model = Cabana
    template_name = "cabanas/cabana_confirm_delete.html"
    success_url = reverse_lazy("cabanas:cabana_list")


class ReservaListView(ListView):
    model = Reserva
    template_name = "cabanas/reserva_list.html"
    context_object_name = "reservas"
    paginate_by = 10


class ReservaDetailView(DetailView):
    model = Reserva
    template_name = "cabanas/reserva_detail.html"
    context_object_name = "reserva"


class ReservaCreateView(CreateView):
    model = Reserva
    fields = ("cabana", "cliente", "fecha_entrada", "fecha_salida")
    template_name = "cabanas/reserva_form.html"
    success_url = reverse_lazy("cabanas:reserva_list")


class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ("cabana", "cliente", "fecha_entrada", "fecha_salida")
    template_name = "cabanas/reserva_form.html"
    success_url = reverse_lazy("cabanas:reserva_list")


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = "cabanas/reserva_confirm_delete.html"
    success_url = reverse_lazy("cabanas:reserva_list")