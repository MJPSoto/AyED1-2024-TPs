def centrar_cadena(cadena: str, cantidad_columnas: int = 80) -> None:
    """
    Está función muestra en pantalla la frase que ingrese el usuario centrada

    pre: Está función necesita como parametro una cadena en formato str y una cantidad de columnas en fomato int
    que Está si no se ingresa se toma como default 80

    post: devuelve una nueva cadena enformato str centrada en base a la cantidad de columnas que se tomo como parametro

    """
    cantidad_caracteres = len(cadena)
    if cantidad_caracteres > cantidad_columnas:
        # Si la cadena es más larga que la cantidad de columnas, se corta
        cadena = cadena[:cantidad_columnas]
        cantidad_caracteres = len(cadena)
    espacios = (cantidad_columnas - cantidad_caracteres) // 2
    return " " * espacios + cadena


def menu() -> None:
    cadena = input("Introduce una cadena: ")
    print(centrar_cadena(cadena))
    return None


if __name__ == "__main__":
    menu()
