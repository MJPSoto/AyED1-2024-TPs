"""
Realizar la implementación recursiva del método de selección para ordenar una lista
de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera
posición, y luego ordenar el resto de la lista con una llamada recursiva. No usar las
funciones min() ni max() de Python.
"""


def encontrar_indice_minimo(lista: list, pos_actual: int, indice_min: int) -> int:
    """
    Esta función encuentra el indice del menor elemento
    pre: Esta función recibe 3 parametros, una lista de numeros enteros, una posición actual entera y un indice minimo entero
    post: Esta función devuelve el índice del elemento menor
    """
    if pos_actual == len(lista):
        return indice_min
    # Comparo el elemento actual con el mínimo encontrado hasta ahora
    if lista[pos_actual] < lista[indice_min]:
        indice_min = pos_actual
    return encontrar_indice_minimo(lista, pos_actual + 1, indice_min)


def ordenar_lista(lista: list, position: int = 0) -> list:
    """
    Esta función ordena una lista cualquiera usando recursividad
    pre: Esta función recibe como parametro una lista y una posición del elemento a ordenar
    post: Esta función devuelve una lista ordenada
    """
    if position >= len(lista) - 1:
        return lista
    min_index = encontrar_indice_minimo(lista, position, position)
    lista[position], lista[min_index] = lista[min_index], lista[position]
    return ordenar_lista(lista, position + 1)


def menu() -> None:
    """
    Esta es la función principal donde se ejecuta todo el codigo
    Pre: Esta función no recibe ningun parametro
    Post: Esta función no devuelve nada
    """
    while True:
        try:
            lista_numeros = input(
                "Ingrese los numeros separados por coma, ejemplo 1,2,3....n: "
            )
            lista_numeros = list(
                map(int, lista_numeros.split(","))
            )  # esto me devuelve una lista con n numeros [num1, num2,.....numN]
            break
        except ValueError as e:
            print(f"Error: {e}")
    # lista completa y con los valores verificados
    print(f"La lista ingresada")
    print(lista_numeros)
    lista_ordenada = ordenar_lista(
        lista_numeros
    )  # el problema de está función es que serial mas parecida a un sort que a un sorted por que estamos modificando la lista original
    print("Lista ordenada")
    print(lista_ordenada)


if __name__ == "__main__":
    menu()
