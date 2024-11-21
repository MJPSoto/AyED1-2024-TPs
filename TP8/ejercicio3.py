"""
Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""
import re 

def desarmar_mail(mail: str) -> tuple:
    """
        Descompone una dirección de correo electrónico en sus partes:
        nombre, dominio y subdominios.
        pre: recibe un mail en formato str
        post: devuelve una tupla con las partes del mail
    """
    nombre, dominio = mail.split("@")
    partes_dominio = dominio.split(".")
    return (nombre, *partes_dominio)

def validar_mail(mensaje: str) -> str:
    """
        Solicita al usuario una dirección de correo electrónico válida.
        Valida el formato del correo usando una expresión regular.
        pre: recibe un mail en formato str
        post: devuleve el mismo mail pero valido en formato str
    """
    patron = r"^([\w\.-]+)@([\w-]+)\.([\w-]+)(?:\.([\w-]+))?$"
    mail = input(mensaje)
    try:
        if re.match(patron, mail):
            return mail
    except ValueError as e:
        print("El correo ingresado no es válido. Intente nuevamente.")
        return validar_mail(mensaje)

def main():
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    mail = validar_mail("Ingrese el correo electrónico: ")
    partes = desarmar_mail(mail)
    print(f"Partes del correo: {partes}")

# Código principal
if __name__ == "__main__":
    main()

