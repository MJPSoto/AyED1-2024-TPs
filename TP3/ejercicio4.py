"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna representa el 
día de la semana y cada fila a una de sus fábricas. Ejemplo:

Crear una matriz con datos generados al azar para N fábricas durante una
semana, considerando que la capacidad máxima de fabricación es de 150
unidades por día y puede suceder que en ciertos días no se fabrique ninguna. 
"""

import random as rn
from tabulate import tabulate

rn.seed(1)

def crear_matriz(N: int)->None:
    return [[rn.randint(0, 150) for i in range(6)]for i in range(N)]

def mostrar_cantidad_fabrica()->None:
    for i, valor in enumerate(matriz):
        print(f"La cantidad de bicis en la fabrica {i} es de {sum(valor)}")
    return None

def obtener_mayor_matriz()->None:
    mayores = []
    for i, fila in enumerate(matriz):
        for j, cantidad_bici in enumerate(fila):
            if j == 0 or cantidad_bici > mayor_dia:
                mayor_dia = cantidad_bici
                position_dia_axu = j
        if i == 0 or mayor_dia > mayor_fabrica:
            mayor_fabrica = mayor_dia
            position_fabrica = i
            position_dia = position_dia_axu
    print(f"La fabrica que mas produjo es la fabrica {position_fabrica} en el dia {position_dia}")
    return None

def obtener_mayor():
    lista_completa = []
    for fila in matriz:
        lista_completa.extend(fila) 
    max(lista_completa)
    return max(lista_completa)
matriz = crear_matriz(3)
#print(tabulate(matriz))
#obtener_mayor_matriz()
print(obtener_mayor())
    
