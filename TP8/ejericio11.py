"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

# librerias
# funciones


def contarvocales(palabra: str) -> dict:
    """
        Cuenta la cantidad de vocales que tiene una palabra 
        Pre: Recibe como parametro una palabra en formato str 
        post: Devuelve un diccionario con la cantidad de vocales que tiene esa palabra
    """
    vocales = "aeiouAEIOU"
    contar_vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in palabra:
        if letra in vocales:
            contar_vocales[letra.lower()] += 1
    return contar_vocales


def main() -> None:
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    frase = input("Ingrese una frase: ")
    lista_palabras = frase.split(" ")
    for palabra in lista_palabras:
        print(f"{palabra}. {contarvocales(palabra)}")


# variables globales
# codigo principal
if __name__ == "__main__":
    main()
