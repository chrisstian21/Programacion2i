# Función para multiplicar dos números
def multiplicar(x, y):
    resultado = x * y
    return resultado
print(f"La multiplicación es :", multiplicar(4,5))

num1= float(input("Ingrese un numero: "))
num2= float(input("Ingrese otro numero: "))
producto= multiplicar(num1,num2)

print(f"La multiplicación es :", producto)

# Función para verificar si un número es par

def es_par(num):
    return num %2 ==0
print("10 es par", es_par(7))
print("4 es par", es_par(4))

# Función para presentarse
def presentarse(nombre, edad):
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")
presentarse("Christian", 21)


