"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""


def diasiguiente(dia: int, mes: int, year: int) -> tuple:
    """
    Esta funcion agrega un dia a una fecha cualquiera 
    pre: Esta función obtiene como parametro 3 numeros enteros positivos 
    post: Esta función devuelve una tupla con el dia siguiente (dia, mes, año)
    """
    if mes == 2 and es_bisiesto(year):
        dias_mes = 29
    else:
        dias_mes = dict_mes_dias.get(mes, 30)
    if dia >= dias_mes:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            year += 1
    else:
        dia += 1
    return (dia, mes, year)


def sumar_n_dias(dia: int, mes: int, year: int, cantidad_dias: int) -> tuple:
    """
    Esta función suma a una fecha cualquiera N cantidad de dias
    pre: Esta función obtiene como parametro 4 numeros enteros positivos 
    post: Esta función devuelve una tupla equivalente al (dia, mes, año) con la suma de N dias 
    """
    for _ in range(cantidad_dias):
        dia, mes, year = diasiguiente(dia, mes, year)
    return (dia, mes, year)


def es_bisiesto(year: int) -> bool:
    """
    Esta función verifica que el año sea bisiesto.
    Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
    pre: Esta función obtine como parametro un año > 0 de tipo entero
    post: Esta función devuelve True si el año es bisiesto y False si el año no es bisiesto
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def dias_entre_fechas(fecha_inicial: tuple, fecha_fin: tuple) -> int:
    """
    Esta funcion calcula la diferencia en dias entre 2 fechas 
    pre: Esta función obtiene como parametro 2 tuplas de 3 numeros enteros equivalentes al dia, mes ,año 
    post: Esta función devuelve un entero que equivale a la diferencia entre las 2 fechas en dias 
    """
    dia_inicial, mes_inicial, year_inicial = fecha_inicial
    dia_fin, mes_fin, year_fin = fecha_fin
    cantidad_dias = 0

    while (dia_inicial, mes_inicial, year_inicial) != (dia_fin, mes_fin, year_fin):
        dia_inicial, mes_inicial, year_inicial = diasiguiente(
            dia_inicial, mes_inicial, year_inicial
        )
        cantidad_dias += 1

    return cantidad_dias


def mostrar_menu():
    for key, valor in dict_opciones_disponibles.items():
        print(f"{key}. {valor}")
    return None


def input_fecha():
    while True:
        try:
            tupla_fecha = tuple(
                map(int, input("Ingrese una fecha (dia, mes, año): ").split(","))
            )
            if len(tupla_fecha) != 3:
                raise ValueError("Verifique los datos ingresados!")
            for valor in tupla_fecha:
                if valor <= 0:
                    raise ValueError("Verifique los datos ingresados!")
            break
        except ValueError as e:
            print(f"Error: {e}")
    return tupla_fecha


def validar_num(num):
    return isinstance(num, int)


def input_cantidad():
    while True:
        try:
            num = int(input(f"Ingrese la cantidad de dias para agregar: "))
            if validar_num(num) and num > 0:
                break
            raise ValueError("Verifique el valor ingresado!")
        except ValueError as e:
            print(f"Error: {e}")
    return num


def menu():
    mostrar_menu()
    while True:
        try:
            opcion = int(input("Seleccione una de las siguiente opciones: "))
            if opcion in dict_opciones_disponibles:
                break
            raise ValueError("Verifique el valor ingresado!")
        except ValueError as e:
            print(f"Error: {e}")
    test_validacion()
    match (opcion):
        case 1:
            tupla_fecha = input_fecha()
            dia, mes, year = tupla_fecha
            cantidad_dias = input_cantidad()
            salida = sumar_n_dias(dia, mes, year, cantidad_dias)
            print(f"Sumando los dias a la fecha ingresada queda {salida}")
            pass
        case 2:
            tupla_fecha_inicio = input_fecha()
            tupla_fecha_fin = input_fecha()
            cantidad_dias = dias_entre_fechas(tupla_fecha_inicio, tupla_fecha_fin)
            print(f"La diferencia entre las 2 fechas en dias es: {cantidad_dias}")
        case -1:
            print("Adios...")
    return None

def test_validacion() -> None:
    """
    Esta función es para validar el funcionamiento del programa
    """
    assert (dias_entre_fechas((28,2,2024),(28,2,2025))) == 366
    assert (dias_entre_fechas((28,2,2024), (31,3,2024))) == 32
    assert (sumar_n_dias(10,1,2024, 20)) == (30,1,2024)
    assert (diasiguiente(28,2,2024)) == (29,2,2024)
    assert (diasiguiente(1,3,2024)) == (2,3,2024)
    return None

# variables globales
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

dict_opciones_disponibles = {
    1: "Sumar N dias a una fecha",
    2: "Calcular la cantidad de días existentes entre dos fechas cualesquiera",
    -1: "Salir",
}
# codigo principal
if __name__ == "__main__":
    menu()
