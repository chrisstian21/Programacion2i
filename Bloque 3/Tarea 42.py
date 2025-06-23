#Contar Lineas en un archivo 
with open("mi_documento.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

print(f"El archivo tiene {len(lineas)} líneas.")