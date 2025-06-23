# el enunciadod continue termina la iteracion actual y salta a la parte superior del bucle
while True:
    line=input("Ingrese un cáracter: ")
    if line[0]=="5":
        continue
    if line == "terminado":
        break 
    print(line)
    print("terminado")


for i in [5,4,3,2,1]:
    print(i)
print("texto")