"""
Escribir un programa que permita ingresar una cadena de caracteres y coloque en
mayúscula la primera letra posterior a un espacio, eliminando todos los espacios
que contenga. Imprimir por pantalla la cadena obtenida.
Ejemplo:
Cadena original:
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva hue-
sos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Cadena final:
PlateroEsPequeño,Peludo,Suave;TanBlandoPorFuera,QueSeDiríaTodoDeAlgodón,QueNoLlevaHuesos.Sólo
LosEspejosDeAzabacheDeSusOjosSonDurosCualDosEscarabajosDeCristalNegro.
"""

def agegar_mayuscula(cadena: str)->str:
    """
    Está función separa por palabras una cadena n, le agrega una mayuscula en el primer caracter de todas las palabras
    
    Pre: Está función necesita como parametro una cadena en formato str 
    
    Post: Está función devuelve otra cadena en formato str con cada palabra con la primer letra en mayuscula y sin espacios 
    """
    return "".join(list(valor.capitalize() for valor in cadena.split()))

cadena = """Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva hue-
sos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
"""

def menu() -> None:
    cadena = input("Ingrese una cadena para agregarle mayuscula a todas las palabras: ")
    print(agegar_mayuscula(cadena))
    return None


if __name__ == "__main__":
    menu()

