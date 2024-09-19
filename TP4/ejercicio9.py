"""
Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final.
"""


def cortar_ordenar_cadena(cadena: str) -> str:
    """
    Está funcion separa una cadena n por espacios y devuelve una nueva cadena ordenada por logitud de la palabra

    pre: Está función necesita como parameto una cadena en formato str

    post: Está función devuelve una nueva cadena con las palabras ordenadas por longitud
    """
    lista_ordenada = sorted(
        cadena.split(), key=lambda palabra: len(palabra)
    )  # Esto ordena de menor a mayor longitud
    # lista_ordenada = sorted(cadena.split(), key = lambda palabra: len(palabra), reverse=True) Esto podria ser que se ordene de mayor a menor longitud
    return " ".join(lista_ordenada)


def menu() -> None:
    cadena = input("Ingrese la cadena: ")
    print(f"La cadena ordenada por longitud es")
    print(cortar_ordenar_cadena(cadena))
    return None


if __name__ == "__main__":
    menu()
