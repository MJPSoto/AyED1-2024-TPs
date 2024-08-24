"""
Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
"""


# funciones
def validar_fecha(dia: int, mes: int, year: int) -> bool:
    """
    Esta función valida una fecha
    pre: esta funcion obtiene 3 numeros enteros
    post: Esta función devuelve true si la fecha es valida, sino devuelve false
    """
    return (
        dia >= 1
        and mes in dict_mes_dias
        and dia <= dict_mes_dias.get(mes)
        and es_bisiesto(year) == False
    )


def es_bisiesto(year: int) -> bool:
    """
    Esta función verifica que el año sea bisiesto.
    Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
    pre: Esta función obtine como parametro un año > 0 de tipo entero
    post: Esta función devuelve True si el año es bisiesto y False si el año no es bisiesto
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def menu() -> None:
    """
    Esta función es el main, valida que el usuario ingrese 3 numeros correspondiente cada uno a (dia, mes, año)
    y despues muestra si la fecha ingresada es valida
    """
    while True:
        try:
            tupla_numeros = input(
                "Ingrese el (dia, mes, año): "
            )  # esto me devuelve una tupla de los 3 numeros (num1, num2, num3)
            tupla_numeros = tuple(map(int, tupla_numeros.split(",")))
            if len(tupla_numeros) != 3:
                raise ValueError("Debe ingresar exactamente tres valores")
            for valor in tupla_numeros:
                if valor <= 0:
                    raise ValueError("Verifique los datos ingresados!")
            break
        except ValueError as e:
            print(f"Error: {e}")
    # validacion correcta
    dia, mes, year = tupla_numeros  # desempaqueto la tupla
    validation = validar_fecha(dia, mes, year)
    if validation:
        print("La fecha ingresada es correcta")
    else:
        print("La fecha ingresada no es correcta")
    test_validacion()
    return None


def test_validacion() -> None:
    """
    Esta función es para validar que la función de validar la fecha este funcionando bien
    """
    assert (validar_fecha(1, 2, 2001)) == True  # fecha valida
    assert (validar_fecha(1, 1, 1980)) == False  # año bisiesto
    assert (validar_fecha(1, 13, 2001)) == False  # mes errado
    assert (validar_fecha(-1, 1, 2001)) == False  # dia negativo
    assert (validar_fecha(32, 1, 2001)) == False  # dia errado
    assert (validar_fecha(12, 12, 2005)) == True  # fecha valida
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

# codigo principal
if __name__ == "__main__":

    menu()
