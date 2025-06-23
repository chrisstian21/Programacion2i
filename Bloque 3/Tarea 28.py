#Contar cuántas líneas empiezan con 'Subject:'
archivo = open('mbox.txt')
contador = 0
for linea in archivo:
    if linea.startswith('Subject:'):
        contador += 1
print('Total de líneas con Subject:', contador)