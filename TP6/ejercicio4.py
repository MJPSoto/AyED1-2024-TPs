"""
Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. 
Tener en cuenta que los comentarios comienzan con el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles) y que también se 
considera comentario a las cadenas de documentación
(docstrings).
"""


def leer_archivo(ruta: str) -> list:
    """
    Está función lee un archivo cualquier y devuelve una lista con las lineas de ese archivo
    Pre: Está función recibe una ruta en formato str para abrir el archivo y leerlo
    Post: Está función devuelve una lista con las lineas de ese archivo
    """
    try:
        with open(ruta, "r") as file:
            Lista_lineas = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError as e:
        print(f"Error: {e}")
    return Lista_lineas


def borrar_comentarios(lista_comentarios: list) -> list:
    """
    Está función borrar las lineas que tenga el formato de comentario simple o docstring
    Pre: Está función recibe como parametro una lista de string que son las lineas del documento py
    Post: Está función devuelve una nueva lista sin los comentarios
    """
    lista_sin_comentarios = [
        line for line in lista_comentarios if not (line.strip().startswith("#"))
    ]
    while '"""' in lista_sin_comentarios:
        inico_docstring = lista_sin_comentarios.index('"""')
        lista_sin_comentarios.pop(inico_docstring)
        fin_docstring = lista_sin_comentarios.index('"""')
        lista_sin_comentarios.pop(fin_docstring)
        lista_sin_comentarios = [
            line
            for line in lista_sin_comentarios
            if not (line in lista_sin_comentarios[inico_docstring:fin_docstring])
        ]
    return lista_sin_comentarios


def menu() -> None:
    """
    Está es la función principal donde se ejecuta todo el codigo
    Pre: Está función no recibe ningun parametro
    Post: Está función no devuelve nada
    """
    lista_lineas = leer_archivo("lineas.py")
    print(borrar_comentarios(lista_lineas))


if __name__ == "__main__":
    menu()
