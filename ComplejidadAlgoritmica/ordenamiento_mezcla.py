import random

def ordenamiento_por_mezcla(lista):
    # Si la lista tiene más de un elemento, procedemos a dividirla
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        #Se llamada a la recursividad en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        print(f"Dividido: {izquierda} {'*' * 5} {derecha}")

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        # Mezclamos las sublistas de manera ordenada
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Copiamos los elementos restantes de la lista izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        # Se copian los elementos restantes de la lista derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f"Combinado izquierda {izquierda}, derecha {derecha}")
        print(f"Lista actual: {lista}")
        print('-' * 50)

    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('¿De qué tamaño deseas la lista?: '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print("Lista original:")
    print(lista)
    print('-' * 50)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print("Lista ordenada:")
    print(lista_ordenada)
