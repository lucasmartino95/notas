factorial = int(input("Ingrese el número del que quiere calcular el factorial: "))

def calcular_factorial(n: int) -> int:

    if n == 0:
        resultado = 1
    else:
        resultado = n * calcular_factorial(n - 1)

    return resultado


resultado_ejemplo = calcular_factorial(factorial)

print(f"El factorial de {factorial} es {resultado_ejemplo}")