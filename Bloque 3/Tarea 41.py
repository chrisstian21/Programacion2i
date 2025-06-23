#Ejercicio : Contar líneas que contienen números
contador = 0
with open("mbox.txt") as archivo:
    for linea in archivo:
        if any(char.isdigit() for char in linea):
            contador += 1
print("Líneas que contienen números:", contador)