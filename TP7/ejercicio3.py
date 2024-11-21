"""
Escribir una función que devuelva la suma de los N primeros números naturales.
"""


def suma_primos(numero: int) -> int:
    """
    Esta función suma los N numeros primeros que sean numeros naturales
    Pre: Esta función recibe como parameto un numero en fomato entero
    Post: Esta función devuelve la suma de los n numeros primeros en formato entero
    """
    if numero == 1:
        return 1
    return numero + suma_primos(numero - 1)  # nose


def menu() -> None:
    """
    Esta es la función principal donde se ejecuta todo el codigo
    Pre: Esta función no recibe ningun parametro
    Post: Esta función no devuelve nada
    """
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    # numero valido
    salida = suma_primos(numero)
    print(f"La suma de los N numeros primeros natuarles de {numero} es {salida}")


if __name__ == "__main__":
    menu()
