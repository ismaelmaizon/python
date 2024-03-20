with open("archivos\\texto_prueba.txt", 'a', encoding='utf-8') as archivo :
    
    # agregar al archivo
    # agregando 5 lineas
    archivo.write('\n')
    for i in range(5):
        archivo.write(f'Linea {i} agregada \n')
    
    