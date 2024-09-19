def cadena_capicua(cadena):
    return cadena == cadena[::-1]

def validar_fn():
    assert(cadena_capicua("oso")) == True
    assert(cadena_capicua("osos")) == False
    assert(cadena_capicua("mondongo")) == False
    assert(cadena_capicua("hinojo")) == False
    assert(cadena_capicua("oro")) == True
    return None

def menu()->None:
    cadena = input("Ingrese una cadena para ver si es capicua: ")
    validar_fn()
    validation = cadena_capicua(cadena)
    if validation:
        print("La cadena ingresa es capicua")
    else:
        print("La cadena ingresa no es capicua")
    return None



if __name__ == "__main__":
    menu()