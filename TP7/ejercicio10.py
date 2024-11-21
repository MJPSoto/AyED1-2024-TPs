"""
Escribir una función que sume todos los elementos de una matriz de M x N y 
devuelva el resultado. No usar la función sum().
"""

from random import randint
from tabulate import tabulate


def sumar_valores_matriz(matriz, fila: int = 0, col: int = 0) -> int:
    """
    Está función suma todos los valores de una matriz M x N
    pre: Está función recibe 3 parametros, 1 de ellos que es la matriz es obligatorio y los 2
    restantes tienen valor por defecto en 0 y no hace falta mandarlo, estos 2 tienen que ser formato entero mayor a 0
    post: Está función devuelve la suma de todos los valores de la matriz
    """
    if fila == len(matriz):
        return 0

    if col == len(matriz[fila]):
        return sumar_valores_matriz(matriz, fila + 1, 0)

    return matriz[fila][col] + sumar_valores_matriz(matriz, fila, col + 1)


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
    suma_matriz = sumar_valores_matriz(matriz)
    print(f"La suma de todos los valores de la matriz es: {suma_matriz}")


if __name__ == "__main__":
    menu()
