"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla. 
"""


# funciones
def obtener_impares() -> list:
    return list(filter(lambda x: x % 2 != 0, list(range(1, 101))))


def menu():
    # hacer menu
    print(obtener_impares())
    return None


# codigo principal
if __name__ == "__main__":
    menu()
