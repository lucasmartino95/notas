# Modularización

La **modularización** permite dividir programas en partes reutilizables y acceder a una amplia biblioteca estándar con herramientas para la manipulación de archivos, redes y gráficos.

**Python** también es extensible, o sea que se pueden integrar funciones escritas en **C** para mejorar el rendimiento o añadir compatiblidad con bibliotecas externas.

# Variables

En Python las variables son más bien **etiquetas**. Una variable es una etiqueta que apunta a un valor en memoria. Por ejemplo:

```python
variable_numerica = 14
print(id(variable_numerica))
print(id(14))
```

**variable_numerica** y el valor **14** tienen la misma etiqueta, o lugar asignado en memoria. Esto permite **optimizar** el uso de memoria en los programas.

Si se limpia la memoria, la dirección del valor la próxima vez que se ejecute el programa será distinta.

Para cada dato que aparece en un programa, **Python** crea un objeto que lo contiene.
Cada objeto tiene:

- **Un identificador único** (un número entero, distinto para cada objeto). El identificador permite a Python referirse al objeto sin ambigüedades.

- **Un tipo de dato** (entero, decimal, cadena de caracteres, etc). El tipo de dato permite saber a Python qué operaciones pueden hacerse con el dato.

- **Un valor** (el valor propio).

### Indicar tipo de dato

En **Python** podemos indicar el tipo de dato de una variable para hacer más legible el código. De todas maneras, el intérprete no toma en cuenta esta indicación. Esto se llama **anotaciones de tipo** (type hints). Por ejemplo:

```python
nombre: str = "Lucas"
edad: int = 30

print(f"Nombre: {nombre}\nEdad: {edad}")
```

# Mutabilidad / Inmutabilidad

La mutabilidad es la posiblidad de cambiar el tipo de dato que contiene una variable.

(Falta completar)