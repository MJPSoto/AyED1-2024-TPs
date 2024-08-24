"""
Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.
b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. No se permite utilizar ayudas externas a las mismas.
"""


# funciones
def es_oblongo(num: int) -> bool:
    """
    Esta función obtiene un numero entero y valida si es oblongo
    pre: esta función obtiene como parametro un numero entero mayor a 0
    post esta función devuelve True si el numero es oblongo y false si no lo es
    """
    tupla_valores = tuple(range(1, int(num**0.5) + 1))
    # función sin lambda
    """
    for valor in tupla_valores:
        if valor * (valor +1) == num:
            return True
    return False
    """
    es_oblongo_anonima = lambda num, tupla_valores: any(
        valor * (valor + 1) == num for valor in tupla_valores
    )
    return es_oblongo_anonima(num, tupla_valores)


def es_triangular(num: int) -> bool:
    """
    Esta función obtiene un numero entero y valida si es triangular
    pre: Esta función obtiene como parametro un numero entero mayor a 0
    post: Esta función devuelve True si el numero es triangular y false si no lo es
    """
    tupla_valores = tuple(range(1, int((2 * num) ** 0.5) + 1))
    """
    k(k +1) / 2 = num 
    si multiplicamos de ambos lados por 2 
    k(k + 1) = 2 * num
    aplicamos distributiva
    k**2 + k = 2 * num 
    igualamos a 0
    k**2 + k -2 * num = 0
    aplicamos cuadratica
    a, b, c = k**2, k, -2*num 
    k = (-1+-(1 + 8 * num)**.5)/ 2 
    (1 + 8 * num) ≈ (8 * num)**.5 por simplificacion estimada
    podemos separar la raiz 
    (8 * num)**.5 = (8)**.5 * (num)**.5 
    (8 * num)**.5 = 2(2)**.5 * (num)**.5
    k ≈ (-1+2(2)**.5 * (num)**.5/ 2  
    por simplificacion estimada 
    k ≈ (2(num)**.5)/2
    ajustamos para obtener todos los valores, por la corrección de sesgo
    k ≈ (2 * num)**.5 + 1
    """
    es_triangular_aninoma = lambda num, tupla_valores: any(
        (valor * (valor + 1)) // 2 == num for valor in tupla_valores
    )
    return es_triangular_aninoma(num, tupla_valores)


def mostrar_menu():
    for key, valor in dict_opciones_disponibles.items():
        print(f"{key}. {valor}")
    return None


def validar_num(num):
    return isinstance(num, int)


def input_numero(nombre):
    while True:
        try:
            num = int(input(f"Ingrese el numero para ver si es {nombre}: "))
            if validar_num(num) and num > 0:
                break
            raise ValueError("Verifique el valor ingresado!")
        except ValueError as e:
            print(f"Error: {e}")
    return num


def menu():
    mostrar_menu()
    while True:
        try:
            opcion = int(input("Seleccione una de las siguiente opciones: "))
            if opcion in dict_opciones_disponibles:
                break
            raise ValueError("Verifique el valor ingresado!")
        except ValueError as e:
            print(f"Error: {e}")
    match (opcion):
        case 1:
            num = input_numero("Oblongo")
            print(es_oblongo(num))
        case 2:
            num = input_numero("Triangular")
            print(es_triangular(num))
        case -1:
            print("Adios...")
    return None


# variables globales
dict_opciones_disponibles = {
    1: "Saber si un numero es oblongo",
    2: "Saber si un numero es triangular",
    -1: "Salir",
}

# codigo principal
if __name__ == "__main__":
    menu()
