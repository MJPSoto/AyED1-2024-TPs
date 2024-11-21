"""
Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. 
Comprobar el comportamiento de la función mediante un programa apropiado.
"""


def buscarclave(diccionario: dict, valor: int) -> list:
   """
   Devuelve una lista de claves que apuntan al valor dado en el diccionario.
   Pre: Recibe un diccionario {key, value} y un valor a buscar en formato entero.
   Post: Devuelve una lista con las claves cuyos valores coinciden con el valor recibido.
   """
   return [clave for clave, val in diccionario.items() if val == valor]


def validar_valor(mensaje: str) -> int:
   """
   Devuelve un valor válido casteado a entero.
   Pre: Recibe un mensaje en formato str.
   Post: Devuelve un valor validado que se pueda castear a un valor entero.
   """
   try:
      valor = int(input(mensaje))
      return valor
   except ValueError:
      print("Por favor, ingrese un número válido.")
      return validar_valor(mensaje)


# Función principal
def main() -> None:
   """
   Función principal donde se ejecuta todo el código.
   Pre: No recibe ningún parámetro.
   Post: No devuelve nada.
   """
   diccionario_ejemplo = {
      "nose": 10,
      "mapa": 20,
      "cadena": 10,
      "pancho": 30,
      "hola": 20,
   }
   valor = validar_valor("Ingrese el valor a buscar en el diccionario: ")
   claves_encontradas = buscarclave(diccionario_ejemplo, valor)
   if claves_encontradas:
      print(f"Las claves que tienen el valor {valor} son: {claves_encontradas}")
   else:
      print(f"No se encontraron claves con el valor {valor}.")


def validar_funcion(diccionario: dict) -> None:
   """
   Valida la función buscarclave mediante casos de prueba definidos.
   Pre: Recibe como parametro un diccionario {key, value}
   post: No devuelve nada
   """
   assert buscarclave(diccionario, 10) == ["nose", "cadena"], "Error en caso 1"
   assert buscarclave(diccionario, 30) == ["pancho"], "Error en caso 2"
   assert buscarclave(diccionario, 40) == [], "Error en caso 3"
   assert buscarclave({}, 10) == [], "Error en caso 4"


# Código principal
if __name__ == "__main__":
   diccionario_prueba = {
      "nose": 10,
      "mapa": 20,
      "cadena": 10,
      "pancho": 30,
      "hola": 20,
   }
   validar_funcion(diccionario_prueba)
   main()
