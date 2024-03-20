lista = [1,2,3,5,8,9]

#Enocntradno el numero mayor de una lista
num_mayor = max(lista)

#Enocntradno el numero menor de una lista
num_menor = min(lista)


#redondenado a 6 decimales

numero = round(12.2565834, 6)
print(numero)

#suma toda los elementos de una iterable
suma_total = sum(lista)
print(suma_total)


# filter()
# ejecuta cada uno de los valores de un iterable
numeros_pares = filter(lambda numero : numero%2 == 0, lista)
print(list(numeros_pares))