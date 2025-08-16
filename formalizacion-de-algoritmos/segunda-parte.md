# Estructuras condicionales

Una **instrucción condicional** permite hacer algo si se cumple una condición, y no hacerlo si no se cumple.

También podemos decir, que **bifurcan** el código, es decir, **alteran el flujo secuencial** para que el programa tome decisiones. Esto se llama, **flujo de selección**.

Un **flujo de selección** consta de las siguientes alternativas:

- Flujo de selección simple: (if).
- Flujo de selección doble (if-else).
- Flujo de selección anidado.

A continuación se puede ver una instrucción condicional escrita de **manera informal** (Pseudocódigo).

```
si (verdad o falso): realiza alguna acción si es verdad
```

En **Python** la palabra clave asociada a esta instrucción es `if`. Por ejemplo:

```python
if 25 >= 8:
    print("Puedo salir a caminar")
```

Si la condición es falsa y queremos hacer algo cuando esto sucede, podemos usar la palabra clave `else`. Por ejemplo:

```python
if 7 >= 8:
    print("Puedo salir a caminar")
else:
    print("No puedo salir a caminar")
```

También podemos establecer la condición de entrada. En el siguiente caso, utilizando `True` en la primer condición, siempre se ejecutará el código dentro de esa condición.


```python
if True:
    print("Puedo salir a caminar")
else:
    print("No puedo salir a caminar")
```

### Instrucciones if-else anidadas

Podemos **anidar** nuestras instrucciones condicionales si necesitamos hacer nuestro código **un poco más complejo**, donde se evalúan múltiples condiciones en un orden específico.

```python
edad = 25
if edad >= 18:
    if edad > 22:
        print("Es mayor de edad y mayor a 22.")
    else:
        print("Es mayor de edad pero menor a 22.")
else:
    print("Es menor de edad.")
```

La **sangria** mejora la legibilidad y hace que el código sea más fácil de entender y rastrear. Se recomienda elegir entre el **espacio o tabulador** para lograr la sangria. Además que es una **regla de sintáxis** en Python, para ejecutar bloques de código.

### Instrucción elif

Por último, si queremos verificar más de una condición y detener el programa cuando se encuentre la primer condición verdadera, podemos usar `elif`. Por ejemplo:

```python
valor = int(input("Ingrese un numero del 1 al 3: "))

if valor == 1:
    print("Es lunes.")
elif valor == 2:
    print("Es Martes.")
elif valor == 3:
    print("Es Miercoles.")
else:
    print("No ha elegido ningun valor entre 1 y 3")
```

### Alternativa de la instrucción elif

En 2021, **Python** añadió una característica para hacer **estructuras condicionales múltiples**: match-case.

```python
print("MENÚ DE OPCIONES")
print("[1] Ventas")
print("[2] Soporte")
print("[3] Administración")

opcion = int(input("Elegir opción: "))

match opcion:
    case 1:
        print("VENTAS")
    case 2:
        print("SOPORTE")
    case 3:
        print("ADMINISTRACIÓN")
    case _: # Comodín: En caso de que no se cumplan las sentencias anteriores
        print("Opción inexsistente")
```

### Comentarios

Los comentarios son útiles para **aclarar** lo que hace determinado bloque de código. Además, los comentarios son ignorados por el intérprete de Python, solo están en el código como referencia.

## Operadores lógicos