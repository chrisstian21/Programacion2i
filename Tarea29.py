#Sumar números ingresados por el usuario hasta que ingrese 0.
suma = 0
numero = None
while numero != 0:
    numero = int(input("Ingresa un número (0 para terminar): "))
    suma += numero
print("La suma total es:", suma)

#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
print("Generación manual del número secreto:")
intento = int(input("Ingresa un número cualquiera para generar el número secreto: "))
numero_secreto = (intento)
print("¡Adivina el número entre 1 y 100!")
intento = -1
intentos = 0
while intento != numero_secreto:
    intento = int(input("Tu intento: "))
    intentos += 1
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")

#Validar contraseña (repetir hasta que coincida con una guardada).
print("Validar contraseña: ")
contraseña = "2103"
entrada =""
while entrada != contraseña:
    entrada = input("Ingresa tu contraseña: ")
print("Contraseña correcta")

#Simular un cajero automático (menú: retirar, depositar, salir).
print("Cajero automático")
saldo = 1350
opcion = ""
while opcion != "3":
    print("1. Retirar")
    print("2. Depositar")
    print("3. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        valor = float(input("Valor a retirar: "))
        if valor <= saldo:
            saldo -= valor
            print(f"Nuevo saldo: {saldo}")
        else:
            print("Fondos insuficientes.")
    elif opcion == "2":
        valor = float(input("Valor a depositar: "))
        saldo += valor
        print(f"Nuevo saldo: {saldo}")
print("Gracias por usar nuestra red de cajeros.")

#Calcular la raíz cuadrada por aproximación (método babilónico).
valor = 20
epsilon = 0.0001
epsilon_al_cuadrado = epsilon ** 2
aprox = valor / 2
nueva_aprox = 0.5 * (aprox + valor / aprox)

while (nueva_aprox - aprox) ** 2 >= epsilon_al_cuadrado:
    aprox = nueva_aprox
    nueva_aprox = 0.5 * (aprox + valor / aprox)

print(f"La raíz cuadrada aproximada de {valor} es {nueva_aprox}")

#Contar dígitos de un número entero (ej: 456 → 3).
numero_entero = 456
temporal = numero_entero
digitos = 0

while temporal > 0:
    temporal //= 10
    digitos += 1

print(f"El número {numero_entero} tiene {digitos} dígitos.")

#Generar la secuencia de Fibonacci hasta un límite.
limite_superior = int(input("Agrega el límite: "))
x, y = 0, 1
fibonacci = [x]

while x <= limite_superior :
    x, y = y, x + y
    if x <= limite_superior:
        fibonacci.append(x)

print(f"Sucesión de Fibonacci hasta {limite_superior}:")
print(fibonacci)

#Encontrar números primos en un rango dado.
rango_inicial = 10
rango_final = 70
actual = rango_inicial

while actual <= rango_final:
    if actual > 1:
        divisor = 2
        primo = True
        while divisor * divisor <= actual:
            if actual % divisor == 0:
                primo = False
                break
            divisor += 1
        if primo:
            print(actual)
    actual += 1

#Simular un temporizador (contar regresivamente desde N).
cuenta_regresiva = int(input("Agrega un número para iniciar el conteo regresivo: "))

while cuenta_regresiva > 0:
    print(f"Tiempo restante: {cuenta_regresiva} segundos")
    cuenta_regresiva -= 1

print("Conteo regresivo finalizado")

#Leer archivos línea por línea hasta fin de archivo.
f = open("trabajo.txt", "r")
linea = f.readline()
while linea != "":
    print(linea, fin ="")
    linea = f.readline()
f.close()
print("Fin del programa")

#visualizar los 5 primero numeros
contador= 0
while contador <= 10:
    print("Numero: ", contador)
    contador += 1
