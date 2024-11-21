"""
En geometría un vector es un segmento de recta orientado que va desde un punto
A hasta un punto B. Los vectores en el plano se representan mediante un par ordenado de números reales (x, y) llamados componentes. Para representarlos basta
con unir el origen de coordenadas con el punto indicado en sus componentes:
Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo: 
A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función. 
"""

# librerias


# funciones
def validar_ortogonal(vector1: tuple, vector2: tuple) -> bool:
    """
    Determina si dos vectores en el plano son ortogonales.
    pre: recibe 2 vectores en formato tupla (x, y)
    post: True si los vectores son ortogonales, False en caso contrario.
    """
    # determino el producto escalar para despues validarlo
    producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    return producto_escalar == 0


def validar_valor(mensaje: str) -> tuple:
    """
        Valida el formato de valor ingresado por el usuario 
        pre: Recibe como parametro un mensaje en formato str 
        post: Devuelve una tupla con el formato correcto 
    """
    valor = input(mensaje)
    try:
        valor = tuple(valor.split(","))
        if len(valor) != 2:
            raise ValueError(
                "Datos inválidos. Deben ser dos valores separados por comas."
            )
        valor = tuple(map(int, valor))
        return valor
    except ValueError as e:
        return validar_valor(mensaje)


# Programa principal
def main() -> None:
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    primer_vector = validar_valor("Ingrese los valores de la primer vector (x, y): ")
    segundo_vector = validar_valor("Ingrese los valores del segundo vector (x, y): ")

    prueba_funtion()
    ortogonal = validar_ortogonal(primer_vector, segundo_vector)
    if ortogonal:
        print(f"Los vectores son ortogonales")
    else:
        print(f"Los vectores son no ortogonales")


def prueba_funtion() -> None:
    """
        Valida el funcionamiento de la función validar_ortogonal
        pre: No recibe nada
        post: No devuelve nada
    """
    assert (validar_ortogonal((1, 0), (0, 1))) == True
    assert (validar_ortogonal((3, 4), (-4, 3))) == True
    assert (validar_ortogonal((2, 1), (1, -2))) == True
    assert (validar_ortogonal((5, 0), (0, -5))) == True
    assert (validar_ortogonal((2, 6), (4, 5))) == False

# Código principal
if __name__ == "__main__":
    main()