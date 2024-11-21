"""
Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo 
Común Divisor (también llamado Divisor Común Mayor) basándose en las siguientes propiedades:
MCD(X, X) = X
MCD(X, Y) = MCD(Y, X)
Si X > Y => MCD(X, Y) = MCD(X–Y, Y).
Utilizando la función anterior calcular el MCD de todos los elementos de una lista de
números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite
utilizar iteraciones en ninguna etapa del proceso.
"""


def max_com_denominador(a: int, b: int) -> int:
    """
    Esta función obtiene el maximo comun denominador de 2 numeros cualquiera mayores a 0
    Pre: Esta función recibe como parametro 2 numeros enteros mayores a 0
    Post: Esta función devuelve el mcd de los 2 numeros pasados como parametro
    """
    if a == b:
        return a
    elif a > b:
        return max_com_denominador(a - b, b)
    else:
        return max_com_denominador(b, a)


def max_com_denominador_lista(nums: list) -> int:
    """
    Esta función obtiene el maximo comun denominador de una lista de numeros
    Pre: Esta función recibe como parametro una lista de numeros enteros mayores a 0
    Post: Esta función devuelve el mcd de la lista pasada como parametro
    """
    if len(nums) == 1:
        return nums[0]
    else:
        return max_com_denominador(nums[0], max_com_denominador_lista(nums[1:]))


def validar_numeros(numeros) -> bool:
    """
    Esta función valida que los numeros de un iterable sean mayores a 0
    la variable numeros no tiene typehint pq es un iterable cualquiera
    pre: Esta función recibe como parametro un iterable cualquiera y se fija que los elementos sean numeros mayores a 0
    post: Esta función devuelve un booleano dependiendo si el iterable tiene todos los elementos numeros enteros mayores a 0
    """
    for valor in numeros:
        if valor <= 0:
            return False
    return True


def menu() -> None:
    """
    Esta es la función principal donde se ejecuta todo el codigo
    Pre: Esta función no recibe ningun parametro
    Post: Esta función no devuelve nada
    """
    while True:
        try:
            tupla_numeros = input(
                "Ingrese los 2 numeros separados por coma, ejemplo 3,3: "
            )
            tupla_numeros = tuple(
                map(int, tupla_numeros.split(","))
            )  # esto me devuelve una tupla de los 2 numeros (num1, num2)
            if len(tupla_numeros) != 2:
                raise ValueError("Debe ingresar exactamente dos valores")
            if not validar_numeros(tupla_numeros):
                raise ValueError("Los numeros tienen que ser positivos")
            break
        except ValueError as e:
            print(f"Error: {e}")
    # numeros verificados
    num1, num2 = tupla_numeros  # desempaqueto los numeros
    mcd = max_com_denominador(num1, num2)
    print(f"El maximo comun denominador es: {mcd}")
    while True:
        try:
            lista_numeros = input(
                "Ingrese los numeros separados por coma, ejemplo 3,3,3....n: "
            )  # esto me devuelve una lista con n numeros [num1, num2,.....numN]
            lista_numeros = list(map(int, lista_numeros.split(",")))
            if not validar_numeros(lista_numeros):
                raise ValueError("Los numeros tienen que ser positivos")
            break
        except ValueError as e:
            print(f"Error: {e}")
    # lista completa y con los valores verificados
    mcd_lista = max_com_denominador_lista(lista_numeros)
    print(f"El maximo comun denominador de la lista es: {mcd_lista}")


if __name__ == "__main__":
    menu()
