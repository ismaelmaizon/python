
# importando el modulo
import modulo_saludar 
saludo = modulo_saludar.saludar('isma')
print(saludo)


# importando el modulo y cambiando el nombre
import modulo_saludar as ms
saludo = ms.saludar('isma')
print(saludo)


# importando el modulo y funcion en particular
from modulo_saludar import saludar
saludo = saludar('isma')
print(saludo)


# importando el modulo y funcion en particular, tambien podemos cambiar el nombre
from modulo_saludar import saludar as sr
saludo = sr('isma')
print(saludo)

# si usamos "as" sirve para cambiar o asignar una forma de 
# llamar el modulo (suele ser que hay modulos que no son tan representativos o son muy largos)


#para ver propiedades y metodos del namespace
print(dir(modulo_saludar))


#accedemos al nombre de este modulo
print(__name__)



# El módulo sys proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete de Python y a 
# funciones que interactúan fuertemente con el intérprete.
import sys  

#La variable sys.path es una lista que contiene ubicaciones de directorios donde Python busca 
# módulos y paquetes. Esto incluye directorios locales (el directorio actual), directorios de paquetes 
# instalados globalmente y directorios definidos por el usuario. Es útil para ver qué directorios están 
# incluidos en la ruta de búsqueda de Python y puede ser útil para diagnosticar problemas de importación de módulos.
print(sys.path)


#Por ejemplo, si ejecutas print(sys.path) y ves que un directorio necesario no está incluido en la lista, 
# podrías agregarlo a sys.path para que Python pueda encontrar los módulos que necesitas importar desde ese directorio.

# Agregar el directorio deseado a sys.path
sys.path.append('/ruta/a/directorio')