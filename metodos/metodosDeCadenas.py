cadena1 = 'hola isma, hola'
cadena2 = 'comodasddfdfe'

# metodo que convierte todo en mayusculas
mayus = cadena1.upper() 
# metodo que convierte todo en minusculas
minus = cadena1.lower()
# metodo que convierte la primer letra en Mayuscula y deja el resto el minuscula
primer_letr_mayus = cadena1.capitalize()


# buscar una cadena en otra cadena, si no encuentra nada devuelve -1
busqueda_find = cadena1.find('isma') 
# buscar una cadena en otra cadena, si no encuentra nada devuelve una excepcion
busqueda_index = cadena1.index('m') 


# buscar una cadena, si es numerico devuelve true, si no lo es, devuelve false
es_numerico = cadena1.isnumeric()
# buscar una cadena, si es Alfanumero devuelve true, si no lo es, devuelve false
es_alfanumerico = cadena2.isalpha()


# buscar una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena2.count('f')
contar_coincidencias = cadena1.count('hola') # cuenta el texto tal cual como lo pasamos


# contamos cantidad de caracteres de una cadena
cantidad = len(cadena2)


# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True, caso contrario de vuelve False
empieza_con = cadena1.startswith('hol')
# verificamos si una cadena termina con otra cadena dada, si es asi devuelve True, caso contrario de vuelve False
termina_con = cadena1.endswith('la')


# si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace('ma', 'lu')

#separar cadenas con la cadena que le pasamos
cadena_separada = cadena1.split(",")

print( cadena_separada)


