import os

while True:
    nombre_archivo = input("Ingrese nombre de archivo a crear: ")
    if not os.path.exists(nombre_archivo):
        break

while True:
    guardar_en_archivo = input("Ingrese lo que desea escribir en el archivo \n [e para salir]: ")
    if guardar_en_archivo != "e":
        with open(nombre_archivo, "a") as archivo:
            archivo.write(guardar_en_archivo + "\n")
    else:
        break


ver_guardado = input("quiere ver lo que escribió? [S/N]: ")

if ver_guardado in "Ss":
    with open(nombre_archivo, "r") as leer:
        print(leer.read())
else:
    print("hasta luego")
