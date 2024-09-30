"""
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""


def imprimir_numeros(ultimo_numero: int = 1) -> None:
    """
        Está función muestra los numeros del 1 al 100000 y cuandos se interrumpe el proceso pregunta si quiere 
        empezar terminar el programa, en caso de no terminarlo comienza desde donde se quedo por ultima vez 
        Pre: Está función recibe como parametro un numero en formato entero con un valor default de 1 
        Post: Está función no devuelve nada
    """
    confirmation = "h"
    try:
        for i in range(ultimo_numero, 100001):
            print(i)
    except KeyboardInterrupt:
        while confirmation not in ("s", "n"):
            confirmation = input("Está seguro que quiere terminar el programa (s/n): ").lower()
        if confirmation == "n":
            imprimir_numeros(i) 

def menu()->None:
    """
        Está es la función principal donde se ejecuta todo el codigo
        Pre: Está función no recibe ningun parametro
        Post: Está función no devuelve nada 
    """
    imprimir_numeros()

if __name__ == "__main__":
    menu()