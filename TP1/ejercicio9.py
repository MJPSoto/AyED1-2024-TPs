"""
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, 
considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo. 
"""

# librerias
import random as rn

rn.seed(1)


# funciones
def calcular_rn_peso(cantidad_naranjas: int) -> tuple:
    """
    Esta función genera aleatoriamente pesos para N cantidad de naranjas
    pre: Esta función obtiene como parametro un entero positivo
    post: Esta función devuelve una tupla con N elemetros que son los pesos de cada naranja
    """
    tupla_pesos = tuple(
        rn.randint(150, 350) for _ in range(cantidad_naranjas)
    )  # aplico una tupla por comprension y dejo la variable de iteración muda
    return tupla_pesos


def calcular_cajones(cantidad_naranjas: int) -> tuple:
    """
    Esta función calcula la cantidad de cajones que se pueden llenar
    pre: esta función recibe como parametro un entero positivo
    post: esta función devuelve una tupla equivalente a (cantidad jugo, cantidad cajones, sobrante, peso total KG)
    """
    tupla_pesos = calcular_rn_peso(cantidad_naranjas)
    cantidad_cajon = CAPACIDAD_CAJON
    cantidad_cajones = 0
    cantidad_jugo = 0
    peso_total = 0
    for valor in tupla_pesos:
        if valor in range(PESO_MIN, PESO_MAX):
            cantidad_cajon -= 1
            peso_total += valor
            if cantidad_cajon == 0:
                cantidad_cajones += 1
                cantidad_cajon = CAPACIDAD_CAJON
        else:
            cantidad_jugo += 1

    sobrante = CAPACIDAD_CAJON - cantidad_cajon
    return (
        cantidad_jugo,
        cantidad_cajones,
        sobrante,
        peso_total / 1000,
    )  # esto lo pasa a kilogramos


def calcular_cantidad_camiones(peso_total_cajones: int) -> int:
    """
    Esta función calcula la cantidad de camiones necesarios para transportar los cajones de naranjas.
    pre: Esta función recibe un entero que representa el peso total de los cajones en kilogramos.
    post: Esta función devuelve un entero que representa la cantidad de camiones necesarios.
    """
    cantidad_camiones = 0

    while peso_total_cajones > 0:
        if peso_total_cajones >= CAPACIDAD_CAMION:
            cantidad_camiones += 1
            peso_total_cajones -= CAPACIDAD_CAMION
        elif peso_total_cajones >= CAPACIDAD_MINIMA_CAMION:
            cantidad_camiones += 1
            peso_total_cajones = 0  # Último camión con capacidad mínima
        else:
            cantidad_camiones += 1
            peso_total_cajones = 0  # Último camión con carga incompleta

    return cantidad_camiones


def validar_num(num):
    return isinstance(num, int)


def menu():
    print()
    while True:
        try:
            cantidad_naranajas = int(input("Ingrese la cantidad de naranjas: "))
            if validar_num(cantidad_naranajas) and cantidad_naranajas > 0:
                break
            raise ValueError("Verifique el valor ingresado!")
        except ValueError as e:
            print(f"Error: {e}")
    # validación correcta
    cantidad_jugo, cantidad_cajones, sobrante, peso_total = calcular_cajones(
        cantidad_naranajas
    )  # desempaqueto
    print(f"La cantidad de naranjas para jugo es {cantidad_jugo}")
    print(f"La cantidad de cajones llenos es de {cantidad_cajones}")
    print(f"La cantidad de naranjas sobrantes para el proximo reparto es de {sobrante}")
    cantidad_camiones = calcular_cantidad_camiones(peso_total)
    print(
        f"La cantidad de camiones que se pueden despachar con {cantidad_cajones} cajones con un peso de {peso_total} es de {cantidad_camiones}"
    )
    return None


# variables globales
PESO_MIN = 200
PESO_MAX = 300
CAPACIDAD_CAJON = 100
CAPACIDAD_CAMION = 500
CAPACIDAD_MINIMA_CAMION = CAPACIDAD_CAMION * 0.8
# codigo principal
if __name__ == "__main__":
    menu()
