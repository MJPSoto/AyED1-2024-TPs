"""
Realizar una función recursiva para imprimir una matriz de M x N con el formato
apropiado.
"""

from random import randint


def imprimir_fila(matriz, fila: int, col: int = 0) -> None:
    """ """
    if col == len(matriz[fila]):
        print()
        return

    print(matriz[fila][col], end=" ")

    imprimir_fila(matriz, fila, col + 1)


def imprimir_matriz(matriz, fila: int = 0) -> None:
    """ """
    if fila == len(matriz):
        return
    imprimir_fila(matriz, fila)
    imprimir_matriz(matriz, fila + 1)


def llenar_matriz(filas: int, colums: int) -> list:
    return [[randint(1, 100) for _ in range(colums)] for _ in range(filas)]


def validar_numeros(numeros) -> bool:
    """
    Está función valida que los numeros de un iterable sean mayores a 0
    la variable numeros no tiene typehint pq es un iterable cualquiera
    pre: Está función recibe como parametro un iterable cualquiera y se fija que los elementos sean numeros mayores a 0
    post: Está función devuelve un booleano dependiendo si el iterable tiene todos los elementos numeros enteros mayores a 0
    """
    for valor in numeros:
        if valor <= 0:
            return False
    return True


def menu() -> None:
    """
    Está es la función principal donde se ejecuta todo el codigo
    Pre: Está función no recibe ningun parametro
    Post: Está función no devuelve nada
    """
    while True:
        try:
            tupla_numeros = input(
                "Ingrese los numeros M x N, M,N separados por coma, ejemplo 1,2: "
            )
            tupla_numeros = tuple(
                map(int, tupla_numeros.split(","))
            )  # esto me devuelve una tupla con n numeros (num1, num2)
            if len(tupla_numeros) != 2:
                raise ValueError("Los valores tiene que ser si o si 2")
            if not validar_numeros(tupla_numeros):
                raise ValueError("Los valores tiene que ser mayores a 0")
            break
        except ValueError as e:
            print(f"Error: {e}")
    # Tupla completa y con los valores verificados
    filas, columnas = tupla_numeros  # desempaqueto la tupla
    imprimir_matriz(llenar_matriz(filas, columnas))


if __name__ == "__main__":
    menu()
