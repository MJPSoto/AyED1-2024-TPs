"""
Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""

# librerias
from datetime import date


# funciones
def convertir_fecha_texto(fecha_tupla: tuple) -> str:
    """
        Devuelve la fecha formateada a un valor legible 2024/12/11 a 11 de diciembre de 2024
        pre: Recibe como parametro una tupla de enteros
        post: Devuelve la fecha formateada para ser legible
    """
    year, month, day = fecha_tupla
    return " ".join([str(day), "de", dict_month[month], "de", str(year)])


def validar_campo(mensaje: str):
    """
        Devuelve un valor que sea valido con ese formato en este caso que tenga 3 datos separados con coma
        pre: Recibe como parametro un mensaje en formato str 
        post: Devuelve el valor ingresado por el usuario, pero que cumpla el formato correcto
    """
    try:
        valor = input(mensaje)
        valor = tuple(valor.split(","))

        if len(valor) != 3:
            raise ValueError(
                "Datos inválidos. Deben ser tres valores separados por comas."
            )

        if len(valor[0]) != 4 or len(valor[1]) != 2 or len(valor[2]) != 2:
            raise ValueError("El formato de la fecha debe ser 'AAAA,MM,DD'.")

        valor = tuple(map(int, valor))
        year, month, day = valor

        date(year, month, day)
        return valor
    except ValueError as e:
        print(f"Error: {e}")
        return validar_campo(mensaje)


def main():
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    fecha_valida = validar_campo("Ingrese la fecha (año, mes, dia): ")
    print(convertir_fecha_texto(fecha_valida))
    return


# variables globales
dict_month = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre",
}

# codigo principal
if __name__ == "__main__":
    main()
