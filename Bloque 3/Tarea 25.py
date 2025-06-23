man_a = open('mbox.txt')
for linea in man_a:
    if linea.startswith('From:') :
        print(linea)