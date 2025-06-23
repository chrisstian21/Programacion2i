# Paso 1: Escribir los datos de estudiantes y notas en un archivo
with open("notas.txt", "w") as archivo:
    archivo.write("Ana,15\n")
    archivo.write("Luis,9\n")
    archivo.write("Carlos,18\n")
    archivo.write("María,7\n")
    archivo.write("José,13\n")

# Paso 2: Leer el archivo y mostrar los estudiantes que aprobaron (nota >= 10)
with open("notas.txt", "r") as archivo:
    for linea in archivo:
        nombre, nota = linea.strip().split(",")  # Separar nombre y nota
        nota = int(nota)
        if nota >= 10:
            print(nombre, "aprobó con", nota)
        else: 
            print(nombre,"reprobo con", nota)