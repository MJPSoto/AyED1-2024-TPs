"""
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""

# librerias
from tabulate import tabulate
# funciones
def generar_diccionario() -> dict:
    """
        Genera un diccionario con las llaves desde 1 al 20 y de valor cada potencia de esos valores
        pre: No recibe nada
        Post: Devuelve un diccionario con el formato {int : int}
    """
    return {i: i**2 for i in range(1, 21)}

def main() -> None:
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    diccionario_cuadrado = generar_diccionario()
    tabla = [(clave, valor) for clave, valor in diccionario_cuadrado.items()]
    
    print(tabulate(tabla, headers=["Número", "Cuadrado"]))

# variables globales
# codigo principal
if __name__ == "__main__":
    main()
