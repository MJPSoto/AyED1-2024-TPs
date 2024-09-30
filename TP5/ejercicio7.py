"""
Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número 
que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más.
"""
#librerias
import random as rn

#funciones
def generar_numero():
    """
    Está es la función genera un numero aleatorio entre 1 y 500
    Pre: Está función no recibe ningun parametro
    Post: Está función devuelve un numero seudo-aleatorio entre 1 y 500
    """
    return rn.randint(1, 500)


def es_mayor(num_ingresado: int, num_aleatorio: int) -> bool:
    """
    Está es la función verifica si el numero ingresado es mayor al numero generado aleatoriamente
    Pre: Está función recibe 2 parametros en formato entero, uno que es el numero ingresado y el otro que el numero aleatorio
    Post: Está función devuelve True si el numero ingresado es mayor al numero aleatorio, en caso contrario devuelve False
    """
    return num_ingresado > num_aleatorio


def menu() -> None:
    """
    Está es la función principal donde se ejecuta todo el codigo
    Pre: Está función no recibe ningun parametro
    Post: Está función no devuelve nada
    """
    numero_random = generar_numero()
    numero_intentos = 0
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            mayor = es_mayor(num, numero_random)
            if num == numero_random or numero_intentos == 3:
                break
            if mayor:
                print(f"El numero ingresado es mayor al numero aleatorio")
            else:
                print(f"El numero ingresado es menor al numero aleatorio")
        except ValueError as e:
            print(f"Error: {e}")
        numero_intentos += 1
    if numero_intentos == 5:
        print("Perdiste maestro, cambiate a la carrera de cocina")
    else:
        print("Adivinaste el numero!!")
    return None

#codigo principal
if __name__ == "__main__":
    menu()
