import math
#Se define una funcion que va a retorna 1 en notación Big-O
def num(n):
    return 1
#luego defino una funcion que retorna el logaritmo base 10 de 'n'
def logarithm(n):
    return math.log10(n)

def lineal(n):
    return n

#Se define una funcion que va a retornar 'n * log10(n)
def n_logarithm(n):
    return n * math.log10(n)

#Esta funcion va a retornar una cuadratica
def square(n):
    return n ** 2

#esta una funcion que retorna 2^n
def exponential(n):
    return 2 ** n

#Se inicia el programa
if __name__ == "__main__":
    #Y se crea una lista con diferentes valores de n para que podamos evaluar
    n = [10, 100, 1000, 1000]
    
    #Luego se va a iterar sobre la lista 'n' para probar cada funcion con los diferentes valores
    for i in range(len(n)):
        print(f"\nResultados para n = {n[i]}:")
        
        print(f"num({n[i]}) = {num(n[i])}")
        print(f"logarithm({n[i]}) = {logarithm(n[i])}")
        print(f"lineal({n[i]}) = {lineal(n[i])}")
        print(f"n_logarithm({n[i]}) = {n_logarithm(n[i])}")
        print(f"square({n[i]}) = {square(n[i])}")
        print(f"exponential({n[i]}) = {exponential(n[i])}")
