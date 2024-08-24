"""
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho medio de 
transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba 
como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. Realizar también un programa 
para verificar el comportamiento de la función.
"""


# funciones
def calcular_monto_total(cantidad_viajes: int, pasaje: int) -> int:
    """
    Esta función calcula el monto del viaje
    pre: Esta función obtine como parametro 2 numeros enteros moyores a 0
    post: Esta función devuelve el monto total del pasaje en entero
    """
    match (cantidad_viajes):
        case cantidad_viajes if cantidad_viajes <= 20:
            return pasaje
        case cantidad_viajes if cantidad_viajes <= 30:
            return pasaje - (pasaje * 0.2)
        case cantidad_viajes if cantidad_viajes <= 40:
            return pasaje - (pasaje * 0.3)
        case cantidad_viajes if cantidad_viajes >= 41:
            return pasaje - (pasaje * 0.4)


def menu() -> None:
    """
    Esta función es el main, valida que el usuario ingrese 3 numeros correspondiente cada uno a (dia, mes, año)
    y despues muestra si la fecha ingresada es valida
    """
    while True:
        try:
            tupla_numeros = input(
                "Ingrese la cantidad de viajes realizados y el valor del pasaje (12, 444): "
            )
            tupla_numeros = tuple(map(int, tupla_numeros.split(",")))
            if len(tupla_numeros) != 2:
                raise ValueError("Verifique los datos ingresados!")
            for valor in tupla_numeros:
                if valor <= 0:
                    raise ValueError("Verifique los datos ingresados!")
            break
        except ValueError as e:
            print(f"Error: {e}")
    # validacion correcta
    cantidad_viajes, valor_boleto = tupla_numeros
    monto_total = calcular_monto_total(cantidad_viajes, valor_boleto)
    print(f"El valor a abonar es de {monto_total}")
    test_validacion()
    return None


def test_validacion() -> None:
    """
    Esta función es para validar el funcionamiento del programa
    """
    assert (calcular_monto_total(1, 500)) == 500
    assert (calcular_monto_total(21, 500)) == 400.0
    assert (calcular_monto_total(31, 500)) == 350.0
    assert (calcular_monto_total(41, 500)) == 300.0
    return None


# codigo principal
if __name__ == "__main__":
    menu()
