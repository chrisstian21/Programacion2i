
# Promedio de notas
print("ESTE PROGRAMA ME CALCULA EL PRMEDIO DE 3 NOTAS INGRESADAS POR EL USUARIO")
def calcular_promedio():
    nota1 = float(input("Ingrese la Nota 1 de 0 a 10: "))
    nota2 = float(input("Ingrese la Nota 2 de 0 a 10: "))
    nota3 = float(input("Ingrese la Nota 3 de 0 a 10: "))

    promedio = (nota1 + nota2 + nota3) / 3
  

    if promedio < 5:
        estado = "Reprobado"
    elif promedio >= 5.1  and  promedio < 6.99:
        estado = "Regular"
    elif promedio >=7 and promedio < 8.99:
        estado = "Buena"
    else:
        estado = "Excelente"

    print(f"\n El Promedio del estudiante es:  {promedio}")
    print(f"\n El estudiante se encuentra en un estado: {estado}")
calcular_promedio()