def cadena_capicua(cadena: str) -> bool:
    """
    Está función valida si una cadena en formato str es capicua o no
    
    pre: Está función necesita como paramtro una cadena en fomato str
    
    post: Está función devuelve un booleano dependiendo si es capicua o no
    """
    return cadena == cadena[::-1]


def validar_fn():
    """
    Está función valida el funcionamiento de la funcion 'cadena_capicua'
    
    pre: Está función no recibe ningun parametro
    
    post: Está función no devuelve nada
    """
    assert (cadena_capicua("oso")) == True
    assert (cadena_capicua("osos")) == False
    assert (cadena_capicua("mondongo")) == False
    assert (cadena_capicua("hinojo")) == False
    assert (cadena_capicua("oro")) == True
    return None


def menu() -> None:
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
