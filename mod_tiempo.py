import time


def imprimir_segun_tiempo(tiempo: float, cadena, intervalo=.1):
    tf = time.time() + tiempo
    while time.time() < tf:
        print(cadena)
        time.sleep(intervalo)


imprimir_algo = input(" Ingrese lo que quisiera ver: ")
tiempo_a_imprimir = float(input(" ingrese un valor: "))

t0 = time.time()
prueba = imprimir_segun_tiempo(tiempo_a_imprimir, imprimir_algo)
print(f"{time.time() - t0}")