#encontrar el valor mayor
numero_mayor= -1
print("Antes", numero_mayor)
for el_num in [9, 41, 12, 3, 74, 15]:
    if el_num > numero_mayor:
        numero_mayor = el_num
    print(numero_mayor, el_num)
print("después", numero_mayor)