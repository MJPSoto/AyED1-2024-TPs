"""
Muchas aplicaciones financieras requieren que los números sean expresados tam-
bién en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento cincuenta y tres". 
Escribir un programa que utilice una función para convertir un
número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría
la función si también aceptara números negativos? ¿Y números con decimales?
"""


def pasar_monto_letras(monto: int) -> str:
    """
    Está función convierte un numero entero a una cadena representando ese numero pero en letras
    
    pre: Está función necesita como parametro un monto en formato entero
    
    post: Está función devuelve una cadena equivalente al numero, pero en letras
    """
    cadena = ""
    monto = abs(monto)
    # Está en desarrollo, no la juzgues mariano que es media timida la función
    while monto != 0:
        longitud = len(str(monto))
        numero_int = int("1" + "0" * (longitud - 1))
        unidad = (monto // numero_int) * numero_int
        if unidad in dict_unidades.keys():
            if unidad <= 9:
                cadena += "y "
            cadena += dict_unidades[unidad] + " "
        else:
            numero = unidad // numero_int
            cadena += dict_unidades[numero] + " " + dict_unidades[numero_int] + " "
        monto -= unidad
    return cadena


dict_unidades = {
    0: "cero",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez",
    11: "once",
    12: "doce",
    13: "trece",
    14: "catorce",
    15: "quince",
    16: "dieciséis",
    17: "diecisiete",
    18: "dieciocho",
    19: "diecinueve",
    20: "veinte",
    30: "treinta",
    40: "cuarenta",
    50: "cincuenta",
    60: "sesenta",
    70: "setenta",
    80: "ochenta",
    90: "noventa",
    100: "ciento",
    200: "doscientos",
    300: "trescientos",
    400: "cuatrocientos",
    500: "quinientos",
    600: "seiscientos",
    700: "setecientos",
    800: "ochocientos",
    900: "novecientos",
    1000: "mil",
    10000: "diez mil",
    100000: "cien mil",
    1000000: "un millón",
    10000000: "diez millones",
    100000000: "cien millones",
    1000000000: "mil millones",
    10000000000: "diez mil millones",
    100000000000: "cien mil millones",
    1000000000000: "un billón",
}


def menu() -> None:
    while True:
        try:
            monto = int(input("Ingrese el monto para pasarlo a letras: "))
            break
        except ValueError as e:
            print("Solo se permiten numeros")
    print(pasar_monto_letras(monto))
    return None


if __name__ == "__main__":
    menu()
