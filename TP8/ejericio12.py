"""
Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio.
"""


# librerias
# funciones
def almacenar_producto(dict_precios: dict) -> dict:
   """
      Almacena en un diccionario el nombre y el precio de cada producto que ingrese el usuario 
      pre: Recibe un diccionario de productos con sus precios en el formato de {str: float}
      post: Devuelve el mismo diccionario con los datos cargados
   """
   try:
      nombre = input("Ingrese nombre del producto: ")
      precio = float(input("Ingrese el precio del producto (-1 para salir): "))
      if precio == -1.0:
         return dict_precios
      dict_precios[nombre] = precio
   except ValueError:
      print("Por favor, ingrese un valor numérico válido.")
   return almacenar_producto(dict_precios)


def incrementar_precios_cuadernos(dict_precios: dict) -> dict:
   """
      Incremente el precio del producto 'cuaderno' en un 15%
      pre: Recibe como paramentro un diccionario {nombre_producto: precio} {str : float}
      post: Devuelve el mismo diccionario con el precio cambiado 
   """
   dict_precios["cuaderno"] *= 1.15
   return dict_precios


def imprimir_listado_precios(dict_precios: dict) -> None:
   """
      Muestra por consola los productos y precios
      pre: Recibe como parametro un diccionario {nombre_producto: precio} {str : float}
      post: No devuelve nada
   """
   print("\nListado de precios:")
   for item, precio in dict_precios.items():
      print(f"{item.capitalize()}: ${precio:.2f}")


def obtener_item_mas_costoso(dict_precios: dict) -> tuple:
   """
      Obtiene el producto y valor mas caro de un diccionario 
      pre: Recibe como parametro un diccionario {nombre_producto: precio} {str : float}
      post: Devuelve una tupla con el nombre del producto y el precio
   """
   elemento_mas_caro = max(dict_precios, key=dict_precios.get)
   precio_mas_caro = dict_precios[elemento_mas_caro]
   return elemento_mas_caro.capitalize(), precio_mas_caro


def main() -> None:
   """
      Funcion principal donde se ejecuta todo el codigo
      Pre: No recibe ningun parametro
      Post: No devuelve nada 
   """
   dict_productos = almacenar_producto({})
   dict_productos = incrementar_precios_cuadernos(dict_productos)
   imprimir_listado_precios(dict_productos)
   producto, precio = obtener_item_mas_costoso(dict_productos)
   print(f"El producto mas caro es {producto} con el precio de {precio}")
   return


# variables globales

# codigo principal
if __name__ == "__main__":
    main()
