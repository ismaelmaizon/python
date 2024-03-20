diccionario ={
    "nombre": "ismael",
    "apellido": "maizon",
    "cel": 3516628
}

# recorremos diccionario para obtener las claves
# el parametro key puede llamarse la forma que uno prefiera
for key in diccionario:
    print(key)
 
# recorremos diccionario con items() para obtener las claves y los valores    
for datos in diccionario.items():
    print(datos) # ahora es una tupla con dos valores
    key = datos[0]
    value = datos[1]
    print(f' key: {key}, value: {value} ')
    
    
    
