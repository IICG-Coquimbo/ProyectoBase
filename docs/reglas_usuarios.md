# Reglas de usuarios y acceso

## Usuarios
- Usa el sistema de usuarios de Django (django.contrib.auth) con el
  modelo User por defecto. NO crees un modelo de usuario propio.
- Nunca guardes contrasenas en texto plano ni crees campos de contrasena.

## App cuentas (apps/cuentas)
- Las vistas de acceso van en apps/cuentas/views.py y urls.py,
  tambien basadas en clases:
  - Login: LoginView de django.contrib.auth.views
  - Logout: LogoutView de django.contrib.auth.views
  - Registro: CreateView con UserCreationForm y
    success_url = reverse_lazy("cuentas:login")
- app_name = "cuentas". Nombres de url: login, logout, registro.
- Templates en apps/cuentas/templates/cuentas/: login.html y registro.html,
  ambos extienden base.html.
- En Django 5, LogoutView solo acepta POST: el boton "Salir" debe ser un
  <form method="post"> con {% csrf_token %}, nunca un enlace.

## Settings (config/settings/base.py)
- LOGIN_URL = "cuentas:login"
- LOGIN_REDIRECT_URL = "inicio"
- LOGOUT_REDIRECT_URL = "cuentas:login"

## Proteger vistas
- Para exigir sesion iniciada, pon LoginRequiredMixin como PRIMER padre:
  class CabanaListView(LoginRequiredMixin, ListView)
- Para exigir un permiso, usa PermissionRequiredMixin con
  permission_required = "<app>.<accion>_<modelo>"
  (ejemplo: "cabanas.add_cabana").
- Los roles son Grupos de Django creados desde el admin
  (ejemplo: Administrador, Recepcionista). No los programes en el codigo.
