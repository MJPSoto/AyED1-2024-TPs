"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""


def obtener_nombre_mes(numero_mes: int) -> str:
    """
        Está función obtiene el nombre del mes en base a un numero ingresado
        Pre: Está función obtiene un parametro en formato int
        Post: Está función devuelve un str con el nombre del mes si es valido y sino una cadena vacia
    """
    meses = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
    ]
    try:
        return meses[numero_mes - 1] #le puse -1 pq el primero mes es 1, pero para nosotros el primer mes es 0 en esta lista 
    except (IndexError, TypeError):
        return ""


def menu()->None:
    """
        Está es la función principal donde se ejecuta todo el codigo
        Pre: Está función no recibe ningun parametro
        Post: Está función no devuelve nada 
    """
    while True:
        try:
            numero_ingresado = int(input("Ingrese un numero: "))
            break
        except ValueError as e:
            print(f"Error: e")
    #numero ingresado es valido 
    salida = obtener_nombre_mes(numero_ingresado)
    if salida:
        print(f"El nombre del mes es {salida}")
    else:
        print("El numero ingresado no pertenece a ningun mes")

if __name__ == "__main__":
    menu()