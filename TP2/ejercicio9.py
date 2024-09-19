"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. Generar e imprimir 
una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
"""


def lista_multiplos(A: int, B: int) -> list:
    return list(
        filter(lambda x: x % 7 == 0 and x % 5 != 0, range(A, B + 1))
    )  # opción 1, acá uso el filter para filtrar los valores que cumplen la condición


"""
def lista_multiplos(A: int, B: int) -> list:
    return list(i for i in range(A, B+1) if i % 7 == 0 and i % 5 != 0) #opción 2, acá uso listas por comprensión clasica 
"""


def menu():
    # hacer menu
    print(lista_multiplos(100, 200))
    return None


# codigo principal
if __name__ == "__main__":
    menu()
