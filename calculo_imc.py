def calcular_IMC(peso: float, altura: float):
    imc = peso / altura ** 2
    return round(imc, 1)


def analizar_IMC(im: float):
    print("su indice es ", im)
    if im < 18.5:
        print(" IMC = BAJO PESO")

    elif im > 18.5 and im < 24.9:
        print(" IMC = PESO NORMAL")

    elif im > 25.0 and im < 30.0:
        print(" IMC = SOBREPESO")

    elif im >= 30.0:
        print("IMC = OBESIDAD")


def mostrar_IMC():
    try:
        peso = float(input(" Introduzca su peso en Kg: "))
        altura = float(input(" Introduzca su altura en metros: "))
    except Exception:
        print(" algo ocurrió, inténtalo de nuevo")
    else:
        imc = calcular_IMC(peso, altura)
        analizar_IMC(imc)


mostrar_IMC()