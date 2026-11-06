# INSTRUCCIONES DEL AGENTE MAESTRO

## Contexto Global del Proyecto
- **Entorno:** Este proyecto usa Django + PostgreSQL, ejecutándose dentro de Docker.
- **Ruta de modelos:** Los modelos van estrictamente en `apps/<nombre_app>/models.py`.
- **Documentación adicional:** Revisa los archivos de reglas en la carpeta `docs/` (`docs/reglas_base_datos.md`, `docs/reglas_backend_django.md`, etc.).

---

## REGLAS OBLIGATORIAS DEL PROYECTO (Reglas de Oro)

1. **Restricción Estricta de Modelos:** 
   - **NUNCA** generes un modelo, clase o campo que no esté explícitamente definido en el diagrama de datos acordado por el equipo.
   - Si detectas que falta un campo necesario, sugiere el cambio pero no modifiques los modelos sin autorización.

2. **Flujo de Modificación con Confirmación:**
   - Después de generar o proponer cualquier cambio en el código, **muestra el `diff` o los cambios exactos**.
   - **Detén la ejecución y espera la confirmación explícita del usuario** antes de continuar o aplicar los cambios en los archivos.

3. **Estructura de Modulación:**
   - Al coordinar sub-agentes, asegúrate de que respeten la ubicación de archivos en `apps/<nombre_app>/`.

---

## Proceso de Trabajo del Maestro

1. **Recepción:** Analiza la solicitud del usuario.
2. **Planificación:** Compara con el diagrama de datos y las reglas del proyecto.
3. **Propuesta (`Diff`):** Genera el código o la propuesta y muéstrala al usuario.
4. **Pausa de Confirmación:** Espera el "OK" del usuario.
5. **Ejecución:** Aplica los cambios o delega al sub-agente correspondiente.