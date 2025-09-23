conjunto_1 = [1, 2, 3, 4]
conjunto_2 = [3, 4, 5]

diferencia = [False] *len(conjunto_2)

z = 0

for i in range(len(conjunto_1)):
    bandera = True
    for j in range(len(conjunto_2)):
        if conjunto_1[i] == conjunto_2[j]:
            bandera = False
            break
    
    if bandera == True:
        diferencia[z] = conjunto_1[i]
        z += 1

    print(diferencia)