"""
El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""

#funciones
def llenar_lista(num: int) -> None:
    """
        Está función carga el dato en la lista
        Pre: Está función recibe 1 parametro en formato entero
        Post: Está función no devuelve nada
    """
    lista_numeros.append(num)
    return None


def obtener_position(num: int) -> int:
    """
        Está función muestra la posición de un dato en la lista 
        Pre: Está función recibe 1 parametro en formato entero
        Post: Está función devuelve la posición del dato ingresado
    """
    return lista_numeros.index(num)


def cargar_datos(mostrar: int, texto_mostrar: str) -> None:
    """
        Está función carga los datos en una lista y muestra la posición del numero que ingrese el usuario
        Pre: Está función recibe 2 parametros uno en formato entero y el otro en formato str 
        Post: Está función no devuelve nada
    """
    error = 0
    while True:
        try:
            num = int(input(f"{texto_mostrar}"))
            if num == -1 or error == 3:
                break
            if mostrar == 1:
                print(f"El numero ingresado esta en la posición {obtener_position(num)+1}")
            else:
                llenar_lista(num)
        except (ValueError, TypeError, IndexError) as e:
            print(f"Error: {e}")
            error += 1
    return None


def menu() -> None:
    """
        Está es la función principal donde se ejecuta todo el codigo
        Pre: Está función no recibe ningun parametro
        Post: Está función no devuelve nada 
    """
    cargar_datos(0, "Ingrese un numero para cargar (-1 para salir): ")
    cargar_datos(1, "Ingrese un numero para mostrar (-1 para salir): ")
    return None

# variables
lista_numeros = []

#codigo principal
if __name__ == "__main__":
    menu()



