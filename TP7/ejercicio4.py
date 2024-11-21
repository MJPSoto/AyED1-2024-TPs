"""
Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.
"""


def producto_sumas_sucesivas(primer_numero: int, segundo_numero: int) -> int:
    """
    Esta función hace el producto entre 2 numeros a y b por sumas sucesivas
    Pre: Esta función recibe 2 parametros en formato entero, uno que representa lo que vamos a sumar y el otro es para ver cuantas veces vamos a sumarlo
    Post: Esta función devuelve la suma de los 2 numeros en formato entero
    """
    if segundo_numero == 0:
        return 0
    # por cada pasada vuelvo a llamar a la funcion pero al segundo valor le resto 1, basicamente esto se va a repetir hasta que el segundo valor sea 0
    return primer_numero + producto_sumas_sucesivas(primer_numero, segundo_numero - 1)


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
    salida = producto_sumas_sucesivas(primer_numero, segundo_numero)
    print(
        f"El producto entre {primer_numero} y {segundo_numero} por sumas sucesivas es {salida}"
    )


if __name__ == "__main__":
    menu()
