#Imprimir las líneas que terminan con un número
archivo = open('mbox.txt')
for linea in archivo:
    linea = linea.rstrip()
    if linea and linea[-1].isdigit():
        print(linea)