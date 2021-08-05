def sumar_numeros(numeros: str) -> float:
    lista_1 = numeros.split()
    lista_2 = [float(elemento) for elemento in lista_1]
    return sum(lista_2)


prueba = input("ingrese numeros a sumar: ")
print(sumar_numeros(prueba))