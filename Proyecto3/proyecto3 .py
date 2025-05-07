#tabla de multiplicar personalizada
#1.pide al usuario un numero entre el 1 y el 12 
#2.imprime la tabla de multiplicar de ese numero ,desde 1 hasta el 12
print("ingrese un numero entre el 1 y el 12")
numero = int(input("ingrese un numero: "))
for i in range(1,13):
    print(numero,"x",i,"=",numero*i)
print("Esta es tu tabla de multiplicar")
