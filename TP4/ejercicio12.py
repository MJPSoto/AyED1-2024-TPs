"""
Escribir un programa para crear una lista por comprensión con los naipes de la ba-
raja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros",
"2 Oros"... ]. Imprimir la lista por pantalla.
"""


def crear_lista_naipes():
    """
    Está función crea una lista con los valores de la baraja española
    
    pre: Está función no necesita ningun parametro
    
    post: Está función devuelve una lista de str con el formato "numero palo"
    """
    tupla_palos = ("Oros", "Bastos", "Espadas", "Copas")
    lista_valores = tuple([str(x), j] for j in tupla_palos for x in range(1, 13))
    return [" ".join(valores) for valores in lista_valores]


def menu() -> None:
    print(crear_lista_naipes())
    return None


if __name__ == "__main__":
    menu()
