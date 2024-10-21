### CICLOS ###

# Las estructuras de repeticion (ciclos) son estructuras que permiten ejecutar un mismo bloque
# de codigo (su CUERPO) multiples veces, segun:
# * el valor de una condicion, que se comprobara antes de iniciar cada ciclo para determinar
#   si se debe o no realizar una nueva iteracion => Ciclos "while"
# * un elemento iterable (es decir, algun tipo de dato que tenga sub-elementos dentro, y que para
#   cada uno de sus sub-elementos se pueda realizar una serie de operaciones) => Ciclos "for".

# Como norma general, cuando sabemos de antemano la cantidad de veces que vamos a ejecutar el cuerpo
# del ciclo (la cantidad de iteraciones a realizar), usamos un ciclo for. Si no conocemos cuantas
# veces vamos a iterar, utilizamos un ciclo while.
# Como siempre, hay casos que escapan a la norma general.

### Ciclos for / for-in ###

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

VER INDICES
VER WHILE
