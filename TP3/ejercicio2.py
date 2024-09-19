"""
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones que generen cada una de ellas 
sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a través del teclado.
"""
from tabulate import tabulate

def generate_matrix_c(N: int):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N - i):
            matrix[i][j] = N - i - j
    return matrix

print(tabulate(generate_matrix_c(4)))