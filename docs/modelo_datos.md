# Modelo de datos (app: clientes)

## Cliente
- rut: CharField(10),obligatorio
- nombre: CharField(100), obligatorio
- telefono:CharField(12),obligatorio
- Categoria: ForeignKey(Categoria)
Regla: Rut solo puede tener numeros y el digito - o k, la k solo puede estar al final del rut debe tener al 6 o 7 caracteres numericos seguido de un - y un numero que puede ser k
el telefono debe comenzar con +569 y el usuario solo puede agregar 8 digitos más, para un total de 12 caracteres.
Un cliente puede estar en una única categoria

## Categoria
- nombre: CharField(8),obligatorio
- Descripcion: Textfield

# Modelo de datos (app: cabanas)
 
## Cabana
- nombre: CharField(100), obligatorio
- capacidad: PositiveIntegerField
- precio_noche: DecimalField(10, 2)
- disponible: BooleanField, default True
- Foto: ImageField

## Reserva
- cabana: ForeignKey(Cabana, related_name="reservas")
- cliente: ForeignKey(Cliente, related_name="reservas")
- fecha_entrada: DateField
- fecha_salida: DateField
 
Regla: fecha_salida debe ser posterior a fecha_entrada.