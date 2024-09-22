"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla.
"""
import random as rn

def generar_matriz_aleatoria(N)->None:
    numeros = list(range(N ** 2))
    rn.shuffle(numeros)
    return [[numeros.pop() for j in range(N)] for i in range(N)]

def imprimir_matriz(matriz)->None:
    for fila in matriz:
        print(fila)

def menu() -> None:
    while True:
        try:
            numero = int(input("Ingrese la cantidad de filas: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    matriz = generar_matriz_aleatoria(numero)
    imprimir_matriz(matriz)
    return None


if __name__ == "__main__":
    menu()