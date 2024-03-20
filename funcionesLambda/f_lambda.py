numeros = [1,2,3,4,5,6,8,20,54,82,100]

# es como la funcion flecha en javascript


multiplicar_por_dos = lambda x : x*2


print(multiplicar_por_dos(5))


# filter()
# ejecuta cada uno de los valores de un iterable
numeros_pares = filter(lambda numero : numero%2 == 0, numeros)
print(list(numeros_pares))