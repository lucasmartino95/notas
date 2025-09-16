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

Otro ejemplo de recursividad

```python
# Factorial de 5
# 5!
# 5 * 4 * 3 * 2 * 1

factorial = int(input("Ingrese el número del que quiere calcular el factorial: "))

def calcular_factorial(n: int) -> int:

    if n == 0: # Caso base
        resultado = 1
    else:
        resultado = n * calcular_factorial(n - 1)

    return resultado


resultado_ejemplo = calcular_factorial(factorial)

print(f"El factorial de {factorial} es {resultado_ejemplo}")
```
