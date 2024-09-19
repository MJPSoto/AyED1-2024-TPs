"""
Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función. 
"""

def reemplazar_palabra(cadena, palabra_original, palabra_nueva):
    palabras = cadena.split()
    cantidad_reemplazos = 0
    for i, palabra in enumerate(palabras):
        if palabra == palabra_original:
            palabras[i] = palabra_nueva
            cantidad_reemplazos += 1
    return ' '.join(palabras), cantidad_reemplazos

def validar_fn()->None:
    
    return None

def menu()->None:
    cadena = input("Ingrese la cadena: ")
    palabra_original = input("Ingrese la palabra original: ")
    palabra_nueva = input("Ingrese la palabra nueva: ")
    cadena_resultante, cantidad_remplazos = reemplazar_palabra(cadena, palabra_nueva, palabra_original)
    print(f"La palabra nueva es {cadena_resultante} y se hicieron {cantidad_remplazos} cambios")
    return None

if __name__ == "__main__":
    menu()