"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. 
Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""


def eliminar_subcadena_con_rebanadas(cadena: str, position: int, cantidad: int) -> str:
    return cadena[:position] + cadena[position + cantidad :]  # mondongo? check


def eliminar_subcadena_sin_rebanadas(cadena: str, position: int, cantidad: int) -> str:
    lista_letras = list(
        cadena[i]
        for i in range(len(cadena))
        if i < position or i >= position + cantidad
    )  # mas o menos misma logica que el anterior
    return "".join(lista_letras)


def verificar_fn():
    assert (
        eliminar_subcadena_con_rebanadas("Este es un ejemplo de cadena mondongo", 8, 6)
        == "Este es mplo de cadena mondongo"
    )
    assert (
        eliminar_subcadena_sin_rebanadas("Este es un ejemplo de cadena mondongo", 8, 6)
        == "Este es mplo de cadena mondongo"
    )
    return None


def menu() -> None:
    while True:
        try:
            cadena = input("Ingrese la cadena: ")
            position = int(input("Ingrese la posición inicial: "))
            cant_caract = int(input("Ingrese la cantidad de caracteres: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    verificar_fn()
    print(f"Sin rebanadas: {eliminar_subcadena_con_rebanadas(cadena, position, cant_caract)}")
    print(f"Con rebanadas: {eliminar_subcadena_sin_rebanadas(cadena, position, cant_caract)}")
    return None


if __name__ == "__main__":
    menu()
