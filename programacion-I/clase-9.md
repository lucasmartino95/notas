# Vector

Es un **arreglo unidimensional**. Cada elemento dentro de la **lista o vector** tiene una posición única. Por lo que podremos acceder al elemento indicando su posición. Permite **organizar y ordenar** cantidades de datos grandes. También permite la **escalabilidad** del código. La lista es un **objeto mutable**

```python
notas_perez = [5, 4, 7, 2, 8, 9, 9, 4, 6, 7, 8,2]

for i in range(len(notas_perez)):
    if notas_perez[i] < 6:
        print(f"Perez aún no aprobó la materia {i}")
```

# Matrices

Es un vector de vectores.
