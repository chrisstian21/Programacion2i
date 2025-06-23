print("\n1.")
lista = ['manzana', 'banana', 'cereza', 'durazno', 'kiwi']
for indice, elemento in enumerate(lista):
    print(f"Índice {indice}: {elemento}")
    
print("\n2.")
entrada = input("Ingresa varias palabras separadas por espacios: ")
lista_palabras = entrada.split()
palabra_mas_larga = max(lista_palabras, key=len)
print(f"La palabra más larga es: {palabra_mas_larga}")

print("\n3.")
linea = input("Ingresa una línea de texto: ")
palabras = linea.lower().split()
frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1
print("\nFrecuencia de palabras:")
for palabra, cantidad in frecuencias.items():
    print(f"{palabra}: {cantidad}")
    
print("\n4.")
from collections import Counter
with open('mbox.txt', 'r', encoding='utf-8') as archivo:
    texto = archivo.read()
palabras = texto.lower().split()
contador = Counter(palabras)
top3 = contador.most_common(3)
print("Las 3 palabras más repetidas son:")
for palabra, frecuencia in top3:
    print(f"{palabra}: {frecuencia} veces")
    
print("\n5.")
tienda = {
    'manzanas': 0.50,
    'pan': 1.20,
    'leche': 1.50,
    'queso': 2.30,
    'huevos': 1.80}
print("Productos disponibles en la tienda:")
for producto, precio in tienda.items():
    print(f"- {producto.capitalize()}: ${precio:.2f}")
busqueda = input("\n¿Qué producto deseas buscar? ").lower()
if busqueda in tienda:
    print(f"El precio de {busqueda} es ${tienda[busqueda]:.2f}")
else:
    print("Lo siento, ese producto no está disponible.")