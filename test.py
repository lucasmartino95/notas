def inicializar_lista(cantidad_elementos: int, valor_por_defecto: any = 0) -> list:
    return [valor_por_defecto] * cantidad_elementos


lista = inicializar_lista(9, "m")
print(lista)