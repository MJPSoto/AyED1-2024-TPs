"""
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y 
un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para
verificar el comportamiento de la misma. Hacer tres versiones de la función, para
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""

def filtrar_palabras_ciclos(cadena: str, numero: int) -> str:
    lista_palabras = cadena.split()  # Separo la cadena pq supongo que es una frase separada por espacios ? mondongo
    cadena_nueva = ""
    for palabra in lista_palabras:
        if len(palabra) >= numero:
            cadena_nueva += palabra + " "
    return cadena_nueva.strip()  #Elimino el ultimo espacio

def filtrar_palabras_comprension(cadena: str, numero: int) -> str:
    lista_palabras = cadena.split()
    return " ".join(list(palabra for palabra in lista_palabras if len(palabra) >= numero))

def filtrar_palabras_filter(cadena: str, numero: int) -> str:
    lista_palabras = cadena.split()
    return " ".join(filter(lambda palabra: len(palabra) >= numero, lista_palabras))

def validar_fn()->None:
    assert(filtrar_palabras_ciclos("No se me ocurre nada", 3)) == "ocurre nada"
    assert(filtrar_palabras_comprension("No se me ocurre nada", 3)) == "ocurre nada"
    assert(filtrar_palabras_filter("No se me ocurre nada", 3)) == "ocurre nada"

    assert(filtrar_palabras_ciclos("mondongo hinojo lechuga tomate pancho", 7)) == "mondongo lechuga"
    assert(filtrar_palabras_comprension("mondongo hinojo lechuga tomate pancho", 7)) == "mondongo lechuga"
    assert(filtrar_palabras_filter("mondongo hinojo lechuga tomate pancho", 7)) == "mondongo lechuga"

    assert(filtrar_palabras_ciclos("Javier milei 1", 2)) == "Javier milei"
    assert(filtrar_palabras_comprension("Javier milei 1", 1)) == "Javier milei 1" 
    assert(filtrar_palabras_filter("Javier milei 1", 3)) == "Javier milei"
    return None

def menu()->None:
    while True:
        try:
            cadena = input("Ingrese la cadena: ")
            numero = int(input("Ingrese el numero: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    validar_fn()
    #tendria que poner una validación para que no muestre cuando no hay palabras con mayor longitud al numero ingresado, pero mondongo :)
    print(filtrar_palabras_ciclos(cadena, numero))
    print(filtrar_palabras_comprension(cadena, numero))
    print(filtrar_palabras_filter(cadena, numero))
    return None



if __name__ == "__main__":
    menu()
