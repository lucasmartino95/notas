lista = [3, 5, 6, 8, 9, 11]


def buscar_lineal(lista: list, buscado: int) -> int:
    for i in range(len(lista)):
        if lista[i] == buscado:
            return i
    
    print("No se encuentra el elemento buscado")


pos = buscar_lineal(lista, 8)

print(f"El 8 se encuentra en la posición {pos}")