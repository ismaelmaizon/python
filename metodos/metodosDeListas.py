lista = [2, 5, 'p', True, False]
lista2 = [2, 5,9, 7,25, True, False]


# Devuelve cantidad de elementos de la lista
cont = len(lista)



# agregando elemeto a la lista con append
lista.append('jajaj')
# agregando elemeto a la lista en un indice especifico
lista.insert( 2 ,'jajaj')
# agregamos una lista a otra lista
lista.extend([False, 2000, 'rio'])

print(lista)

# eliminando un elemento de la lista, indicando el indice del elemento
lista.pop(0) # para elminar el ultimo y no sabemos su indice, simplemento ponemos -1
# removiendo un elemento de la lista por su valor
lista.remove(False) #elimina el primero que encuentra
# elimina todos los elementos de la lista
#lista.clear()

# ordena los elementos en forma acendente, es necesario que la misma sea solo numeros
lista2.sort()
lista2.sort(reverse=True)
# revierte el orden de la lista
lista.reverse()

print(lista)
print(lista2)
