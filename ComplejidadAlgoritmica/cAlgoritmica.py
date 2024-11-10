import time

def factorial(n):
    respuesta = 1
    # se utiliza un bucle while para multiplicar respuesta por cada numero desde 'n' hasta 1
    while n > 1: 
        respuesta *= n 
        n -= 1 
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    #se multiplica 'n' por el factorial de 'n-1'
    return n * factorial_r(n - 1)

# Inicializamos el programa principal
if __name__ == '__main__':
    n = 100 
    comienzo = time.time()
    factorial(n)  
    final = time.time()
    print(f"Tiempo versión iterativa: {final - comienzo}")
  
    comienzo = time.time()
    factorial_r(n)
    final = time.time()  # se registra el tiempo
    print(f"Tiempo versión recursiva: {final - comienzo}")