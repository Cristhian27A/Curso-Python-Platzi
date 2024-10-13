import os

# Se cambia el directorio de trabajo
os.chdir('c:/Users/USUARIO/OneDrive/Documentos/CPython/Carla Florida - Curso de python/Lectura y escritura de archivos')

#leer un archivo linea por linea
"""with open('relojero.txt', 'r') as file: # Con esto se puede usar solo el nombre del archivo
    for lineas in file:
        print(lineas.strip())"""

#leer todas la lineas en una lista
"""with open('relojero.txt', 'r') as file:
  lineas = file.readlines()
  print(lineas)"""

#añadir texto
"""with open('relojero.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""

#Sobreescribir el texto
"""with open('relojero.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")"""

#Leer cuantas lineas de texto tengo
with open('relojero.txt', 'r') as file:
    lineas = file.readlines()
    print(len(lineas))
