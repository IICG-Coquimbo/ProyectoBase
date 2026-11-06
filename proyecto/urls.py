"""URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
include("apps.clientes.urls", namespace="clientes"),
include("apps.cabanas.urls", namespace="cabanas"),

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/", include("apps.clientes.urls", namespace="clientes")),
    path("cabanas/", include("apps.cabanas.urls", namespace="cabanas")),
    # Home
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]