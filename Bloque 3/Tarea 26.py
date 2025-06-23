man_a = open('mbox.txt')
for linea in man_a:
    linea = linea.rstrip()
    if linea.startswith('From:') :
        print(linea)