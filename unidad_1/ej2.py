first_name = input('Ingrese su nombre: ')   # first_name es una variable
                                            # llamo a la funcion input() me permite ingresar datos
                                            # por teclado, le digo al usuario 'Ingrese su nombre: '
                                            # el usuario ingresa el nombre (texto), oprime Enter, y
                                            # lo que ingreso se guarda en la variable first_name
last_name = input('Ingrese su apellido: ')  # Lo mismo con el apellido (last_name)

print('Hola {} {}!'.format(last_name, first_name))

# Funcion print():
# * Recibe una cantidad variable de argumentos (separados por coma) que pueden ser de distintos tipos:
#   str, int, float, bool, ... Ejemplos:

#print('Agus Fraga') # 1 solo argumento, un string, que dice 'Agus Fraga'
#print('Agus', 'Fraga') # 2 argumentos, 2 strings, que dicen 'Agus' el primero, y 'Fraga' el segundo.

# * Imprime los argumentos que recibe, uno por uno, en el orden en el que los recibe.
# * De manera predeterminada, el separador de argumentos es un espacio. Puedo cambiar este
#   comportamiento pasandole el argumento especial sep. Ejemplo:

# print('Agus', 'Fraga') # Imprime 'Agus Fraga'
# print('Agus', 'Fraga', sep=' ') # Imprime 'Agus Fraga' (el espacio es el sep predeterminado)
# print('Agus', 'Fraga', sep=', ') # Imprime 'Agus, Fraga'
# print('Agus', 'Fraga', sep=',') # Imprime 'Agus,Fraga'
# print('Agus', 'Fraga', 'Python', 'UCA', sep='%') # Imprime 'Agus%Fraga%Python%UCA'

# * De manera predeterminada, al final se imprime un salto de linea (\n). Puedo cambiar este
#   comportamiento pasandole el argumento especial end. Ejemplo:

# print('Python1') # Imprime 'Python1' y salta a la linea de abajo
# print('Python2', end='\n') # Imprime 'Python2' y salta a la linea de abajo ('\n' es el end default)
# print('Python3', end='*') # Imprime 'Python*' y NO salta de linea
# print('Agus', 'Fraga', 'Python4', end='&') # Imprime 'Agus Fraga Python&' y NO salta de linea
# print('Agus', 'Fraga', 'Python5', end='&') # Imprime 'Agus Fraga Python&' y NO salta de linea
# print() # Salto de linea

# Puedo combinar sep y end:

# print('Agus', 'Fraga', 27, 'UCA', 3.5, 'Python', sep='hola', end='()\n\n')
# print('Buen dia', end='')   # Al poner un string vacio, no imprime NADA de end, y NO salta de linea
# print('Buenas', end='')
# print('Hoy es', end='')
# print('6 de octubre')

# Format:
# Format se usa para darle formato a un string, y es un modo muy comodo de imprimir informacion guardada
# en variables sin volvernos locos con el sep y el end. 
# Ademas permite dar formato a los distintos tipos (imprimir numeros con una determinada cantidad de decimales, o
# rellenando con ceros para que todos tengan la misma longitud, etc.)
# Ejemplo:

# codigo_postal = 1234
# calle = 'Evergreen Terrace'
# altura = 742
# ciudad = 'Springfield'
# pais = 'USA'
# direccion = '{} {}, {} {}, {}'.format(altura, calle, codigo_postal, ciudad, pais)
# print(direccion)