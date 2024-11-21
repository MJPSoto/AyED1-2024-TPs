"""
Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""
import string

def eliminar_palabras_repetidas(frase: str) ->list:
    """
        Elimina las palabras repetidas
        pre: Recibe una frase en formato de str 
        post: devuelve una lista con las palabras de la frase sin repetir ordenadas por la longitud
    """
    frase = frase.translate(str.maketrans("", "", string.punctuation))
    palabras = frase.lower().split()
    lista_palabras = list(set(palabras))
    lista_palabras.sort(key=len)
    return lista_palabras

# Programa principal
def main() -> None:
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    frase = input("Ingrese una frase: ")
    frase_sin_palabras_repetidas = eliminar_palabras_repetidas(frase)
    print(f"La frase sin palabras repetidas es: ")
    print(frase_sin_palabras_repetidas)

# Código principal
if __name__ == "__main__":
    main()
