for i in range(1,11):
    print(i)

# este iterador lo podemos manipular de forma manual cuando se ejecuta
my_iter = iter(range(1,4))
print(my_iter)
print(next(my_iter))#generar iteraciones manualmente con la palabra next
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) #tener en cuenta hasta que punto iterar 
#de lo contrario ir mas alla de las interaciones generara un stopiteration