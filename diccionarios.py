diccionario ={
    "nombre": "ismael",
    "apellido": "maizon",
    "cel": 3516628
}

print(diccionario)

# Keys()
# devuelve las claves(en una lista), tambien nos sirve para iterar

element = diccionario.keys()

print(element)


# Get()
# nos trae el elmento que requerimos (si no encuentra nada, el programa continua y me devuelve none)
nombre = diccionario.get('nombre')
print(nombre)

# Items()
# obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)


# Pop()
# eliminando un elemento del diccionario

diccionario.pop('nombre')
print(diccionario)


# Clear()
# Eliminando todo del diccionario
diccionario.clear()

print(diccionario)

