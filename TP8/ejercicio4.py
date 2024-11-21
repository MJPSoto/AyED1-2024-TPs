"""
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""

# librerias


# funciones
def fichas_encajan(ficha1: tuple, ficha2: tuple) -> bool:
    """
        Verifica si dos fichas de dominó encajan.
        Las fichas encajan si tienen al menos un número en común.
        pre: recibe 2 tuplas con el formato (num1, num2)
        post: devuelve un booleano
    """
    return not set(ficha1).isdisjoint(
        set(ficha2)
    )  # lo combierto a set para verificar la intersección


def validar_valor(mensaje: str) -> str:
    valor = input(mensaje)
    try:
        valor = tuple(valor.split(","))
        if len(valor) != 2:
            raise ValueError(
                "Datos inválidos. Deben ser dos valores separados por comas."
            )
        valor = tuple(map(int, valor))
        return valor
    except ValueError as e:
        return validar_valor(mensaje)


# Programa principal
def main() -> None:
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    primer_ficha = validar_valor("Ingrese los valores de la primer ficha (num1, num2): ")
    segunda_ficha = validar_valor(
        "Ingrese los valores de la segunda ficha (num1, num2): "
    )

    prueba_funtion()
    encajan = fichas_encajan(primer_ficha, segunda_ficha)
    if encajan:
        print(f"Las fichas ingresan encajan")
    else:
        print(f"Las fichas ingresan no encajan")


def prueba_funtion() -> None:
    """
        Valida el funcionamiento de la funcion fichas_encajan
        pre: No recibe nada
        post: No devuelve nada
    """
    assert (fichas_encajan((3, 4), (5, 4))) == True
    assert (fichas_encajan((2, 6), (4, 5))) == False
    assert (fichas_encajan((1, 1), (1, 6))) == True
    assert (fichas_encajan((0, 3), (3, 0))) == True


# Código principal
if __name__ == "__main__":
    main()
