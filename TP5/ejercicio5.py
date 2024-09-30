"""
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""
import math

def calcular_raiz_cuadrada(numero: int)->int:
    """
        Esta función calcula la raíz cuadrada de un número ingresado.
        
        Pre: Se recibe un número entero o flotante como parámetro.
        Post: Devuelve la raíz cuadrada del número si es válido. Si el número es negativo o no es numérico, muestra un mensaje de error.
    """
    try:
        numero = int(numero)
        return math.sqrt(numero)
    except (TypeError,ValueError) as e:
        print(f"Error: {e}")
    return -1

def menu()->None:
    """
        Está es la función principal donde se ejecuta todo el codigo
        Pre: Está función no recibe ningun parametro
        Post: Está función no devuelve nada 
    """
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    raiz = calcular_raiz_cuadrada(numero)
    if raiz != -1:
        print(f"La raiz cuadrada de {numero} es {raiz}")
if __name__ == "__main__":
    menu()
