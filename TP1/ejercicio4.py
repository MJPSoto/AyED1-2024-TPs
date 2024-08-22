"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""

tupla_billetos_disponibles = (5000, 1000, 500, 200, 100, 50, 10)


def calcular_vuelto(monto_compra: int, monto_recibido: int) -> dict:
    """
    Esta función recibe el monto de la compra y el monto abonado y devuelve la cantidad de billetes del vuelto
    pre: Esta función recibe como parametros 2 numeros enteros
    post: Esta función devuelve un diccionario con la cantidad de billetes de vuelto {billete: cantidad}
    """
    vuelto = monto_recibido - monto_compra
    if vuelto <= 0:
        return {}
    dict_vuelto = {}
    if vuelto > 0:
        for valor in tupla_billetos_disponibles:
            cantidad = 0 #reseteo la cantidad de billetes por cada iteración
            while vuelto >= valor: #mientras que mi vuelto sea mayor al valor sigue iterando
                cantidad += 1
                vuelto -= valor
            if cantidad > 0:#si entro por lo menos una vez al while lo suma al dict
                dict_vuelto[valor] = cantidad
        return dict_vuelto
    else:
        return {}


def menu() -> None:
    """
    Esta función es el main, valida que el usuario ingrese 2 numeros correspondiente cada uno a (total compra y dinero recibido)
    y muestra la cantidad de billetes que tiene que devolver
    """
    while True:
        try:
            tupla_numeros = input(
                "Ingrese el total de la compra y el dinero recibido (250, 300): "
            )
            tupla_numeros = tuple(map(int, tupla_numeros.split(",")))
            if len(tupla_numeros) != 2 or tupla_numeros[0] < 0 or tupla_numeros[1] < 0:
                raise ValueError("Verifique los datos ingresados!")
            break
        except ValueError as e:
            print(f"Error: {e}")
    # validacion correcta
    monto_compra, monto_recibido = tupla_numeros  # desempaqueto la tupla
    dict_vuelto = calcular_vuelto(monto_compra, monto_recibido) #invoco a la función
    if dict_vuelto: #compruebo de que el dict no este vacio 
        print("\nCantidad de billetes de vuelto: ")
        for valor in dict_vuelto: #recorro el dict para mostrar los valores del mismo
            print(f"Billete ${valor}. {dict_vuelto.get(valor)}")
        print("")
    else:
        print("El vuelto es justo o no alcanza para la compra")
    test_validacion() # hago un test de la funcion
    return None


def test_validacion() -> None:
    """
    Esta función es para validar el funcionamiento del programa
    """
    assert(calcular_vuelto(3170,5000)) == {1000: 1, 500: 1, 200: 1,100:1, 10:3}
    assert(calcular_vuelto(200,200)) == {}
    assert(calcular_vuelto(3170,2000)) == {}
    assert(calcular_vuelto(5000,7000)) == {1000: 2}
    assert(calcular_vuelto(150,300)) == {100: 1, 50: 1}
    return None


if __name__ == "__main__":
    menu()
