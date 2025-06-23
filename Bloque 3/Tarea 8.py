# 1. Crear una función que imprima un mensaje
def saludo():
    print("¡Hola, mundo!")

saludo()

# 2. Función con un argumento
def saludar(nombre):
    print("Hola,", nombre)

saludar("Christian")

# 3. Suma de dos números
def sumar(a, b):
    return a + b

print("Suma:", sumar(4, 7))

# 4. Calcular el salario
def computepay(horas, tarifa):
    if horas > 40:
        extra = horas - 40
        pago = 40 * tarifa + extra * tarifa * 1.5
    else:
        pago = horas * tarifa
    return pago

print("Pago:", computepay(45, 10))

# 5. Función para determinar el mayor carácter
def mayor_caracter(cadena):
    mayor = cadena[0]
    for c in cadena:
        if c > mayor:
            mayor = c
    return mayor

print("Mayor carácter:", mayor_caracter("python"))

# 6. Conversión de tipo
def convertir_a_flotante(valor):
    try:
        return float(valor)
    except:
        return "No se puede convertir"

print("Convertido:", convertir_a_flotante("3.14"))

# 7. Saludo en diferentes idiomas
def saludo_idioma(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print("Saludo:", saludo_idioma("fr"))

# 8. Comprobar si un número es par
def es_par(numero):
    return numero % 2 == 0

print("¿Es par?:", es_par(8))

# 9. Concatenar cadenas
def concatenar(cad1, cad2):
    return cad1 + cad2

print("Concatenación:", concatenar("Hola ", "mundo"))

# 10. Calcular promedio
def promedio(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma / len(lista)

print("Promedio:", promedio([4, 5, 6, 7]))

# 11. Contar vocales
def contar_vocales(cadena):
    contador = 0
    for c in cadena.lower():
        if c in 'aeiou':
            contador += 1
    return contador

print("Cantidad de vocales:", contar_vocales("Educación"))

# 12. Revertir cadena
def invertir(cadena):
    return cadena[::-1]

print("Invertida:", invertir("python"))

# 13. Tabla de multiplicar
def tabla(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

print("Tabla del 3:")
tabla(3)

# 14. Función sin parámetros
def mensaje():
    print("Primera línea")
    print("Segunda línea")
    print("Tercera línea")

mensaje()

# 15. Número más pequeño
def menor_valor(lista):
    menor = lista[0]
    for n in lista:
        if n < menor:
            menor = n
    return menor

print("Menor valor:", menor_valor([8, 3, 6, 2, 9]))

# 16. Calcular factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print("Factorial de 5:", factorial(5))

# 17. Determinar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print("¿Es primo 7?:", es_primo(7))

# 18. Repetir cadena
def repetir(cadena, n):
    return cadena * n

print("Repetido:", repetir("Hola ", 3))

# 19. Descripción con múltiples parámetros
def descripcion(nombre, edad, ciudad):
    print(nombre, "tiene", edad, "años y vive en", ciudad)

descripcion("Laura", 30, "Madrid")

# 20. Verificar palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

print("¿Es palíndromo?:", es_palindromo("Anita lava la tina"))