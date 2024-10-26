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

# Ejemplo: Imprimir todos los caracteres de un string
"""
string = "Info. Gral. Python UCA"
for character in string:
    print(character)
"""

# Ejemplo mas avanzado: Imprimir todos los elementos de una lista
"""
lst = ['hola', 'buen dia', 3, 3.14, [1, 2, 3]]
for elem in lst:    # Toma los elementos, uno por uno, y los guarda en la variable elem
    print(elem)     # Imprime el elemento actualmente tomado
    x = elem * 2    # Puedo operar con el valor de elem
    print(x)
"""

# Ejemplo mas avanzado: Dado un conjunto de lapiceras, imprimir un texto que describa a cada una
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

# El ciclo while nos permite ejecutar un bloque de codigo, su CUERPO, una cantidad indefinida
# de veces dependiendo de una CONDICION. Tambien es muy util (igual que for-in-range) cuando
# queremos realizar iteraciones teniendo en consideracion los indices de una secuencia (lista,
# tupla, string, etc.)

# Ejemplo:
# Supongamos que queremos pedir a un usuario que ingrese un numero par positivo, y queremos
# validar el numero ingresado, de manera que si el mismo ingresa un numero impar o un numero
# negativo, la entrada sea rechazada y se le vuelva a pedir otro numero. Esto no podriamos,
# en principio, hacerlo con un ciclo for-in, debido a que:
# * No tenemos un elemento iterable que recorrer, sino que el ciclo que vamos a escribir
#   estara basado en una CONDICION.
# * No tenemos forma de conocer cuantas veces se va a ejecutar el ciclo (no podemos predecir
#   cuantas veces puede equivocarse el usuario).
"""
def get_even_number():
    done = False        # Flag de que el ingreso es valido
    while not done:     # Mientras el flag no este en True
        num = int(input('Ingrese un numero par positivo: '))
        if num > 0 and num % 2 == 0:    # Si cumple todas las condiciones
            done = True                 # Marco que la entrada fue valida, lo que hace que
                                        # pueda salir del ciclo
        else:                           # Si no cumple ALGUNA de las condiciones (and)
            print('El numero {} es invalido.'.format(num)) # Muestro un mensaje de error

    return num  # El ciclo while anterior me ASEGURA que, si llego hasta aca, "num" es valido

x = get_even_number()
print(x)
"""

# Ejemplo:
# Desarrollar la funcion index(s, c) que devuelva el indice de la primera aparicion del 
# caracter "c" en el string "s". Si "c" no esta en "s", debera devolver -1.

# La mejor solucion usando for-in-range es la siguiente:
"""
def index_ineficiente(s, c):
    ret = -1
    found = False
    for i in range(len(s)):
        # return i  ---> Seria lo ideal, pero no se nos permite usar mas de un return :(
        if not found and s[i] == c:
            found = True
            ret = i
    return ret
"""
# Esto es muy ineficiente, porque una vez encontrada la primera coincidencia de "c" en "s", 
# sigue recorriendo el string, lo que podria evitarse (retornar justo cuando se encuentra 
# la primera coincidencia).
# Recordar que en Informatica General UCA NO PODEMOS:
# * Usar mas de un return por funcion
# * Usar break para romper ciclos
# * Usar continue
# Debido a estas limitaciones, no hay una forma eficiente y a la vez permitida de resolver este problema
# usando for. Lo haremos usando while:
"""
def index(s, c):
    i = 0               # Indice para recorrer el string
    ret = -1            # Valor de retorno (si "c" no esta en "s", "ret = i" no se ejecuta, y devolvemos -1)
    found = False       # Flag que me permite cortar el ciclo cuando encuentre la primera aparicion de "c" en "s"
    while not found and i < len(s):
        if s[i] == c:   # Cuando encuentro la aparicion
            ret = i     # Me guardo el indice (sobreescribo ret)
            found = True    # Seteo el flag
        i += 1
    return ret          # Devuelve el indice (si ret fue sobreescrito), o -1

print(index('hola', 'l'))                   # 2
print(index('hola buenos dias ', ' '))      # 4
print(index('buenos dias', 'w'))            # -1
"""

# Ejemplo:
# Escribir una funcion que permita decidir si un numero es o no primo
# Una primera version podria ser:
"""
def es_primo_1(n):
    primo = True            # Flag para cortar el ciclo cuando se encuentre un divisor
    i = 2                   # Empezando en 2, vamos a buscar divisores
    while primo and i <= n // 2:  # Puede cortar porque i > n // 2, o porque primo es False
        if n % i == 0:
            primo = False
        i += 1
    return primo
"""
# Mas eficiente: se ha demostrado que, en lugar de buscar divisores hasta la mitad del numero,
# lo podemos hacer hasta su raiz cuadrada
"""
def es_primo_2(n):
    primo = True            # Flag para cortar el ciclo cuando se encuentre un divisor
    i = 2                   # Empezando en 2, vamos a buscar divisores
    while primo and i <= int(n ** 0.5):  # Puede cortar porque i > n // 2, o porque primo es False
        if n % i == 0:
            primo = False
        i += 1
    return primo
"""
