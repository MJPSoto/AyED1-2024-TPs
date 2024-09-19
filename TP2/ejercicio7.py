"""
Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes.
"""
# funciones
def intercalar_elementos(lista1: list, lista2: list) -> None:
    for i, valor in enumerate(lista2):
        lista1[i + 1:i + 1] = [valor]
        i += 2
    return lista1

def menu():
    # hacer menu
    print(intercalar_elementos([8, 1, 3], [5, 9, 7]))
    return None


# codigo principal
if __name__ == "__main__":
    menu()

