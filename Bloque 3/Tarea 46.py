#4. Copiar el contenido de un archivo a otro
with open("original.txt", "r") as archivo_original:
    contenido = archivo_original.read()

with open("copia.txt", "w") as archivo_copia:
    archivo_copia.write(contenido)

print("Archivo copiado correctamente.")