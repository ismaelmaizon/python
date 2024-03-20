tupla = ("ismael", "maizon", 200000)
lista = ["ismael", "maizon", 200000]


#                   Desempaquetamiento

#se puede hacer tanto con tuplas con lista, dato importante es que hay que crear una variable por cada valor que tenga
#la tupla o la lista, no se puede crear de menos o de mas variables
nombreT, apellidoT, numT = tupla
nombreL, apellidoL, numL = lista
print( nombreT, apellidoT, numT )

# Otra forma de crear tupla
tupla2 = tuple(['dato1', 'dato2']) #con tuple
tupla2 = 'dato1', 'dato2' # sin parentecis

# las tuplas ocupan menos espacio de memoria que las listas, dado que las tuplas no son modificables
# es recomendable usar tuplas para vasibles que sabemos que no se van a modificar



#                       Conjunto


#crear un conjunto con set()
conjunto = set(["Dato 1", "Dato 2"])
print(conjunto)

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = { conjunto1, 'dato 3' }
print(conjunto2)

# subConjunto y superConjunto
conjunto3 = {1,2,3,4,5}
conjunto4 = {1,2,3}
conjunto5 = {9,8,7}

# subConjunto
result1 = conjunto4.issubset(conjunto3)
print(result1)  
# superConjunto
result2 = conjunto3.issuperset(conjunto4)
print(result2)

#verifiacar si hay algun numero en comun
result3 = conjunto4.isdisjoint(conjunto3)
print(result3) #con solo hacer un numero en comun, es suficiente para que devuelva False

result4 = conjunto5.isdisjoint(conjunto3)
print(result4)


#           Diccionario

#diccionario dict()
diccionario = dict(nombre="ismael", apellido = "maizon")
print('diccionario: ')
print(diccionario)

#creando diccionario con fromkeys(), te crear las keys con valores None
diccionario = dict.fromkeys(['nombre', 'apellido', 'direccion'])
#creando diccionario con fromkeys(), cambiando el valor por defecto por "no se"
diccionario = dict.fromkeys(['nombre', 'apellido', 'direccion'], "no se")



print(diccionario)



