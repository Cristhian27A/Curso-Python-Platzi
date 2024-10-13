to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
#para saber cuantos elementos hay en una lista se usa la funcion "len"
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento:", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento:", string[-1])
print(mix[2:-2])
print(mix)
# se usa "append" para anadir elementos al final
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
# para insertar elementos en una posicion especifica
mix.insert(1,["a","b"])
print(mix)
# para encontrar la aparicion de un elemento "index"
# encontrar mayor elemento "max" y menor elemento "min"
# para eliminar un elemento "del"