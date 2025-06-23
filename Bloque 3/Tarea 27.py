#Imprimir líneas que contienen un dominio específico
archivo = open('mbox.txt')
for linea in archivo:
    linea = linea.rstrip()
    if '@gmail.com' in linea:
        print(linea)
