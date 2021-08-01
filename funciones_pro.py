# def quitar_espacios(cadena: str) -> str:
#     nueva_cadena = cadena.replace(" ", "")
#    return nueva_cadena


# cadena_usuario = quitar_espacios("hola como estas")

# print(cadena_usuario)

def f(cadena):
    nueva = ""
    for c in cadena:
        if not c.isspace():
            nueva += c
    return nueva


def cambiar_pares_may(cadena: str) -> str:
    cadena_cambiada = ""
    for indice, caracter in enumerate(cadena):
        if indice % 2 == 0:
            cadena_cambiada += caracter.upper()
        else:
            cadena_cambiada += caracter
    return cadena_cambiada


def reemplazar_en_cadena(cadena, parametro_1=" ", parametro_2="u"):
    cadena_reemplazada = ""
    for letra in cadena:
        if letra == parametro_1:
            cadena_reemplazada += parametro_2
        else:
            cadena_reemplazada += letra
    return cadena_reemplazada
    # return cadena.replace(parametro_1, parametro_2)
    # return cadena_reemplazada


def quitar_espacios(cadena):
    return reemplazar_en_cadena(cadena, parametro_2="")


assert quitar_espacios("         jj   j   sss") == "jjjsss"
assert reemplazar_en_cadena("hola como estassssss")  == "holaucomouestassssss"
assert reemplazar_en_cadena("hola como estassssss", parametro_2="U")  == "holaUcomoUestassssss"
assert reemplazar_en_cadena("hola como estassssss", parametro_1="x")  == "hola como estassssss"
assert reemplazar_en_cadena("hola como estassssss", parametro_2="gabox", parametro_1="s")  == "hola como egaboxtagaboxgaboxgaboxgaboxgaboxgabox"