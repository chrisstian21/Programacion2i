#1.solicita al usuario su nombre y su año de nacimiento
#2.calcula su edad aproximada en 2025
#3.muestra un mensaje personalizado como: hola juan, tienes aproximadamente 20 años
#4.si la persona es mayor de adad (18 o mas) muestra : eres mayor de edad si no muestra: eres menor de edad
nombre = input("Ingrese su nombre: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2025 - año_nacimiento
print(f"Hola {nombre}, tienes aproximadamente {edad} años.")
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


