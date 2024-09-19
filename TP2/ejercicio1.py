"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la 
lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""

# librerias
import random as rn
from functools import reduce

rn.seed(1)


# funciones
def cargar_numeros_aleatorios() -> list:
    return list(rn.randint(1000, 9999) for _ in range(rn.randint(10, 99)))


def calcular_producto() -> int:
    return reduce(lambda x, y: x * y, lista_numeros)


def eliminar_apariciones(num: int, lista: list) -> None:
    if not lista or num not in lista:
        return -1
    lista[:] = [valor for valor in lista if valor != num] #uso el slice


def saber_si_es_capícua() -> bool:
    return lista_numeros == lista_numeros[::-1]


def mostrar_opciones_disponibles(lista) -> None:
    for i, valor in enumerate(lista):
        print(f"{i+1}. {valor}")
    return None


def validar_numero(texto: str, lista: list):
    while True:
        try:
            if lista:
                mostrar_opciones_disponibles(lista)
            opcion = int(input(f"{texto}"))
            break
        except ValueError as e:
            print("Solo se permiten numeros")
    return opcion


def menu():
    opcion = validar_numero(
        "Seleccione una de las siguientes opciones: ", lista_opciones
    )
    # valadación correcta
    match opcion:
        case 1:
            lista_numeros[:] = cargar_numeros_aleatorios()
            print(f"Se genero la lista de numeros")
            print(f"{lista_numeros}")
        case 2:
            producto = calcular_producto()
            print(lista_numeros)
            print(f"El producto de la lista es: {producto}")
        case 3:
            numero = validar_numero("seleccione un numero para eliminar: ", lista_numeros)
            print(f"Lista original: ")
            print(lista_numeros)
            eliminar_apariciones(numero, lista_numeros)
            print(f"Lista despues de la eliminación: ")
            print(lista_numeros)
        case 4:
            if saber_si_es_capícua():
                print("La lista es capicua")
            else:
                print("La lista no es capicua")
        case 5:
            print("Adios!")
        case _:
            print("opción invalida")
    if opcion != 5:
        menu()
    return None


# variables globales
lista_numeros = cargar_numeros_aleatorios()
lista_opciones = [
    "Cargar una lista con números al azar de cuatro dígitos.",
    "Calcular y devolver el producto de todos los elementos de la lista anterior.",
    "Eliminar todas las apariciones de un valor en la lista anterior.",
    "Determinar si el contenido de una lista cualquiera es capicúa",
    "Salir",
]

# codigo principal
if __name__ == "__main__":
    menu()
