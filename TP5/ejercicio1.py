"""
Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""

def validar_entrada() -> int:
    """
    Esta función verifica que el dato ingresado sea un número natural mayor a cero.
    Pre: No recibe ningún parámetro.
    Post: Devuelve el número validado si es correcto.
    """
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            if numero <= 0:
                raise ValueError("El número debe ser mayor que 0")
            return numero 
        except ValueError as e:
            print(f"Error: {e}.")
    
def validar_funcion()->None:#no se validar una función sin parametros 
    
    return None

def menu()->None:
    """
        Está es la función principal donde se ejecuta todo el codigo
        Pre: Está función no recibe ningun parametro
        Post: Está función no devuelve nada 
    """
    salida = validar_entrada()
    print(f"El numero ingresado es {salida} y cumple con las condiciones")
    return None

if __name__ == "__main__":
    menu()