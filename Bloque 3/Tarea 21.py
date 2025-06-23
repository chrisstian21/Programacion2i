# ejercicio 1: Conteo Regresivo con while
n = 10
while n > 0:
    print(n)
    n -= 1
print("¡Despegue!")

# ejercicio 2: Palabra Secreta (while y break)
palabra_secreta = "python"

while True:
    intento = input("Adivina la palabra secreta: ")
    if intento == palabra_secreta:
        print("¡CORRECTO, FELICIDADES HAS ADIVINADO LA PALABRA!")
        break
    else:
        print("Inténtalo de nuevo.")

# Ejercicio 3: Entradas con continue

while True:
    entrada = input("Ingresa un texto: ")
    
    if entrada == "#":
        continue  

    if entrada == "listo":
        print("¡Procesamiento terminado!")
        break  

    print(entrada.upper()) 

# Ejercicio 4: Lista con for

invitados = ['Ana', 'Luis', 'Carla', 'Pedro']

for nombre in invitados:
    print(f"Hola {nombre}, ¡bienvenido/a a la fiesta!")

# Ejercicio 5: Número Mayor (for)

numeros = [3, 41, 12, 9, 74, 15, 1, 55]
mayor_hasta_ahora = -1

for numero in numeros:
    if numero > mayor_hasta_ahora:
        mayor_hasta_ahora = numero

print("El número más grande es:", mayor_hasta_ahora)

# Ejercicio 6: Elementos Pares (for y condicional)

numeros = [2, 5, 8, 11, 14, 17, 20, 23]
contador_pares = 0  

for numero in numeros:
    if numero % 2 == 0:  
        contador_pares += 1  

print("Cantidad de números pares:", contador_pares)

# Ejercicio 7: Suma de todos los números 

numeros = [10, 20, 30, 40, 50]
suma_total = 0  

for numero in numeros:
    suma_total += numero  

print("La suma total es:", suma_total)

# Ejercicio 9: Números mayores a un valor ingresado
numeros = [5, 25, 12, 33, 18, 45, 7]
umbral = int(input("Ingresa un número umbral: "))

print("Números mayores que", umbral, ":")
for numero in numeros:
    if numero > umbral:
        print(numero)

# Ejercicio 10: Búsqueda de un valor

numeros = [9, 41, 12, 3, 74, 15]
encontrado = False  
for numero in numeros:
    if numero == 3:
        encontrado = True
        break  

print(f"El valor 3 fue encontrado: {encontrado}")

# Ejercicio 11: Encontrando el numero menor

numeros = [30, 10, 5, 25, 50, 2]
menor_hasta_ahora = None  

for numero in numeros:
    if menor_hasta_ahora is None or numero < menor_hasta_ahora:
        menor_hasta_ahora = numero  
        
print("El número más pequeño es:", menor_hasta_ahora)


