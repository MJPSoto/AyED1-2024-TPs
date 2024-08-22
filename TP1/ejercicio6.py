"""
Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.
"""


def concatenar_numeros(num1: int, num2: int) -> str:
    return f"{num1}{num2}"  # mondongo


def menu() -> None:
    while True:
        try:
            tupla_numeros = input("Ingrese 2 numeros para concatenar (1234, 567): ")
            tupla_numeros = tuple(
                map(int, tupla_numeros.split(","))
            )  # Spliteo por la coma y despues esos valores los casteo a int con el map, función de orden superior
            if len(tupla_numeros) != 2:
                raise ValueError("Verifique los datos ingresados!")
            break
        except ValueError as e:
            print(f"Error: {e}")
    # validacion correcta
    num1, num2 = tupla_numeros
    nums_concat = concatenar_numeros(num1, num2)
    print(f"La concatenación de los numeros {num1} y {num2} es {nums_concat}")
    test_validacion()
    return None

def test_validacion() -> None:
    """
    Esta función es para validar el funcionamiento del programa
    """
    assert(concatenar_numeros(1234,567)) == "1234567"
    assert(concatenar_numeros(12,3)) == "123"
    assert(concatenar_numeros(33,12)) != "12"
    assert(concatenar_numeros(3,456987)) == "3456987"
    return None

if __name__ == "__main__":
    menu()
