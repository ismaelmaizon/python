archivo_sin_leer = open("archivos\\texto_prueba.txt", encoding='utf-8') # utf-8 se usa en caso de que haga falta
#Dato: una vez que leemos el archivo no se puede volver a leer, a menos que lo cerremos



#leyendo el archivo de texto
#archivo = archivo_sin_leer.read()


# leemos todas las lineas
#linea_1 = archivo_sin_leer.readlines()
#print(linea_1)



# leemos una sola linea
#linea_2 = archivo_sin_leer.readline()
#print(linea_2)



# tambien podemos pasar parametros
linea_3 = archivo_sin_leer.readline(5)
print(linea_3)


#forma de cerrar el archivo
archivo_sin_leer.close()


# si queremos volver a usarlo, debemos volver a usar open()


archivo = open("archivos\\texto_prueba.txt", encoding='utf-8')
print(archivo.read())