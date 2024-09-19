"""
Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
"""

def obtener_claves(clave_maestra: int)->tuple:
    clave_maestra_str = str(clave_maestra)
    clave2 = ""
    clave1 = ""
    for i, caract in enumerate(clave_maestra_str):
        if i % 2 == 0:
            clave1 += caract
        else:
            clave2 += caract
    return clave1, clave2 #mondono? 

def menu()->None:
    while True:
        try:
            clave_maestra = int(input("Ingrese la clave maestra: "))
            if len(str(clave_maestra)) >= 5:
                break
        except ValueError as e:
            print(f"Error: {e}")
    clave1, clave2 = obtener_claves(clave_maestra)
    print(f"La primer clave es {clave1} y la segunda clave es {clave2}")
    return None

if __name__ == "__main__":
    menu()