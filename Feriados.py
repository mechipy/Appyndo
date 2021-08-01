"""
Entrada: mi_funcion(6)
Salida:
El mes 6 tiene los siguientes feriados:
Dia 2 por motivo: el motivo asd asd
Dia 27: por motivo: asd asd asd as d
"""
import requests
from requests import exceptions


def mostrar_feriados(mes):
    if mes >= 13 or mes <= 0:
        raise Exception(" Ingrese el número de mes del 1 al 12")

    URL = "http://nolaborables.com.ar/api/v2/feriados/2021"
    print(" Estamos cargando la info. Please wait...")

    mis_feriados = []
    try:
        info = requests.get(URL)
    except exceptions.ConnectionError:
        print(" algo anda mal, Revisa tu conexión")
    else:
        print("Está todo OK... Continuamos")
        lista_feriados = info.json()
        for feriado in lista_feriados:
            if feriado["mes"] == mes:
                motivo = feriado["motivo"]
                dia = feriado["dia"]
                mis_feriados.append((dia, motivo))
                # print(feriado["motivo"], feriado["dia"])
    print(f"Los feriados del mes {mes} son: ")
    for dia, motivo in mis_feriados:
        print(f"El dia {dia} es feriado por: {motivo}")

mostrar_feriados(10)

