import os

def crear_archivo():
    i = 1
    while True:
        nombre = f"Archivo{i}.txt"
        if not os.path.exists(nombre):
            with open(nombre, "w") as archivo:
                print(f"Archivo creado correctamente.")
            break
        i += 1

def nuevo_archivo():
    nombre = input("Introduce el nombre del archivo: ")
    if not nombre.endswith(".txt"):
        nombre += ".txt"
    if not os.path.exists(nombre):
        with open(nombre, "w") as archivo:
            print(f"Archivo '{nombre}' creado correctamente.")
    else:
        print("El archivo ya existe.")

def eliminar_archivo(nombre):
    try:
        os.remove(nombre)
        print(f"Archivo '{nombre}' eliminado correctamente.")
    except FileNotFoundError:
        print("El archivo no existe.")

def escribir_archivo(nombre):
    texto = input("Escribe el texto que deseas guardar: ")
    with open(nombre, "a") as archivo:
        archivo.write(texto + "\n")
    print(f"Texto escrito en '{nombre}' correctamente.")

def menu():
    while True:
        print("\nMenú de archivos:")
        print("1: Crear archivo consecutivo")
        print("2: Nuevo archivo (nombre personalizado)")
        print("3: Escribir en archivo")
        print("4: Eliminar archivo")
        print("5: Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            nuevo_archivo()
        elif opcion == "3":
            nombre = input("Introduce el nombre del archivo: ")
            escribir_archivo(nombre)
        elif opcion == "4":
            nombre = input("Introduce el nombre del archivo a eliminar: ")
            eliminar_archivo(nombre)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()