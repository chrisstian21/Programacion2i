#Ejercicio : Contar el total de palabras en todo el archivo
contador = 0
with open("mbox.txt") as archivo:
    for linea in archivo:
        contador += len(linea.split())
print("Cantidad total de palabras:", contador)