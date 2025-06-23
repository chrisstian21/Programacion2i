palabra_a_buscar = "algunas"

palabra_de_reemplazo = "varias"

nombre_archivo_original = "mbox3.txt"

nombre_archivo_salida = "mbox3_modificado.txt"


with open(nombre_archivo_original, "r") as entrada, \
     open(nombre_archivo_salida, "w") as salida:
    for linea in entrada:
        
        linea_modificada = linea.replace(palabra_a_buscar, palabra_de_reemplazo)

        salida.write(linea_modificada)