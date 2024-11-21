"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y
 nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cadena 
"IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor.
"""

#funciones
def leer_archivo(ruta: str) -> list:
    """
        Está función lee todas las lineas de un archivo que le pasemos 
        Pre: Está función recibe como parametro una ruta en formato str 
        Post: Está función devuelve una lista con la lectura del archivo 
    """
    try:
        with open(ruta, "+r") as file: #abro el archivo en formato lectura
            lista_nombres = file.readlines() #leo todas las lineas 
    except FileNotFoundError as e:
        return []
    return lista_nombres #devuelvo la lista de nombres

def escribir_archivo(cadena: str, ruta: str)->None:
    """
        Está función escribe en un archivo la cadena que nosotros le pasemos 
        Pre: Está función recibe 2 parametros en formato str donde uno es lo se va a escribir y el otro es la ruta
        Post: Está función no devuelve nada
    """
    try:
        with open(ruta, "a") as file: #abro el archivo y si no existe lo creo
            file.write(cadena + "\n") #escribo en el archivo la cadena y le agrego un salto de linea
    except FileNotFoundError as e:
        print(f"Error: {e}")
 
def separar_apellidos(lista_nombres: list)->None:
    """
        Está función separa los apellidos por como finalizan y los escribe en un archivo diferente 
        Pre: Está función recibe como parametro una lista de str
        Post: Está función no devuelve nada
    """
    for nombre in lista_nombres: #recoro la lista de nombres 
        apellido = nombre.split(",")[0] #obtengo el apellidos de esa cadena
        if "ian" in apellido[-3::]: #pregunto si finaliza en ian
            escribir_archivo(apellido, "ARMENIA.txt")
        elif "ini" in apellido[-3::]: #pregunto si finaliza en ini
            escribir_archivo(apellido, "ITALIA.txt")
        elif "ez" in apellido[-2::]: #pregunto si finaliza en ez
            escribir_archivo(apellido, "ESPAÑA.txt")

def menu()->None:
    """
        Está es la función principal donde se ejecuta todo el codigo
        Pre: Está función no recibe ningun parametro
        Post: Está función no devuelve nada 
    """
    nombres = ["Arslanian, Gustavo", "Rossini, Giuseppe", "Pérez, Juan", "Smith, John", "Soto, Mateo"] #hardcodee la lista de los nombre 
    for nombre in nombres:
        escribir_archivo(nombre, "nombres.txt") #creo el archivo para que no se rompa 
    nombres = leer_archivo("nombres.txt") #leo el archivo creado anteriormente
    if nombres:
        separar_apellidos(nombres) #separo los apellidos
    else:
        print("No se pudo leer el archivo.")

#codigo principal
if __name__ == "__main__":
    menu()

