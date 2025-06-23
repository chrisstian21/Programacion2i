# Creamos un archivo con algunos números
with open("numeros.txt", "w") as f:
    f.write("8\n15\n23\n5\n11")

# Abrimos el archivo en modo lectura
with open("numeros.txt", "r") as f:
    numeros = [int(linea) for linea in f]  # Convertimos cada línea en número entero

# Calculamos el promedio
promedio = sum(numeros) / len(numeros)

print("El promedio es:", promedio)