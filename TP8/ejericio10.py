"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

# librerias
from tabulate import tabulate


# funciones
def eliminarclaves(diccionario: dict, claves: list) -> tuple:
    """
        Elimina las los items de un diccionario 
        pre: Recibe como parametro un diccionario y las claves a borrar en formato lista 
        post: Devuelve una tupla con el diccionario y la cantidad de claves eliminadas
    """
    #No quiero hacer mas contratos......
    claves_eliminadas = len(diccionario) - len(
        {k: v for k, v in diccionario.items() if k not in claves}
    )
    diccionario = {k: v for k, v in diccionario.items() if k not in claves}
    return diccionario, claves_eliminadas


def main() -> None:    
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    # ejemplo del funcionamiento
    diccionario = {
        "nombre": "pablo",
        "edad": 25,
        "ciudad": "Madrid",
        "profesion": "Ingeniero",
        "pais": "España",
    }
    claves_a_eliminar = ["edad", "pais", "profesion"]

    diccionario_modificado, cantidad_eliminada = eliminarclaves(
        diccionario, claves_a_eliminar
    )
    tabla = [(clave, valor) for clave, valor in diccionario_modificado.items()]

    print(tabulate(tabla, headers=["key", "value"]))
    print(f"Cantidad de claves eliminadas: {cantidad_eliminada}")


# variables globales
# codigo principal
if __name__ == "__main__":
    main()
