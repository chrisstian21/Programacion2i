#Imprimir las primeras 10 líneas del archivo
archivo = open('mbox.txt')
contador = 0
for linea in archivo:
    print(linea.rstrip())
    contador += 1
    if contador == 10:
        break