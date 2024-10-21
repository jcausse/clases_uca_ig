##############
### CICLOS ###
##############

# Las estructuras de repeticion (ciclos) son estructuras que permiten ejecutar un mismo bloque
# de codigo (su CUERPO) multiples veces, segun:
# * El valor de una condicion, que se comprobara antes de iniciar cada ciclo para determinar
#   si se debe o no realizar una nueva iteracion. Cuando la condicion es evaluad como True,
#   el cuerpo del ciclo vuelve a ejecutarse. Si no, se saltea. => Ciclos "while"
# * Un elemento iterable (es decir, algun tipo de dato que tenga sub-elementos dentro, y que para
#   cada uno de sus sub-elementos se pueda realizar una serie de operaciones) => Ciclos "for".
#   A los elementos iterables con frecuencia se los suele llamar "secuencias".

# Como norma general, cuando sabemos de antemano la cantidad de veces que vamos a ejecutar el cuerpo
# del ciclo (la cantidad de iteraciones a realizar), usamos un ciclo for. Si no conocemos cuantas
# veces vamos a iterar, utilizamos un ciclo while.
# Como siempre, hay casos que escapan a la norma general.

###########################
### Ciclos for / for-in ###
###########################

# En Python, cuando queremos realizar una operacion multiples veces sobre los elementos de un 
# iterable (lista, string, tupla, claves o valores de un diccionario, etc.), generalmente usamos 
# un ciclo for.

# Ejemplo: Imprimir todos los elementos de una lista
"""
lst = ['hola', 'buen dia', 3, 3.14, [1, 2, 3]]
for elem in lst:    # Toma los elementos, uno por uno, y los guarda en la variable elem
    print(elem)     # Imprime el elemento actualmente tomado
    x = elem * 2    # Puedo operar con el valor de elem
    print(x)
"""

# Ejemplo: Imprimir todos los caracteres de un string
"""
string = "Info. Gral. Python UCA"
for character in string:
    print(character)
"""

# Ejemplo: Dado un conjunto de lapiceras, imprimir un texto que describa a cada una
"""
conjunto_lapiceras = [
    {'marca': 'bic', 'tipo': 'roller', 'color': 'violeta'},
    {'marca': 'uniball', 'tipo': 'roller', 'color': 'amarillo'},
    {'marca': 'parker', 'tipo': 'pluma', 'color': 'auzl'},
    {'marca': 'abcd', 'tipo': 'tipo 1', 'color': 'verde'}
]

i = 1
for lapicera in conjunto_lapiceras:
    print('Lapicera {}: Es una lapicera {}, de marca {}, color {}.'.format(
        i,
        lapicera['tipo'],
        lapicera['marca'],
        lapicera['color']
    ))
    i += 1
"""

#######################
### Funcion range() ###
#######################

# La funcion range genera una secuencia de numeros enteros, contiguos (seguidos), muy similar a 
# una lista, con todos los numeros enteros entre dos valores que recibe como parametros.
"""
range(START, STOP, STEP)

range(START, STOP)

range(STOP)
"""

# START: es el valor inicial (que puede ser omitido). Este valor sera INCLUIDO en la secuencia.
#        En caso de que este valor sea omitido, el unico parametro que recibe range es el STOP, y
#        se toma el valor por default (predeterminado) de START: 0.
# STOP: es el valor final (que NO puede ser omitido). Este valor sera EXCLUIDO de la secuencia, por
#       lo que el ultimo valor de la secuencia sera STOP - 1.

# range() tambien soporta un ultimo parametro STEP, que indica de cuanto en cuanto generar la
# secuencia. Los numeros de la secuencia ya no serian contiguos, sino que tendrian una separacion.
# El STEP predeterminado es 1 (cuenta de 1 en 1: 1, 2, 3, ...).

# Ejemplo:
"""
# Imprime:
# 5 6 7 8 9
for i in range(5, 10):
    print('{} '.format(i), end='')
print() # Imprime una linea vacia al final, para que se vea mejor
"""

# Ejemplo:
"""
# Imprime:
# 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print('{} '.format(i), end='')
print() # Imprime una linea vacia al final, para que se vea mejor
"""

# Ejemplo:
"""
# Como START > STOP, se genera una secuencia vacia. No imprime nada.
for i in range(15, 10):
    print('{} '.format(i), end='')
"""

# Ejemplo:
"""
# Imprime:
# 1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58 61 64 67
for i in range(1, 70, 3): # 3 es el STEP. Cuenta de 3 en 3.
    print('{} '.format(i), end='')
print()
"""

####################
### Ciclos while ###
####################
