# librerias
import random as rn

# funciones


def generar_nums_rn(cantidad: int) -> list:
    return list(rn.randint(1, 100) for i in range(cantidad))


"""
def elementos_repetidos(lista: list)->bool:
    for valor in lista:
        if lista.count(valor) > 1:
            return True
    return False
"""


def elementos_repetidos(lista: list) -> bool:
    return any(
        lista.count(valor) > 1 for valor in lista
    )  # basicamente reduje el codigo de arriba


"""
def armar_lista_elem_unicos(lista_origen: list)->list:
    lista_unicos = []
    for valor in lista_origen:
        if lista_origen.count(valor) == 1:
            lista_unicos.append(valor)
    return lista_unicos
"""


def armar_lista_elem_unicos(lista_origen: list) -> list:
    return list(
        valor for valor in lista_origen if lista_origen.count(valor) == 1
    )  # basicamente reduje el codigo de arriba


def menu():
    # hacer menu
    return None


# codigo principal
if __name__ == "__main__":
    menu()
