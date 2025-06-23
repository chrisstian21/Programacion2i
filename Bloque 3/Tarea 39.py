with open("palabras.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

contenido = contenido.lower()

contador = contenido.count("hola")

print(f"La palabra 'hola' aparece {contador} veces en el archivo.")