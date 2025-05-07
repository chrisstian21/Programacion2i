num = 7
intentos = 3

for i in range(1, intentos + 1):
    intento = int(input(f"Intento {i} - Ingresa un número entre 1 y 10: "))

    if intento == num:
        print("¡Correcto! Adivinaste el número.")
        
    elif intento > num:
        print("Incorrecto. El número es mayor.")
    elif intento < num:
        print("Incorrecto. El número es menor.")
