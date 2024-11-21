"""
Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado.
"""

# Librerías
from tabulate import tabulate

# Funciones
def tabla_n(numero: int) -> dict:
    """
        Genera un diccionario con las claves desde 1 al 12 y los valores con la tabla de multiplicar de el numero ingresado 
        Pre: Recibe como parametro un numero entero 
        post: Devuelve un diccionario con el formato {int: int}
    """
    return {i: numero * i for i in range(1, 13)}

def validar_valor(mensaje: str) -> int:
    """
        Valida el formato de valor ingresado por el usuario 
        pre: Recibe como parametro un mensaje en formato str 
        post: Devuelve una tupla con el formato correcto 
    """
    try:
        valor = int(input(mensaje))
        return valor
    except ValueError as e:
        print("Por favor, ingrese un número válido.")
        return validar_valor(mensaje)

def main() -> None:
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    numero = validar_valor("Ingrese el numero: ")
    dict_multi = tabla_n(numero)
    
    tabla = [(clave, valor) for clave, valor in dict_multi.items()]
    
    print(tabulate(tabla, headers=["Número", "Multiplicación"]))

# Código principal
if __name__ == "__main__":
    main()
