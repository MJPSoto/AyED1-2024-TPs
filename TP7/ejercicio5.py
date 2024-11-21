"""
Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas.
"""


def resto_restas_sucesivas(primer_numero: int, segundo_numero: int) -> int:
    """
    Esta función hace el resto entre los numeros a y b utilizando restas sucesivas
    Pre: Esta función recibe 2 parametros en formato entero
    Post: Esta función devuelve el resto de los 2 numeros en formato entero
    """
    if segundo_numero == 0:
        return 0
    if primer_numero < segundo_numero:
        return primer_numero
    return resto_restas_sucesivas(primer_numero - segundo_numero, segundo_numero)


def menu() -> None:
    """
    Esta es la función principal donde se ejecuta todo el codigo
    Pre: Esta función no recibe ningun parametro
    Post: Esta función no devuelve nada
    """
    while True:
        try:
            tupla_numeros = input("Ingrese los numero a, b: ")
            tupla_numeros = tuple(map(int, tupla_numeros.split(",")))
            if len(tupla_numeros) != 2:
                raise ValueError("Verifique los datos ingresados!")
            break
        except ValueError as e:
            print(f"Error: {e}")
    # numero validos
    primer_numero, segundo_numero = tupla_numeros
    salida = resto_restas_sucesivas(primer_numero, segundo_numero)
    print(
        f"El resto entre {primer_numero} y {segundo_numero} por restas sucesivas es {salida}"
    )


if __name__ == "__main__":
    menu()
