"""
Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse 
después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""

###### no se 
def dividir_archivo(archivo_entrada: str, tamaño_maximo: int) -> None:
    """
        Divide el archivo de texto en la cantidad de caracteres, crea un archivo por cada parte que cumpla el largo 
        Pre: Recibe como parametro un ruta base donde se encuentra el texto en formato str y un tamaño maximo en formato int
        post: No devuelve nada
    """
    try:
        with open(archivo_entrada, 'rt', encoding='utf-8') as archivo:
            base_nombre = archivo_entrada.rsplit('.', 1)[0]
            parte_num = 1
            contenido_parte = ""
            tamaño_actual = 0
            
            for linea in archivo:
                if tamaño_actual + len(linea) > tamaño_maximo:
                    with open(f"{base_nombre}_parte{parte_num}.txt", 'wt', encoding='utf-8') as salida:
                        salida.write(contenido_parte)
                    parte_num += 1
                    contenido_parte = linea
                    tamaño_actual = len(linea)
                else:
                    contenido_parte += linea
                    tamaño_actual += len(linea)
            
            if contenido_parte.strip(): 
                with open(f"{base_nombre}_parte{parte_num}.txt", 'wt', encoding='utf-8') as salida:
                    salida.write(contenido_parte)
                
            print("Archivo dividido exitosamente.")
    
    except Exception as e:
        print(f"Error al dividir el archivo: {e}")

def validar_valor(mensaje: str) -> int:
    """
        Valida el formato de valor ingresado por el usuario 
        pre: Recibe como parametro un mensaje en formato str 
        post: Devuelve una tupla con el formato correcto 
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    """
        Funcion principal donde se ejecuta todo el codigo
        Pre: No recibe ningun parametro
        Post: No devuelve nada 
    """
    tamaño_maximo = validar_valor("Ingrese el tamaño máximo para cada parte (en caracteres): ")
    dividir_archivo("separar.txt", tamaño_maximo)

if __name__ == "__main__":
    main()
