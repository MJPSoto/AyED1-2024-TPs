"""
La función de Ackermann A(m,n) se define de la siguiente forma:
n+1 si m = 0
A(m-1,1) si n = 0
A(m-1,A(m,n-1)) de otro modo
Imprimir un cuadro con los valores que adopta la función 
para valores de m entre 0
y 3 y de n entre 0 y 7.
"""

from tabulate import tabulate


def function_ack(num_m: int, num_n: int) -> int:
    """
    Esta función calcula el valor de la función de Ackermann para los enteros num_m y num_n.
    pre: Esta
    """
    if num_m == 0:
        return num_n + 1
    elif num_n == 0:
        return function_ack(num_m - 1, 1)
    return function_ack(num_m - 1, function_ack(num_m, num_n - 1))


def menu() -> None:
    """
    Está es la función principal donde se ejecuta todo el codigo
    Pre: Está función no recibe ningun parametro
    Post: Está función no devuelve nada
    """
    lista_valores = []

    for valor_m in range(4):
        fila = []
        for valor_n in range(8):
            try:
                fila.append(function_ack(valor_m, valor_n))
            except RecursionError:
                fila.append("mucho") # muestro este mensaje para no tener que cambiar el valor pythom
        lista_valores.append(fila)

    print(
        tabulate(lista_valores, headers=[f"{n}" for n in range(8)], showindex="always")
    )


if __name__ == "__main__":
    menu()
