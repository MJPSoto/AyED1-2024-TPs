"""
Realizar una función que reciba como parámetros dos cadenas de caracteres 
conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""

def sumar_numeros(primer_cadena: str, segunda_cadena: str)->int:
    """
        Está función recibe 2 cadenas que representan 2 numeros reales y devuelve la suma de los mismos
        Pre: Está función recibe 2 parametros en formato str 
        Post: Está función devuelve un numero entero que es la suma de los 2 parametros
    """
    try:
        numero1 = float(primer_cadena) #supongo que es utilizando float pq puede ingresar numeros con coma (2.75)
        numero2 = float(segunda_cadena) #supongo que es utilizando float pq puede ingresar numeros con coma (2.75)
        return numero1 + numero2 
    except ValueError as e:
        print(f"Error: {e}")
        return -1

def menu()->None:
    """
        Está es la función principal donde se ejecuta todo el codigo
        Pre: Está función no recibe ningun parametro
        Post: Está función no devuelve nada 
    """
    primera_cadena = input("Ingrese el primero numero: ")
    segunda_cadena = input("Ingrese el segundo numero: ")
    salida = sumar_numeros(primera_cadena, segunda_cadena)
    if salida != -1:
        print(f"La suma de los 2 numeros ingresados es {salida}")
    return None

if __name__ == "__main__":
    menu()