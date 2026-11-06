# Reglas de base de datos

- Nombres de modelos en singular y CamelCase (ej. Cabana, Reserva).
- Nombres de campos en snake_case.
- Toda ForeignKey debe llevar related_name explícito.
- Usa DecimalField para montos de dinero, nunca FloatField.