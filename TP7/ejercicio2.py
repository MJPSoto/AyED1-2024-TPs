"""
Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal. 
"""


def convertir_bina_deci(binario: int, position: int = 0) -> int:
    """
    Esta función convierte un numero binario en decimal
    Pre: Esta función recibe 2 parametros en formato entero, uno que es el numero binario y el otro que el la posición del numero binario
    que la uso para la formula (11100) => n * 2**position
    Post: Esta función devuelve el numero decimal en formato entero
    """
    if binario == 0:
        return 0
    ultimo_digito = binario % 10
    numero_decimal = ultimo_digito * (2**position)
    return numero_decimal + convertir_bina_deci(binario // 10, position + 1)


def convertir_deci_bina(
    decimal: int,
):  # esta función es para probar el programa no entra en el ejercicio
    """
    Esta función convierte un numero decimal a binario
    Pre: Esta función recibe 1 parametro en formato entero que es el numero decimal
    Post: Esta función devuelve el numero equivalente al decimal pero en formato binario
    """
    if decimal == 0:
        return 0
    elif decimal == 1:
        return 1
    return decimal % 2 + 10 * convertir_deci_bina(decimal // 2)


def menu() -> None:
    """
    Esta es la función principal donde se ejecuta todo el codigo
    Pre: Esta función no recibe ningun parametro
    Post: Esta función no devuelve nada
    """
    while True:
        try:
            binario = int(input("Ingrese un numero binario: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    # numero valido
    print(convertir_bina_deci(binario))


if __name__ == "__main__":
    menu()
