#Calculadora de promedio de calificaciones
#1. Pedir el nombre al estudiante
#2. Solicita 4 calificaciones (numeros enteros entre 0 y 20)
#3. Calcula el promedio de las 4 calificaciones.
#4. Muestra un mensaje como: "Juan tu promedio es 16. Felicitaciones"
#5. Si el promedio es menor a 14 muestra: "Lo siento Juan, estas reprobado"
nombre = input("Ingrese su nombre: ")
calificacion1 = int(input("Ingrese su primera calificacion: "))
calificacion2 = int(input("Ingrese su segunda calificacion: "))
calificacion3 = int(input("Ingrese su tercera calificacion: "))
calificacion4 = int(input("Ingrese su cuarta calificacion: "))
promedio = (calificacion1+calificacion2+calificacion3+calificacion4)/4
print(nombre,"Tu promedio es: ",promedio)
if promedio >= 14:
    print("Felicitaciones",nombre, "estas aprobado")
else: 
    print("Lo siento",nombre,"estas reprobado.")
print("Este es tu promedio")