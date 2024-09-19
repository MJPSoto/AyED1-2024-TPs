"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma. 
Ejemplo, dada la cadena "El número de teléfono es 4356-7890" 
extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""


def cortar_palabra_con_rebanadas(position: int, cant_caract: int, cadena: str) -> str:
    """
    Está función extrae una subcadena de una cadena N

    pre: Está función necesita como parametro una posición de la cadena en formato entero, una cantidad de
    caracteres n en formato entero y una cadena en fomato str

    post: Está función devuelve una subcadena de la cadena original con la condición que empiece desde la posición
    ingesada y la cantidad de caracteres ingresada
    """
    if len(cadena[position::]) >= cant_caract:
        return cadena[position : (position + cant_caract)]
    return ""


def cortar_palabra_sin_rebanadas(position: int, cant_caract: int, cadena: str) -> str:
    """
    Está función extrae una subcadena de una cadena N

    pre: Está función necesita como parametro una posición de la cadena en formato entero, una cantidad de
    caracteres n en formato entero y una cadena en fomato str

    post: Está función devuelve una subcadena de la cadena original con la condición que empiece desde la posición
    ingesada y la cantidad de caracteres ingresada
    """
    return "".join(
        list(
            cadena[i]
            for i in range(position, len(cadena))
            if i < position + cant_caract
        )
    )


def verificar_fn():
    """
    Está función valida el funcionamiento de la funcion 'cortar_palabra_con_rebanadas, cortar_palabra_sin_rebanadas'

    pre: Está función no recibe ningun parametro

    post: Está función no devuelve nada
    """
    assert (
        cortar_palabra_con_rebanadas(25, 9, "El número de teléfono es 4356-7890")
        == "4356-7890"
    )
    assert (
        cortar_palabra_sin_rebanadas(25, 9, "El número de teléfono es 4356-7890")
        == "4356-7890"
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
    print(
        f"Sin rebanadas: {cortar_palabra_sin_rebanadas(position, cant_caract, cadena)}"
    )
    print(
        f"Con rebanadas: {cortar_palabra_con_rebanadas(position, cant_caract, cadena)}"
    )
    return None


if __name__ == "__main__":
    menu()
