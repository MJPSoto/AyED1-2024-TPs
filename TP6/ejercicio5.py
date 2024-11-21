"""
Se dispone de tres formatos diferentes de archivos de texto en los que se almacenan datos de empleados, 
detallados más abajo. Desarrollar un programa para cada
uno de los formatos suministrados, que permitan leer cada uno de los archivos y
grabar los datos obtenidos en otro archivo de texto con formato CSV.
"""


def procesar_espacios_fijos(ruta: str, ruta_salida: str) -> None:
   """
   Procesa un archivo con campos de longitud fija, elimina los espacios innecesarios y
   escribe los datos en un archivo separados por comas.
   pre: Recibe como parametro 2 rutas en formato str
   post: No devuelve nada
   """
   try:
      with open(ruta, "r", encoding="utf-8") as file_read, open(
         ruta_salida, "w", encoding="utf-8"
      ) as file_write:
         data = file_read.readlines()
         for line in data:
               file_write.write(
                  f"{line[:17].strip()},{line[17:28].strip()},{line[28:].strip()}\n"
               )
      print("Archivo 1 actualizado correctamente.")
   except FileNotFoundError:
      print("El archivo no existe.")


def procesar_numero_digitos(ruta: str, ruta_salida: str) -> None:
   """
   Procesa un archivo con campos que su longitud son los 2 primeros digitos,
   estos se tiene que cargar en otro archivo, separados por comas
   pre: Recibe como parametro 2 rutas en formato str
   post: No devuelve nada
   """
   try:
      with open(ruta, "r", encoding="utf-8") as file_read, open(
         ruta_salida, "w", encoding="utf-8"
      ) as file_write:
         data = file_read.readlines()
         for line in data:
               line = line.strip()
               valor_inicial = 0
               data = []
               largo = int(line[valor_inicial : valor_inicial + 2])
               for i in range(3):
                  field = line[valor_inicial + 2 : valor_inicial + largo + 2]
                  valor_inicial += largo + 2
                  data.append(field)
                  if i == 2:
                     break
                  largo = int(line[valor_inicial : valor_inicial + 2])
               file_write.write(f'{",".join(data)}\n')
      print("Archivo 2 actualizado correctamente.")
   except FileNotFoundError:
      print("El archivo no existe.")


def main():
   procesar_espacios_fijos("archivoEspacioFijos1.txt", "archivoEspacioFijos2.txt")
   procesar_numero_digitos("archivoNumeroDigitos1.txt", "archivoNumeroDigitos2.txt")


if __name__ == "__main__":
   main()
