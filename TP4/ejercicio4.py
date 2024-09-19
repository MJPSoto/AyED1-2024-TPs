def convertir_num_a_romano(numero: int) -> str:
    """
    Está función conviete un numero cualquiera a numero romano
    pre: Está función necesita como parametro un numero en formato entero
    post: Está función devuelve una cadena equivalente al numero romano
    """
    cadena_romana = ""
    for valor, simbolo in dict_romanos.items():
        while numero >= valor:
            cadena_romana += simbolo
            numero -= valor
    return cadena_romana


def menu() -> None:
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
    1: "I",
}

if __name__ == "__main__":
    menu()
