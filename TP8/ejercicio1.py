"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""

from datetime import date, timedelta, datetime


def sumar_n_dias(fecha: tuple, dias: int) -> tuple:
    """
    Suma N cantidad de dias a una fecha determinada
    pre: Recibe como parametro una fecha en formato de tupla (año, mes, dias) y la cantidad de dias a sumar en forma entero
    post: Devuelve una tupla con la nueva fecha despues de sumarle los N dias
    """
    año, mes, día = fecha
    nueva_fecha = date(año, mes, día) + timedelta(days=dias)
    return (nueva_fecha.year, nueva_fecha.month, nueva_fecha.day)


def validar_campo(mensaje: str, validation=False, validar_fecha=False):
    """
    Valida los campos que tengan un formato determinado o que se quieran castear
    pre: Recibe como parametro un mensaje en formato str y 2 booleanos con un valor por default en False
    post: Devuelve el valor con el formato correcto
    no tiene typehint pq puede validar que se pueda castear a entero o validar una fecha
    en teoria las funciones hacen una sola cosa, peroo.......
    """
    try:
        valor = input(mensaje)
        if validation:
            valor = tuple(map(int, valor.split(",")))
            if len(valor) != 3:
                raise ValueError("Datos invalidos. Reintentelo")
            if validar_fecha:
                year, month, day = valor
                date(year, month, day)
            return valor
        return int(valor)
    except ValueError as e:
        print(e)
        return validar_campo(mensaje, validation, validar_fecha)


def diff_horarios(horarios: tuple) -> tuple:
    """
    Obtiene la diferencia entre 2 horarios HH:MM:SS
    Pre: Recibe una tupla de tuplas con 2 elementos y cada tupla 3 elementos ((HH:MM:SS), (HH:MM:SS))
    post: Devuelve una tupla con la diferencia entre horarios
    """
    primer_horario, segundo_horario = horarios
    h1 = timedelta(
        hours=primer_horario[0], minutes=primer_horario[1], seconds=primer_horario[2]
    )
    h2 = timedelta(
        hours=segundo_horario[0], minutes=segundo_horario[1], seconds=segundo_horario[2]
    )

    diferencia = abs(h1 - h2)
    if diferencia > timedelta(hours=12):
        diferencia = timedelta(hours=24) - diferencia

    horas = diferencia.seconds // 3600
    minutos = (diferencia.seconds % 3600) // 60
    segundos = diferencia.seconds % 60
    return (horas, minutos, segundos)


def main():
    """
    Funcion principal donde se ejecuta todo el codigo
    Pre: No recibe ningun parametro
    Post: No devuelve nada
    """
    fecha = validar_campo("Ingrese la fecha (año, mes, dia): ", True, True)
    dias = validar_campo("Ingrese la cantidad de dias a sumar: ")

    suma_fecha = sumar_n_dias(fecha, dias)
    print(f"Fecha resultante después de sumar {dias} días es: {suma_fecha}")

    primer_horario = validar_campo("Ingrese el primer horario (HH,MM,SS): ", True)
    segundo_horario = validar_campo("Ingrese el segundo horario (HH,MM,SS): ", True)
    tupla_horarios = primer_horario, segundo_horario

    diferencia = diff_horarios(tupla_horarios)
    print(f"La diferencia entre los horarios {tupla_horarios} es: ")
    print(f"{diferencia}")
    return


if __name__ == "__main__":
    main()
