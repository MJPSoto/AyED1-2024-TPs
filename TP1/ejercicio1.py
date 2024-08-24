"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
"""


# funciones
def obtener_mayor(*args) -> int:
    """
    Esta funcion obtiene el mayor estricto de 3 numeros enteros
    pre: Esta funcion recibe una tupla con 3 valores y estos 3 valores tienen que ser enteros
    post: Esta funcion devulve el mayor estricto de los 3 numeros y si no lo encuentra devuelve -1
    """
    lista_numeros = list(args)
    numero_mayor = max(lista_numeros)
    cantidad = lista_numeros.count(numero_mayor)
    if cantidad > 1:
        return -1
    return numero_mayor


def menu() -> None:
    while True:
        try:
            tupla_numeros = input(
                "Ingrese los 3 numeros separados por coma, ejemplo (3,3,3): "
            )  # esto me devuelve una tupla de los 3 numeros (num1, num2, num3)
            tupla_numeros = tuple(map(int, tupla_numeros.split(",")))
            if len(tupla_numeros) != 3:
                raise ValueError("Debe ingresar exactamente tres valores")
            for valor in tupla_numeros:
                if valor <= 0:
                    raise ValueError("Verifique los datos ingresados!")
            break
        except ValueError as e:
            print(f"Error: {e}. Verifique que el valor ingresado sea correcto!")
    # La validación paso correctamente
    num1, num2, num3 = tupla_numeros  # desempaqueto la tupla
    mayor_estricto = obtener_mayor(
        num1, num2, num3
    )  # invoco la funcion para obtener el mayor estricto
    if mayor_estricto != -1:
        print(f"El mayor estricto de los 3 numeros es {mayor_estricto}")
    else:
        print("No se encontro mayor estricto")
    return None


# codigo principal
if __name__ == "__main__":
    menu()
