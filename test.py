def inicializar_lista(cantidad_elementos: int, valor_por_defecto: any = 0) -> list:
    return [valor_por_defecto] * cantidad_elementos


def mostrar_lista(lista: list):
    for i in range(len(lista)):
        print(f"Indice {i} = {lista[i]}")
        

lista_2 = inicializar_lista(9, "m")    

lista_2[2] = "a"

mostrar_lista(lista_2)