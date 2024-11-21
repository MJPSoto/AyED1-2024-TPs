"""
Desarrollar una función que devuelva el mínimo elemento de una matriz de M x N.
"""

from random import randint
from tabulate import tabulate


def encontrar_minimo(matriz, fila: int = 0, col: int = 0, minimo: int = None) -> int:
    """
    Está función encuenta el elemento con menor valor
    pre: Está función recibe como parametro una matriz (lista de listas) y
    3 valores no obligatorios por que tiene como valor por defecto
    post: Está función devuelve el elemento con menor valor
    """
    if fila == len(matriz):
        return minimo

    if minimo is None:  # esto lo hago para tomar el primer valor de la lista de listas
        minimo = matriz[fila][col]

    if matriz[fila][col] < minimo:
        minimo = matriz[fila][col]

    if col == len(matriz[fila]) - 1:
        return encontrar_minimo(matriz, fila + 1, 0, minimo)

    return encontrar_minimo(matriz, fila, col + 1, minimo)


def llenar_matriz(filas: int, colums: int) -> list:
    """
    Está función genera una matriz de M x N con valores aleatorios
    pre: Está función recibe como parametro la cantidad de filas y la cantidad de columnas en formato entero mayor a 0
    post: Está función devulve la matriz genera de M x N
    """
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
    matriz = llenar_matriz(filas, columnas)
    print(tabulate(matriz))
    numero_minimo = encontrar_minimo(matriz)
    print(f"El numero minimo de la matriz es: {numero_minimo}")


if __name__ == "__main__":
    menu()
