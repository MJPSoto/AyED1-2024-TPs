"""
La siguiente función permite averiguar el día de la semana para una fecha determinada. 
La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 
1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.
"""


# funciones
def calcular_dias_semana(dia: int, mes: int, year: int) -> int:
    """
    Esta función calcula el dia de la semana en base a una fecha cualquiera
    pre: Esta función obtiene como parametro 3 numeros enteros mayores a 0
    post: Esta función devuelve un numero entero equivalente al dia de la semana
    """
    # Por la formula de zeller podemos decir que
    if mes < 3:  # esto es por que la formula toma enero y febrero como 13º y 14º
        mes += 12
        year -= 1

    k = year % 100  # Esto es para tomar los ultimos 2 digitos del año
    j = year // 100  # Esto es para tomar los 2 primeros digitos del año

    f_zeller = dia + ((13 * (mes + 1)) // 5) + k + (k // 4) + (j // 4) - 2 * j
    
    #f_zeller % 7 antes habia aplicado esto, pero la formula de zeller esta diseñada para devolver un numero entre 0 a 6, 0 sabado, 1 domingo, etc

    return (f_zeller + 6) % 7  #esto nos da el dia 0 para domingo, 1 para lunes, 2 para martes, etc.

def calcular_calendario(mes:int, year:int):
    """
    Esta función calcula los dias de la semana de un mes y año determinado 
    pre: Esta función obtiene como parametro 2 numero enteros positivos
    post: Esta función muentra en pantalla los dias del mes en semanas 
    """
    if es_bisiesto(year):
        dias_mes = 29
    else:
        dias_mes = dict_mes_dias.get(mes, 30)
    primer_dia_semana = calcular_dias_semana(1, mes, year) #calculo el primer dia para un proximo calculo 

    for i in range(1, dias_mes +1):
        print(f"{i}. {dict_dias.get(calcular_dias_semana(i, mes, year))}") 
        if (i + primer_dia_semana) % 7 == 0:#printeo un salgo de linea cuando se completa la semana 
            print() 
    return None

def es_bisiesto(year: int) -> bool:
    """
    Esta función verifica que el año sea bisiesto.
    Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
    pre: Esta función obtine como parametro un año > 0 de tipo entero
    post: Esta función devuelve True si el año es bisiesto y False si el año no es bisiesto
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def menu():
    while True:
        try:
            tupla_numeros = input("Ingrese una fecha (8,4,2003): ")
            tupla_numeros = tuple(map(int, tupla_numeros.split(",")))
            if len(tupla_numeros) != 3:
                raise ValueError("Verifique los datos ingresados!")
            for valor in tupla_numeros:
                if valor <= 0:
                    raise ValueError("Verifique los datos ingresados!")
            break
        except ValueError as e:
            print(f"Error: {e}")
    #validación correcta 
    dia,mes,year = tupla_numeros #desempaqueto
    calcular_calendario(mes, year)
    dia_semana = calcular_dias_semana(dia,mes,year)
    print(f"El dia de la semana para esa fecha es {dict_dias.get(dia_semana)}")
    return None


# variables globales
dict_dias = {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado"
}

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

# codigo principal
if __name__ == "__main__":
    menu()
