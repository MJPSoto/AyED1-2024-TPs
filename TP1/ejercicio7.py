"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""

dict_mes_dias = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def diasiguiente(dia:int, mes:int,year:int) ->tuple:
    dias_mes = dict_mes_dias.get(mes)
    if dia >= dias_mes and mes in dict_mes_dias:
        mes += 1 #se le suma 1 para cambiar al mes siguiente 
        dia = 1 #se reinicia pq es el primer dia del siguiente mes 
        diasiguiente(dia, mes, year)
    else:
        dia += 1
    return (dia, mes, year)


def sumar_n_dias(dia:int, mes:int,year:int, cantidad_dias: int) ->tuple:
    contador = 0
    ultima_fecha = ()
    while True:
        if contador == cantidad_dias:
            break
        ultima_fecha = diasiguiente(dia, mes, year)
        dia,mes = ultima_fecha[0], ultima_fecha[1]
        contador +=1
    return ultima_fecha

print(sumar_n_dias(1,2,2024,20))

