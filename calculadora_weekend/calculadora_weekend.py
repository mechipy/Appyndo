print("***** CALCULADORA ***** \n",
        "Menu \n",
        "1) Suma \n 2) Resta \n 3) Multiplicación \n",
        "4) División \n 5) Salir")

fin = False

while not fin:
    opc = int(input("Opción: "))
    if opc == 1:
        sum1 = int(input("Sumando uno: "))
        sum2 = int(input("Sumando dos: "))
        print("la suma es: ", sum1 + sum2)
    elif opc == 2:
        minuendo = int(input("Minuendo: "))
        sustraendo = int(input("Sustraendo: "))
        print("la resta es: ", minuendo - sustraendo)
    elif opc == 3:
        multiplicando = int(input("Multiplicando: "))
        multiplicador = int(input("Multiplicador: "))
        print("la multiplicación es: ", multiplicando * multiplicador)
    elif opc == 4:
        dividendo = int(input("Dividendo: "))
        divisor = int(input("Divisor: "))
        print("la división es: ", dividendo / divisor)
    elif opc == 5:
        fin = True
