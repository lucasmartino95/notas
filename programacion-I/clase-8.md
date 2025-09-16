# Recursividad

Repite una función sobre sí misima una **n** cantidad de veces hasta llegar a un punto de salida.

```python
# Cuenta regresiva con for
numero = int(input("Ingrese un número para iniciar cuenta regresiva: "))

for i in range(numero, -1, -1):
    print(i)

# Cuenta regresiva con función recursiva
def contar_regresivamente(n: int) -> None:
    '''
    Cuenta regresivamente

    Recibe un número desde el que inicia la cuenta

    No retorna nada
    '''

    if n == -1:
        print("Finalizó")
    else:
        print(n)
        contar_regresivamente(n - 1)

print("Ahora se aplica la recursividad")

contar_regresivamente(10)
```
