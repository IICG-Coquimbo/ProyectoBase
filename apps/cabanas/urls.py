from django.urls import path
from .views import (
    CabanaListView, CabanaDetailView, CabanaCreateView, CabanaUpdateView, CabanaDeleteView,
    ReservaListView, ReservaDetailView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView
)

app_name = "cabanas"

urlpatterns = [
    # Cabañas
    path("", CabanaListView.as_view(), name="cabana_list"),
    path("cabana/<int:pk>/", CabanaDetailView.as_view(), name="cabana_detail"),
    path("cabana/crear/", CabanaCreateView.as_view(), name="cabana_create"),
    path("cabana/editar/<int:pk>/", CabanaUpdateView.as_view(), name="cabana_update"),
    path("cabana/eliminar/<int:pk>/", CabanaDeleteView.as_view(), name="cabana_delete"),
    # Reservas
    path("reserva/", ReservaListView.as_view(), name="reserva_list"),
    path("reserva/<int:pk>/", ReservaDetailView.as_view(), name="reserva_detail"),
    path("reserva/crear/", ReservaCreateView.as_view(), name="reserva_create"),
    path("reserva/editar/<int:pk>/", ReservaUpdateView.as_view(), name="reserva_update"),
    path("reserva/eliminar/<int:pk>/", ReservaDeleteView.as_view(), name="reserva_delete"),
]