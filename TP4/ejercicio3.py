def obtener_claves(clave_maestra: int) -> tuple:
    """
    Está función obtiene una clave maestra y saca 2 claves nuevas con la condición de que los
    indices de la clave maestra son para la clave1 y los pares para la clave 2
    Pre: Está función necesita como pararmetro una clave maesta en formate entero
    Post: Está función devulve una tupla con las claves (clave1, clave2)
    """
    return tuple(
        "".join(digito for i, digito in enumerate(str(clave_maestra)) if i % 2 == j)
        for j in (0, 1)
    )


def menu() -> None:
    while True:
        try:
            clave_maestra = int(input("Ingrese la clave maestra: "))
            if len(str(clave_maestra)) >= 5:
                break
        except ValueError as e:
            print(f"Error: {e}")
    clave1, clave2 = obtener_claves(clave_maestra)
    print(f"La primer clave es {clave1} y la segunda clave es {clave2}")
    return None


if __name__ == "__main__":
    menu()
