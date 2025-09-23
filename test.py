lista_a = [3, 7, 9, 10, 12]
lista_b = [5, 7, 9, 12]

def recortar_lista(lista: list,
                   limite: any = False) -> list:
    '''
    '''
    for i in range(len(lista)):
        if lista[i] == limite:
            indice_final = i
            break

    # Slicing
    # lista = lista[0:indice_final]
    lista_retorno = lista[0:indice_final]
    return lista_retorno


def calcular_interseccion(conjunto_1: list,
conjunto_2: list) -> list:

    '''
    Calcula la intersección entre dos conjuntos

    Recibe dos conjuntos de números

    Retorna la intersección en forma de lista
    '''

    if len(conjunto_1) < len(conjunto_2):
        cantidad_retorno = len(conjunto_1)
    else:
        cantidad_retorno = len(conjunto_2)

    lista_retorno = [False] * cantidad_retorno

    z = 0

    for i in range(len(conjunto_1)):

        for j in range(len(conjunto_2)):
            print(f"i = {i}, j = {j}")
            print(f"{conjunto_1[i]}, {conjunto_2[j]}")
            if conjunto_1[i] == conjunto_2[j]:
                lista_retorno[z] = conjunto_1[i]
                z += 1
                break
    
    lista_retorno = recortar_lista(lista_retorno)
    return lista_retorno


print(calcular_interseccion(lista_a, lista_b))