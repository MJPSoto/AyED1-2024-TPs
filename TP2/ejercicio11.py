"""
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado. 
"""
import random as rn

rn.seed(1)

lista_afiliados = [3201, 3201, 5179, 2931, 9117, 8364, 8737, 7219, 4439, 2537]
lista_tipo_atention = [rn.randint(0,1) for _ in range(10)]

def mostrar_listado_atention():
    if len(lista_tipo_atention) == 0:
        return
    urgencias = []
    turnos = []
    for afiliado, tipo in zip(lista_afiliados, lista_tipo_atention): #uso el zip para ir 1 a 1 en las 2 listas y despues desempaqueto la tupla
        if tipo == 0:
            urgencias.append(afiliado)
        else:
            turnos.append(afiliado)
    print("Pacientes atendidos por urgencia en orden de llegada:")
    for afiliado in urgencias:
        print(afiliado)
    
    print("\nPacientes atendidos con turno en orden de llegada:")
    for afiliado in turnos:
        print(afiliado)
    return None


def buscar_afiliado():
    while True:
        try:
            numero_afiliado = int(input("\nIngrese el número de afiliado a buscar -1 para salir: "))
            if numero_afiliado == -1:
                break
            raise ValueError("Verifique el valor ingresado!")
        except ValueError as e:
            print(f"Error: {e}")

        cantidad_turno = 0
        cantidad_urgencia = 0
        
        # Contamos las ocurrencias de ese afiliado
        for afiliado, tipo in zip(lista_afiliados, lista_tipo_atention):
            if afiliado == numero_afiliado:
                if tipo == 0:
                    cantidad_urgencia += 1
                else:
                    cantidad_turno += 1
        
        print(f"El afiliado {numero_afiliado} fue atendido {cantidad_urgencia} veces por urgencia y {cantidad_turno} veces con turno")

mostrar_listado_atention()
buscar_afiliado()