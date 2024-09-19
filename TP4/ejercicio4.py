"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
"""

def convertir_num_a_romano(numero: int) -> str:
    cadena_romana = ""
    for valor, simbolo in dict_romanos.items():
        while numero >= valor: #es mas o menos similar al de los billetes pero con diccionarios, mondongo ? :)
            cadena_romana += simbolo
            numero -= valor
    return cadena_romana

def menu()->None:
    while True:
        try:
            numero = int(input("Ingrese la clave maestra: "))
            if numero < 0 or numero > 3999:
                raise ValueError("El numero tiene que estar entre 0 y 3999")
            break
        except ValueError as e:
            print(f"Error: {e}")
    romano = convertir_num_a_romano(numero)
    print(f"El numero {numero} en romano es {romano}")
    return None

dict_romanos = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

if __name__ == "__main__":
    menu()