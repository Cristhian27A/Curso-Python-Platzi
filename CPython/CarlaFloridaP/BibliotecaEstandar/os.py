import os

#Obtener el directorio actual
"""cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)"""

#Vamos a listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')] #('.') para especificar directorio actual
print("Archivos txt: ", txt_files)

#Renombrar archivo
os.rename('holaMundo.txt', 'cuento.txt')
print('Archivo renombrado')

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)