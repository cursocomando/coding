import math
dict_antenas = {    "a": 35600,    "b": 6800,    "c": 59300,    "d": 24200,    "e": 7400,    "existentes": 18400}
#lectura separada y distribucion de listas desde input inicial 
datos = input()
lista_datos = datos.split(" ")
num_departamentos = int(lista_datos[0])
num_terrenos = int(lista_datos[1])
while num_departamentos < 1: #correción de errores del paso anterior en caso de <1
    datos = input()
    lista_datos = datos.split(" ")
    num_departamentos = int(lista_datos[0])
    terrenos = int(lista_datos[1])
acum_tipoantenas_dept = [] #lista general para acumular la data de las antenas en los departamentos
for i in range(num_departamentos): 
    acum_tipoantenas_dept.append([0,0,0,0,0]) #creación de elementos para los tipos de antena 
for i in range(num_terrenos):
    datos_terr = input() #siguiente input 
    lista_datosterr = datos_terr.split(" ") #dividir el input ej: ["1", "63000", "24", "c"]
    seleccion_depto = int(lista_datosterr[0]) 
    area_por_cubrir = float(lista_datosterr[1])
    ant_existentes = int(lista_datosterr[2])
    tipo_de_antena = lista_datosterr[3] #ahora quedaría en [1, 63000, 24, "c"]
    
    while ant_existentes <0: #Depuración de error por condicional
        datos_terr = input() #siguiente input 
        lista_datosterr = datos_terr.split(" ") #dividir el input ej: ["1", "63000", "24", "c"]
        seleccion_depto = int(lista_datosterr[0])
        area_por_cubrir = float(lista_datosterr[1])
        ant_existentes = int(lista_datosterr[2])
        tipo_de_antena = lista_datosterr[3].lower() #ahora quedaría en [1, 63000, 24, "c"]. lower para correción de mayúisculas
    
    if num_departamentos < seleccion_depto or (tipo_de_antena !="a" and tipo_de_antena !="b" and tipo_de_antena != "c" and tipo_de_antena != "d" and tipo_de_antena != "e") : #Condicional por cantidad de departamentos y tipo de antenas
        continue
#PROCESO - Cálculo para deducir la cantidad de antenas nuevas
    if tipo_de_antena == "a": 
        cobertura_actual = ant_existentes* dict_antenas["existentes"] #Cálculo
        area_proceso = area_por_cubrir - cobertura_actual #Cálculo
        cantidad_antenas_nuevas = math.ceil(area_proceso / dict_antenas[tipo_de_antena]) #Cálculo
        if cantidad_antenas_nuevas <0: #Depuración de errores por condicional
            cantidad_antenas_nuevas = 0
        acum_tipoantenas_dept[seleccion_depto-1][0] += cantidad_antenas_nuevas # acumulador por posicion en la matriz 
    if tipo_de_antena == "b": 
        cobertura_actual = ant_existentes* dict_antenas["existentes"]
        area_proceso = area_por_cubrir - cobertura_actual
        cantidad_antenas_nuevas = math.ceil(area_proceso / dict_antenas[tipo_de_antena])
        if cantidad_antenas_nuevas <0:
            cantidad_antenas_nuevas = 0
        acum_tipoantenas_dept[seleccion_depto-1][1] += cantidad_antenas_nuevas # acumulador por posicion en la matriz
    if tipo_de_antena == "c": 
        cobertura_actual = ant_existentes* dict_antenas["existentes"]
        area_proceso = area_por_cubrir - cobertura_actual
        cantidad_antenas_nuevas = math.ceil(area_proceso / dict_antenas[tipo_de_antena])
        if cantidad_antenas_nuevas <0:
            cantidad_antenas_nuevas = 0
        acum_tipoantenas_dept[seleccion_depto-1][2] += cantidad_antenas_nuevas # acumulador por posicion en la matriz
    if tipo_de_antena == "d": 
        cobertura_actual = ant_existentes* dict_antenas["existentes"]
        area_proceso = area_por_cubrir - cobertura_actual
        cantidad_antenas_nuevas = math.ceil(area_proceso / dict_antenas[tipo_de_antena])
        if cantidad_antenas_nuevas <0:
            cantidad_antenas_nuevas = 0
        acum_tipoantenas_dept[seleccion_depto-1][3] += cantidad_antenas_nuevas # acumulador por posicion en la matriz
    if tipo_de_antena == "e": 
        cobertura_actual = ant_existentes* dict_antenas["existentes"]
        area_proceso = area_por_cubrir - cobertura_actual
        cantidad_antenas_nuevas = math.ceil(area_proceso / dict_antenas[tipo_de_antena])
        if cantidad_antenas_nuevas <0:
            cantidad_antenas_nuevas = 0
        acum_tipoantenas_dept[seleccion_depto-1][4] += cantidad_antenas_nuevas # acumulador por posicion en la matriz
lista_total_suma_depto = [] #Creación de la lista total
for i in range(num_departamentos):
    suma = 0
    for j in range(5):
        suma = suma + acum_tipoantenas_dept[i][j]
    lista_total_suma_depto.append(suma)
pos_min = lista_total_suma_depto.index(min(lista_total_suma_depto))
pos_max = lista_total_suma_depto.index(max(lista_total_suma_depto))
tipo_ant = ['a', 'b', 'c', 'd', 'e']
#Como aparecía en la tutoría
for i in range(num_departamentos):
    print(i + 1)
    print((lista_total_suma_depto[i]))  # Aqui se debe sumar los valores del vector acum_type_ant en la posicion i
    # tipo antena max y min
    max_ant = max(acum_tipoantenas_dept[i])
    min_ant = min(acum_tipoantenas_dept[i])
    indice_max = acum_tipoantenas_dept[i].index(max_ant)
    indice_min = acum_tipoantenas_dept[i].index(min_ant)
    print(tipo_ant[indice_min], min_ant)
    print(tipo_ant[indice_max], max_ant)
acum_tipo_antenas = [[],[],[],[],[]]
for zona in acum_tipoantenas_dept:
    for j in range(len(tipo_ant)):
        
        acum_tipo_antenas[j].append(zona[j])
i = 0
for algo in acum_tipo_antenas:
    # encontrar min
    valor_min = min(algo)
    ind_min = algo.index(valor_min)
    # encontrar max
    valor_max = max(algo)
    ind_max = algo.index(valor_max)
    # asignarle a cada uno el indice, y sumarle 1
    print((ind_min + 1), tipo_ant[i], valor_min)
    print((ind_max + 1), tipo_ant[i], valor_max)
    i += 1
