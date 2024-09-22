"""
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones que generen cada una de ellas 
sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. El tamaño de las matrices debe establecerse como N x N, donde N se ingresa a través del teclado.
"""

from tabulate import tabulate


def matriz_a(N: int) -> list[list[int]]:
    return [[i * 2 + 1 if i == j else 0 for j in range(N)] for i in range(N)]


def matriz_b(N: int) -> list[list[int]]:
    return [[27 // (3**i) if j == 3 - i else 0 for j in range(N)] for i in range(N)]


def matriz_c(N: int) -> list[list[int]]:
    return [[4 - i if j <= i else 0 for j in range(N)] for i in range(N)]


def matriz_d(N: int) -> list[list[int]]:
    return [[2 ** (3 - i) for j in range(N)] for i in range(N)]


def matriz_e(N: int) -> list[list[int]]:
    valor = 0
    return [
        [(valor := valor + 1) if (i + j) % 2 == 1 else 0 for j in range(N)]
        for i in range(N)
    ]


def matriz_i(N: int) -> list[list[int]]:
    matriz = [[0] * N for _ in range(N)]
    valor = 1
    capa = 0
    while valor <= N * N:
        for j in range(capa, N - capa):
            matriz[capa][j] = valor
            valor += 1
        for i in range(capa + 1, N - capa):
            matriz[i][N - capa - 1] = valor
            valor += 1
        for j in range(N - capa - 2, capa - 1, -1):
            matriz[N - capa - 1][j] = valor
            valor += 1
        for i in range(N - capa - 2, capa, -1):
            matriz[i][capa] = valor
            valor += 1
        capa += 1
    return matriz


def mostrar_opciones() -> None:
    for i, valor in enumerate(lista_opciones):
        print(f"{i+1}. {valor}")
    return None

def menu() -> None:
    mostrar_opciones()
    option = input("Seleccione una opción: ")
    try:
        numero_int = int(input("Ingrese la cantidad de NxM tiene que ser un numero solo: "))
    except ValueError as e:
        print(f"{e}")
    match option:
        case "1":
            print(tabulate(matriz_a(numero_int)))
        case "2":
            print(tabulate(matriz_b(numero_int)))
        case "3":
            print(tabulate(matriz_c(numero_int)))
        case "4":
            print(tabulate(matriz_d(numero_int)))
        case "5":
            print(tabulate(matriz_i(numero_int)))
        case _:
            print(f"Opción no valida")

    return None


# variables globales:
lista_opciones = [
    "Ejercicio A",
    "Ejercicio B",
    "Ejercicio C",
    "Ejercicio D",
    "Ejercicio E",
    "Ejercicio I",
]


if __name__ == "__main__":
    menu()
