"""
Se solicita crear un programa para leer direcciones de correo electrónico y verificar
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que una
dirección sea considerada válida el nombre de usuario debe poseer solamente caracteres
alfanuméricos, la dirección contener un solo carácter @, el dominio debe tener al menos un
carácter y tiene que finalizar con .com.ar.
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mostrar
un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente, recordando
que las direcciones de mail no son case sensitive.
"""
import re

def verificar_correo(correo: str)->bool:
    """
    Está función verifica si un correo es valido o no 
    pre: Está función necesita como parametro un cadena que vendria a ser el correo en formato str 
    post: Está función devuelve un bool donde True es que el correo es valido y si no devuelve False
    """
    patron = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}+"
    return re.match(patron, correo)

def menu() -> None:
    conjunto_dominions = set()# se puede usar conjuntos, estos no permiten valores duplicados
    while True:
        correo = input("Ingrese un correo para validar (o -1 para salir): ")
        if correo == "-1":
            break
        if verificar_correo(correo):
            print("El correo ingresado es válido.")
            dominio = correo.split('@')[1]
            conjunto_dominions.add(dominio) 
        else:
            print("El correo ingresado no es válido.")
    for dominio in sorted(conjunto_dominions):
        print(dominio)

if __name__ == "__main__":
    menu()