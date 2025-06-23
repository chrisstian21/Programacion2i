import os

if os.path.exists("mbox.txt"):
    os.remove("mbox.txt")
    print("Archivo eliminado.")
else:
    print("El archivo no existe.")