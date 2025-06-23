# Buscar y contar una palabra en un archivo
palabra_buscar = "en"
contador = 0

with open("mi_documento.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        contador += linea.lower().count(palabra_buscar.lower())

print(f"La palabra '{palabra_buscar}' aparece {contador} veces en el archivo.")