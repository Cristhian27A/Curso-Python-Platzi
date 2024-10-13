
with open('./text.txt', 'w+') as file: #para leer y escribir
    #con 'w+' vamos a tener permiso de leer y escritura, pero se sobreescribe todo el archivo
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo\n')
    file.write('otra linea\n')
    file.write('mas linea\n')