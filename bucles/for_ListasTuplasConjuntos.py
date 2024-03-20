#           FOR

# iterar listas (pero tambien pueden ser tuplas)

# FOR IN

persona = ["ismael", "maizon", 200000]
print('for: ')
for dato in persona:
    print(dato)
    
numeros = [1,2,3,4,5,6,7,8,9,10]

# mostrando la tabla del 2 hasta el 10
for num in numeros:
    resul = num * 2
    print(f' {num} multiplicado por 2: {resul} ')



# iterando sobre 2 listas (al mismo tiempo), pueden ser mas de 2 listas
# (es importante que las listas tengan la misma cantidad de elementos)
# AMBAS LISTAS SE RECORREN AL MISMO TIEMPO, NO UNA PRIMERO Y LA OTRA DESPUES
lista1 = [1,2,3,4]
animal = ['perro', 'gato', 'chancho', 'pajaro']

for lis, ani in zip(lista1, animal):
    print(f' recorriendo lista1 : {lis}')
    print(f' recorriendo animal : {ani}')


# RANGE()
# Establecer parametro o rango de trabajo
for num in range(5, 10):
    print(num)
# excluye el ultimo valor
for num in range(10):
    print(num)

# forma NO optima de recorrer una lista por su indice
for num in range(len(numeros)):
    print(f'indice: {num}, valor: {numeros[num]}')

# forma optima de recorrer una lista por su indice
# "num" en este caso es una tupla, num = (indice, valor)
for num in enumerate(numeros):
    print(num)
    indice = num[0]
    valor = num[1]
    print(f'indice: {indice}, valor: {valor}')




# FOR IN ELSE
for num in enumerate(numeros):
    print(num)
    indice = num[0]
    valor = num[1]
    print(f'indice: {indice}, valor: {valor}')
else:
    print('termino el bucle')


#               CONJUNTOS

#  Los conjuntos se iteran igual
# excepto que no funciona esto en los conjuntos

# forma NO optima de recorrer una lista por su indice
for num in range(len(numeros)):
    print(f'indice: {num}, valor: {numeros[num]}')
    
    
    
    
# ejemplos


frutas = ['pera', 'manzana', 'flan' ,'ciruela', 'sandia', 'uva']


#eviat que se coma el flan con CONTINUE
for fruta in frutas:
    if fruta == 'flan':
        continue
    print(f'me voy a comer una {fruta}')
    
#evitar que el bucke siga ejecutandose (si tenemos un else, tampoco se ejecuta)
for fruta in frutas:
    print(f'me voy a comer una {fruta}')
    if fruta == 'manzana':
        break

print('bucle terminado')


#recorrer una cadena de texto
texto = 'ismaelMaizon'
for l in texto:
    print(l)
    
#for en una sola linea de codigo
num = [2,3,4]
numeros_duplicado = [ x*2 for x in num ]
print(numeros_duplicado)
numeros_mitad = [ x/2 for x in num ]
print(numeros_mitad)
numeros_cuadrado = [ x**2 for x in num ]
print(numeros_cuadrado)
    
