"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento, 
imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
"""


def cargar_numeros(N: int):
    return [
        [
            int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            for j in range(N)
        ]
        for i in range(N)
    ]


print(cargar_numeros(3))


def ordenar_filas_matriz(matriz: list) -> list:
    for fila in matriz:
        fila.sort()
    return matriz


def validar_rango(fila1: int, fila2: int, matriz: list) ->bool:
    return fila1 < 0 or fila2 < 0 or fila1 >= len(matriz) or fila2 >= len(matriz)


def intercambiar_filas(matriz: list, fila1: int, fila2: int) -> None:
    if validar_rango(fila1, fila2, matriz):
        print("Error: uno o ambos índices de fila están fuera de rango.")
        return
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]


def intercambiar_columnas(matriz: list, col1: int, col2: int) -> None:
    if validar_rango():
        print("Error: uno o ambos índices de columna están fuera de rango.")
        return

    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]


def transponer_matriz(matriz: list) -> None:
    N = len(matriz)
    for i in range(N):
        for j in range(i + 1, N):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]


def validar_matriz(campo1: int, matriz: list) ->bool:
    return campo1 < 0 or campo1 >= len(matriz[0])


def promedio_fila(matriz: list, fila_numero: int) -> float:
    if validar_matriz(fila_numero, matriz):
        print("Error: el índice de fila está fuera de rango.")
        return None
    if fila_numero:
        promedio = sum(matriz[fila_numero]) / len(matriz[fila_numero])
    return promedio


def porcentaje_impares_columna(matriz: list, col_numero: int) -> float:
    if validar_matriz(col_numero, matriz):
        print("Error: el índice de columna está fuera de rango.")
        return None

    total_elementos = 0
    impares = 0
    for fila in matriz:
        if col_numero < len(fila):
            valor = fila[col_numero]
            total_elementos += 1
            if valor % 2 != 0:
                impares += 1
    if total_elementos:
        porcentaje = impares / total_elementos * 100
    return porcentaje


def es_simetrica(matriz: list) -> bool:
    N = len(matriz)
    for i in range(N):
        for j in range(N):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def es_simetrica_diagonal_secundaria(matriz: list) -> bool:
    N = len(matriz)
    for i in range(N):
        for j in range(N):
            if matriz[i][j] != matriz[N-1-j][N-1-i]:
                return False
    return True

def es_palindromo(columna: list) -> bool:
    return columna == columna[::-1]

def columnas_palindromas(matriz: list) -> list:
    return [col for col in range(len(matriz)) if es_palindromo([matriz[row][col] for row in range(len(matriz))])] #ejercicio feo, mondongo 