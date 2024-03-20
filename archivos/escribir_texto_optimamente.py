with open("archivos\\texto_prueba.txt", 'w', encoding='utf-8') as archivo :
    
    # sobreEscribiendo el archivo
    # archivo.write('hola isma, como estas?')
    archivo.writelines(['hola isma, como estas?\n', 'donde estas?'])
    