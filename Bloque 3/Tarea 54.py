total_puntuaciones = 0
contador_personas = 0

with open("mbox2.txt", "r") as f:
    encabezado = f.readline() 
    for linea in f:
        datos = linea.strip().split(',')
        if len(datos) == 3:  
            try:
                puntuacion = int(datos[2])
                total_puntuaciones += puntuacion
                contador_personas += 1
            except ValueError:
                print(f"Advertencia: Puntuación no numérica en la línea: {linea.strip()}")

if contador_personas > 0:
    promedio = total_puntuaciones / contador_personas
    print(f"El promedio de puntuación es: {promedio:.2f}")
else:
    print("No se encontraron puntuaciones válidas.")