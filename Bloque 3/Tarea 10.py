# Función para multiplicar dos números
num1= float(input("Ingrese un numero: "))
num2= float(input("Ingrese otro numero: "))
producto= (num1*num2)

print(f"La multiplicación es :", producto)


#verifica si el numero es par o impar
def verificar_par():
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} no es par.")
verificar_par()

#funcion presentarse
def presentarse():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")
presentarse()