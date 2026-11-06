# Reglas de vistas y templates

## Vistas
- Usa SOLO vistas basadas en clases genericas de Django
  (django.views.generic). NUNCA escribas vistas como funciones (def).
- Elige la clase segun la tarea:
  - ListView: listar registros
  - DetailView: ver un registro
  - CreateView: formulario para crear
  - UpdateView: formulario para editar
  - DeleteView: pantalla de confirmacion y borrado
  - TemplateView: pagina fija (por ejemplo, la de inicio)
- Nombre de la clase: <Modelo><Accion>View
  (ejemplo: CabanaListView, CabanaCreateView).
- Atributos minimos: model. En CreateView y UpdateView agrega fields.
- En CreateView, UpdateView y DeleteView define success_url con reverse_lazy.
- Todas las vistas van en apps/<app>/views.py.
- No modifiques models.py ni admin.py al crear vistas.

## URLs
- Cada app tiene su apps/<app>/urls.py con app_name = "<app>".
- Usa path("...", MiVista.as_view(), name="...").
- Nombres de url: <modelo>_list, <modelo>_detail, <modelo>_create,
  <modelo>_update, <modelo>_delete.
- Incluye las urls de cada app en config/urls.py con include().
- La pagina de inicio es un TemplateView en config/urls.py con name="inicio".

## Templates
- Usa los nombres por defecto de Django; asi no hace falta template_name:
  - apps/<app>/templates/<app>/<modelo>_list.html
  - apps/<app>/templates/<app>/<modelo>_detail.html
  - apps/<app>/templates/<app>/<modelo>_form.html (sirve para Create y Update)
  - apps/<app>/templates/<app>/<modelo>_confirm_delete.html
- El template base esta en templates/base.html (carpeta en la raiz del
  proyecto, registrada en TEMPLATES["DIRS"] de settings).
- Todo template empieza con {% extends "base.html" %} y escribe su
  contenido dentro de {% block content %}.
- Estilos: Bootstrap 5 por CDN, con clases de Bootstrap.
- En las listas se recorre object_list; en el detalle se usa object.
- Formularios: <form method="post">, {% csrf_token %} y {{ form.as_p }}.
- Los enlaces usan {% url 'app:nombre' %}, nunca rutas escritas a mano.
