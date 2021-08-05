from datetime import datetime


def calcular(año_nac: int) -> int:
    año_actual = datetime.now().year
    return año_actual - año_nac


def contar_caracteres(cadena: str) -> int:
    """ esta funcion devuelve la cantidad de caracteres,
    excluyendo los espacios en blanco"""
    cont = 0

    for i in cadena:
        if not i.isspace():
            cont += 1

    return cont


assert calcular(1991) == 30
assert calcular(1994) == 27
assert calcular(2000) == 21

assert contar_caracteres("  hola") == 4
assert contar_caracteres("  ") == 0
assert contar_caracteres("  hola je je") == 8
assert contar_caracteres("  j j j                                                                       ") == 3