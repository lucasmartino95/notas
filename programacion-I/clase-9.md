# Vector

Es un **arreglo unidimensional**. Cada elemento dentro de la **lista o vector** tiene una posición única. Por lo que podremos acceder al elemento indicando su posición. Permite **organizar y ordenar** cantidades de datos grandes. También permite la **escalabilidad** del código. La lista es un **objeto mutable**

```python
notas_perez = [5, 4, 7, 2, 8, 9, 9, 4, 6, 7, 8,2]

for i in range(len(notas_perez)):
    if notas_perez[i] < 6:
        print(f"Perez aún no aprobó la materia {i}")
```

Otrosejemplos de cómo crear una lista

```python
lista_1 = list((1, 2, 3, 66, 7))
print(lista_1)
```

```python
lista = [0] * 5
print(lista)
```

## Memoria stack y memoria heap

La **memoria stack** es estática, tiene un tamaño fijo y predefinado. Almacena variables locales y retornos de una función. Es **gestionada de manera automática** en tiempo de ejecución.

Por otro lado, la **memoria heap** es dinámica, tiende a crecer mucho. Almacena objetos, listas y diccionarios. Es gestionada de manera manual o automática.

- **Manual**: Lo hace el programador. Es el encargado de reservar y liberar la memoria para una variable determinada, por ejemplo en en el lenguaje C.

- **Automática**: Lo gestiona el lenguaje. El mismo reserva espacio en memoria dinámica y al momento de liberar la misma se apoya en un software llamado: Recolector de Basura.