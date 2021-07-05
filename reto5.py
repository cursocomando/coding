# id_department(0),department_name(1),terrain_area(2),old_antenna(3),new_antenna_type(4)
import math
old_range = 18400
new_range = {"a": 35600, "b": 6800, "c": 59300, "d": 24200, "e": 7400}
data = open("data.csv", "r", encoding="utf-8")
matriz = data.readlines()
for i in range(len(matriz)):
    matriz[i] = matriz[i][:-1]
    matriz[i] = matriz[i].split(",")
for i in range(1, len(matriz)):
    matriz[i][0] = int(matriz[i][0])
    matriz[i][2] = float(matriz[i][2])
    matriz[i][3] = int(matriz[i][3])
entrada = input()
entradaLista = entrada.split()
for i in range(len(entradaLista)):
    entradaLista[i] = int(entradaLista[i])
entradaLista.sort()  # 5 1 3
for i in range(len(entradaLista)):
    sumaProm = 0
    previas = 0
    contador = 0
    sumatoriaStd = 0
    sumatoriaStdPrevias = 0
    menor = matriz[1][2]
    mayor = matriz[1][2]
    menorPrevias = matriz[1][3]
    mayorPrevias = matriz[1][3]
    for j in range(len(matriz)):
        if entradaLista[i] == matriz[j][0]:
            id_dpt = entradaLista[i]
            dpt_name = matriz[j][1]
            sumaProm += matriz[j][2]
            previas += matriz[j][3]
            contador += 1
    media = sumaProm / contador
    mediaPrevias = previas / contador
    for j in range(len(matriz)):
        if entradaLista[i] == matriz[j][0]:
            sumatoriaStd += (matriz[j][2] - media) ** 2
            sumatoriaStdPrevias += (matriz[j][3] - mediaPrevias) ** 2
            if matriz[j][2] < menor:
                menor = matriz[j][2]
            if matriz[j][2] > mayor:
                mayor = matriz[j][2]
            if matriz[j][3] < menorPrevias:
                menorPrevias = matriz[j][3]
            if matriz[j][3] > mayorPrevias:
                mayorPrevias = matriz[j][3]
    std = math.sqrt(sumatoriaStd / (contador - 1))
    stdPrevias = math.sqrt(sumatoriaStdPrevias / (contador - 1))
    print(id_dpt, dpt_name)
    print("terrain area")
    print("mean {:.2f}".format(media))
    print("std {:.2f}".format(std))
    print("min {:.2f}".format(menor))
    print("max {:.2f}".format(mayor))
    print("total {:.2f}".format(sumaProm))
    print("old antenna")
    print("mean {:.2f}".format(mediaPrevias))
    print("std {:.2f}".format(stdPrevias))
    print("min {}".format(menorPrevias))
    print("max {}".format(mayorPrevias))
    print("total {}".format(previas))
    totalNuevas = [["a", "b", "c", "d", "e"], [0, 0, 0, 0, 0]]
    for j in new_range:
        cantidadTipo = totalNuevas[1][totalNuevas[0].index(j)]
        for k in range(len(matriz)):
            if entradaLista[i] == matriz[k][0]:
                if j in matriz[k]:
                    cantidad = (matriz[k][2] - (old_range * matriz[k][3])) / new_range[j]
                    cantidad = math.ceil(cantidad)
                    if cantidad < 0:
                        cantidad = 0
                    cantidadTipo += cantidad
        print("{} {}".format(j, cantidadTipo))
