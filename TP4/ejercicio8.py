"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""


def cortar_ultimos_caracteres(cadena: str, numero: int) -> str:
    return cadena[numero::] #mondongo ?


def menu() -> None:
    while True:
        try:
            cadena = input("Ingrese la cadena: ")
            numero = int(input("Ingrese la posición inicial: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    ultimos_caract = cortar_ultimos_caracteres(cadena, numero)
    print(f"Los ultimos caracteres de la cadena {cadena} son: {ultimos_caract}")
    return None


if __name__ == "__main__":
    menu()