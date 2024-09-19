"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
"""

def centrar_cadena(cadena: str, cantidad_columnas: int = 80)->None:
    cantidad_caracteres = len(cadena)
    espacios_izquierda = (cantidad_columnas - cantidad_caracteres) // 2
    return f"{' '*espacios_izquierda + cadena}" #centrarla en la pantalla de la terminal o en las 80 columnas? mondongo

def menu()->None:
    cadena = input("Introduce una cadena: ")
    print("La cadena centra: \n")
    print(centrar_cadena(cadena))
    return None

if __name__ == "__main__":
    menu()