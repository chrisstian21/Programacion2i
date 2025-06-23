#Romper un bucle
#termina el bucle actual y salta al enunciado que le sigue inmediatamente aal bucle

while True:
    linea= input("adivina un numero: ")
    if linea == "5":
        break
    print(linea)
    print("Intenta otra vez")