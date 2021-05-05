#Reto 1
#Julian Quintero

import math
#Variables
area_ant = float(input(""))
cant_ant = int(input(""))
tipo_ant = input("")

#Valores
area_ant_inst = 18400
if tipo_ant == "a":
    valor_area = 35600
elif tipo_ant == "b":
    valor_area = 6800
elif tipo_ant == "c":
    valor_area = 59300
elif tipo_ant == "d":
    valor_area = 24200
elif tipo_ant == "e":
    valor_area = 7400
else:
    cant_ant = -1

#Desarrollo
if cant_ant < 0:
    print("error en los datos")
cant_ant_nuev = (area_ant - cant_ant * area_ant_inst) / valor_area
if cant_ant_nuev < 0:
    print ("error en los datos")
else:
    print (math.ceil(cant_ant_nuev))
