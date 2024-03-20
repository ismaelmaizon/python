with open("archivos\\texto_prueba.txt", encoding='utf-8') as archivo :
    
    # leemos el archivo
    contenido = archivo.read()
    
    #mostrar el contenido
    print(contenido)