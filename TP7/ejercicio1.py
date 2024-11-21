"""
Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
utilizar cadenas de caracteres.
"""


def cantidad_digitos(numero: int) -> int:
    """
    Esta función toma un numero y lo verrifica si es de un digito, si no lo es lo divide por 10 hasta que solo quede un digito
    Pre: Esta función recibe como parametro un numero en fomato enteo
    Post: Esta función devuelve la cantidad de digitos en formato entero
    """
    numero = abs(numero)  # paso el numero a valor absoluto
    contador_digitos = 1
    if numero < 10:  # basicamente el numero es de un digito
        return contador_digitos
    return contador_digitos + cantidad_digitos(
        numero // 10
    )  # a la cantidad que nos da la función le sumamos 1


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
    # numero validado
    salida = cantidad_digitos(numero)
    print(f"La cantidad de digitos del numero {numero} es {salida}")


if __name__ == "__main__":
    menu()
