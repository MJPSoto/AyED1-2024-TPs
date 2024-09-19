"""
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
"""


# funciones
def numero_impares():
    return list(filter(lambda x: x % 2 != 0, range(100, 201)))


def menu():
    # hacer menu
    print(numero_impares())
    return None


# codigo principal
if __name__ == "__main__":
    menu()
