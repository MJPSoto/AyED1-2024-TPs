"""
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >
MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo.
"""


def leer_archivo(ruta_origen: str) -> list:
    """
    Está función lee un archivo con la ruta que le pasemos y nos devuelve una lista de lo que haya en ese archivo
    Pre: Está función recibe un parametro en formato str
    Post: Está función devuelve una lista con lo que leyo en el archivo
    """
    try:
        with open(ruta_origen, "r") as file:
            lista_deportes = [linea.strip() for linea in file.readlines()]
    except FileNotFoundError as e:
        return []
    lista_deportes_aux = []
    for item in lista_deportes:
        if item.isalpha():
            alturas = []
            lista_deportes_aux.append([item, alturas])
        else:
            alturas.append(item)
    return lista_deportes_aux


def GrabarPromedio(ruta_origen: str, ruta_destino: str) -> None:
    """
    Está función escribe en el archivo con la ruta que le pasemos el promedios de los atletas
    Pre: Está función recibe 2 parametros estos en formato str
    Post: Está función no devuelve nada
    """
    lista_deportes_aux = leer_archivo(ruta_origen)
    try:
        with open(ruta_destino, "a") as file:
            for item in lista_deportes_aux:
                file.write(
                    item[0]
                    + "\n"
                    + str(sum([float(num) for num in item[1]]) / len(item[1]))
                    + "\n"
                )
    except FileNotFoundError as e:
        print(f"Error: {e}")


def GrabarRangoAlturas(ruta: str, altura: float) -> None:
    """
    Está función escribe el archivo con la altura que le pasemos
    Pre: Está función recibe 2 parametros en formato str y float
    Post: Está función no devuelve nada
    """
    try:
        with open(ruta, "a") as file:
            file.write(str(altura) + "\n")
    except FileNotFoundError as e:
        print(f"Error: {e}")


def validar_altura(altura: float) -> bool:
    """
    Está función valida la altura ingresada
    Pre: Está función recibe un parametro en formato float, el cual es la altura a verificar
    Post: Está función devuelve un boleano dependiendo si es valida o no
    """
    return altura >= 1.6 and altura <= 2.5


def llenar_archivo() -> None:
    """
    Está función carga el archivo de alturas por categoria hasta que el usuario deje de cargar
    Pre: Está función no recibe nada
    Post: Está función no devuelve nada
    """
    while True:
        deporte = input("Ingrese el deporte (-1 para salir): ")
        if deporte == "-1":
            break
        GrabarRangoAlturas("alturas.txt", deporte)
        while True:
            try:
                altura = float(input("Ingrese la altura (-1 para salir): "))
                if altura == -1:
                    break
                if validar_altura(altura):
                    GrabarRangoAlturas("alturas.txt", altura)
                    print("Altura cargada correrctamente")
                else:
                    print("Altura no valida")
            except ValueError as e:
                print(f"Error: {e}")


def MostrarMasAltos(ruta_alturas: str, ruta_promedio: str) -> None:
    """
    Está función muestra las categorias donde cada deportistas de las mismas supera el promedio de esa categoria
    Pre: Está función recibe 2 parametos en formato str
    Post: Está función no devuelve nada
    """
    lista_alturas = leer_archivo(ruta_alturas)
    lista_promedio = leer_archivo(ruta_promedio)
    lista_mayor_promedio = []
    for i, item in enumerate(lista_alturas):
        mayor = True
        for num in item[1]:
            if num < lista_promedio[i][1][0]:
                mayor = False
                break
        if mayor:
            lista_mayor_promedio.append(item[0])
    if lista_mayor_promedio:
        print("Las categorias que superan el promedio son: ")
        for categoria in lista_mayor_promedio:
            print(categoria)


def menu() -> None:
    """
    Está es la función principal donde se ejecuta todo el codigo
    Pre: Está función no recibe ningun parametro
    Post: Está función no devuelve nada
    """
    llenar_archivo()
    GrabarPromedio("alturas.txt", "promedio.txt")
    MostrarMasAltos("alturas.txt", "promedio.txt")


if __name__ == "__main__":
    menu()
