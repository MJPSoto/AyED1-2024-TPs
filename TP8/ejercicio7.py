"""
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes
"""


# librerias
# funciones
def validar_valor(mensaje: str, conjunto: set) -> set:
    """
        Valida el formato de valor ingresado por el usuario, si el valor es valido lo elimina del conjuto
        pre: Recibe como parametro un mensaje en formato str y un conjunto en formato set
        post: Devuelve un set
    """
    print(f"Conjunto inicial: {conjunto}")
    try:
        valor = int(input(mensaje))
        if valor == -1:
            return conjunto
        conjunto.remove(valor)
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
    except KeyError:
        print("La key ingresa no existe.")
    return validar_valor(mensaje, conjunto)


def main() -> None:
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    conjunto = set(range(10))
    
    validar_valor("Ingrese un número entre 0 y 9 para eliminar del conjunto (o -1 para finalizar): ",conjunto)
    print("Proceso finalizado.")


# variables globales
# codigo principal
if __name__ == "__main__":
    main()
