#################
### VARIABLES ###
#################

# Podemos pensar a las variables como "cajas" que contienen adentro un valor, y reciben un nombre.
# Si nosotros organizamos la casa para una mudanza, las distintas cosas a mudar las voy a guardar en
# distintas cajas, con distintas etiquetas, y dentro van a contener cosas de distintos tipos.

### Anatomia de una variable ###

# <variable> = <valor>

# Definir una variable en Python es dar por primera vez el nombre de una variable y asignarle un valor
# Ejemplo:

x = 35      # Aca la estamos definiendo porque nunca antes aparecio

# Asignar una variable en Python es cambiar el valor de una variable que ya estaba declarada
# Ejemplo:

x = 17      # Aca la estamos asignando porque ya aparecia antes y le cambiamos el valor

# Acceder a una variable es utilizar su nombre en reemplazo del valor que la variable contiene en ESE momento (recordar que
# la ejecucion del programa es SECUENCIAL, es decir, se ejecuta una linea despues de otra). Esto lo hago para, por ejemplo:
#   1. Imprimir el valor de una variable

print(x)    # Imprime 17

#   2. Definir otra variable con el valor actual de una variable ya definida anteriormente

y = x       # Estoy definiendo (porque no aparecio antes) una variable y que esta COPIANDO EL VALOR de x

print(y)    # Imprime 17

x = 14      # Cambia el valor de x pero NO el de y

print(x)    # Imprime 14

print(y)    # Imprime 17

#       NOTA: Esto mismo sucede siempre que yo quiero crear una variable a partir de otra, excepto cuando la variable original
#             es una lista. Esto lo vemos (mucho) mas adelante en la materia.

######################
### TIPOS DE DATOS ###
######################

### int ###

# Si nosotros queremos modelar la cantidad de personas que hay en una habitacion, dicha cantidad deberia ser un entero positivo
# - no puedo tener menos de 0 personas
# - no puedo tener media persona

# Imaginemos que una empresa publica un articulo (iPhone 16) en su web como que siempre hay stock, pero en realidad no tiene
# fisicamente los telefonos, sino que, como entregan 1 vez por semana, cada viernes compran todos los telefonos y los distribuyen
# Ahora bien, a veces, algunas compras se cancelan, y los telefonos ya comprados no son entregados (porque el cliente cancelo la
# compra) y quedan en deposito.
# Si queremos modelar la cantidad de iPhones en stock al final de cada semana (el viernes), dicha cantidad deberia ser un entero
# que puede ser tanto positivo como negativo
# - si es positivo, se cancelaron compras de la semana anterior, y quedaron en stock
# - si es negativo, se ordenaron para esa semana mas de los que habia en deposito, y hay que comprar nuevos
# - si es cero, no se vendio nada esa semana y no tenia remanentes de la semana anterior, o las ventas de esa semana fueron iguales
#   a los remanentes
# - no puedo tener medio telefono

# TODAS LAS SITUACIONES DONDE DEBO MODELAR DATOS QUE SON ENTEROS => el tipo de dato que usamos es int. Permite tanto enteros
# positivos como negativos.

### float ###

# Si quiero modelar la cantidad de dinero que tengo en una cuenta de banco que permite un descubierto, el dato deberia poder ser
# tanto positivo como negativo y soportar decimales

# TODAS LAS SITUACIONES DONDE DEBO MODELAR DATOS QUE SON NUMEROS REALES => el tipo de dato que usamos es float. 
# Permite tanto fraccionarios positivos como negativos.

### bool ###

# Si quiero modelar un valor de verdad (como en el ejemplo anterior del banco, quiero modelar si un usuario del banco tiene
# o no deuda). Un usuario tiene deuda si su saldo es menor que cero, y no tiene deuda si es >= que cero.
# Hay dos valores posibles:
# - tiene deuda (True)
# - no tiene deuda (False)
# El tipo de dato que modela estas situaciones es bool, y tiene como valores posibles True o False

# Ejemplo:

saldo = -15.3
tiene_deuda = saldo < 0     # saldo < 0 es una COMPARACION, y toda comparacion devuelve un valor de tipo bool
                            # como saldo es menor que cero, la comparacion saldo < 0 resulta verdadera, y su resultado (True)
                            # se asigna a la variable tiene_deuda

print(tiene_deuda)

### str ###

# Si quiero modelar el nombre de una persona, utilizo el tipo de dato string (cadena), que es una cadena de texto.
# Las cadenas de texto son una coleccion ordenada de caracteres, uno detras del otro, donde cada caracter, en Python, se modela 
# mediante un estandar que se llama UTF-8.
# Como UTF-8 es un estandar muy grande, utilizamos otro estandar (que es anterior a UTF-8), que es el estandar ASCII. Como
# UTF-8 fue diseñado para ser retrocompatible con ASCII, todos los caracteres de ASCII son parte del estandar UTF-8 (pero no
# vale la vuelta).
# El estandar ASCII lista todos los caracteres del alfabeto ingles (US-ASCII), y les asigna un valor numerico a cada uno.
# Esos valores estan en la tabla ASCII:
# https://media.geeksforgeeks.org/wp-content/uploads/20240304094301/ASCII-Table.png

# Ahora bien, como los digitos tambien son parte de ASCII, el numero 327 lo podriamos representar de mas de una forma:

x_int = 327     # De tipo int
x_str = '327'   # De tipo str

# Cuando representamos numeros en formato de strings, las operaciones definidas son las de strings

print('123' + '4')  # Imprime '1234' en lugar de 127

# Para realizar conversiones de strings que pueden representar datos numericos, usamos:
# int() para convertir a int
# float() para convertir a float, donde el separador decimal TIENE que ser un punto (no coma)

print(int('123') + 4)   # Imprime 127

###############
### CASTEOS ###
###############

# Cuando quiero convertir un valor de un tipo de dato a otro, se usa un cast

# 1. Casteo de float a int => Se queda con la parte entera y pierde los decimales
x = 1327.8
print(type(x))  # Imprime: <class 'float'>

y = int(x)
print(type(y))  # Imprime: <class 'int'>
print(y)        # Imprime: 1327

# 2. Casteo de int a float => Agrega .0 como parte decimal
x = 1327
print(type(x))  # Imprime: <class 'int'>

y = float(x)
print(type(y))  # Imprime: <class 'float'>
print(y)        # Imprime: 1327.0

# 3. Casteo de bool a int => True se convierte a 1, y False se convierte a 0
x = True
print(type(x))  # Imprime: <class 'bool'>

y = int(x)
print(type(y))  # Imprime: <class 'int'>
print(y)        # Imprime: 1

x = False
print(type(x))  # Imprime: <class 'bool'>

y = int(x)
print(type(y))  # Imprime: <class 'int'>
print(y)        # Imprime: 1

# 4. Casteo de int a bool => 0 se convierte en False, cualquier valor distinto de 0, en True,
#    incluso si es negativo
x = 0
print(type(x))  # Imprime: <class 'int'>

y = bool(x)
print(type(y))  # Imprime: <class 'bool'>
print(y)        # Imprime: False

x = 1
print(type(x))  # Imprime: <class 'int'>

y = bool(x)
print(type(y))  # Imprime: <class 'bool'>
print(y)        # Imprime: True

x = -17
print(type(x))  # Imprime: <class 'int'>

y = bool(x)
print(type(y))  # Imprime: <class 'bool'>
print(y)        # Imprime: True

# 5. Casteo de int o float a str

x = -17
print(type(x))  # Imprime: <class 'int'>

y = str(x)
print(type(y))  # Imprime: <class 'str'>
print(y)        # Imprime: '-17'

x = -17.75
print(type(x))  # Imprime: <class 'float'>

y = str(x)
print(type(y))  # Imprime: <class 'str'>
print(y)        # Imprime: '-17.75'

# 6. Casteo de str a int y de str a float

x = '13'
print(type(x))  # Imprime: <class 'str'>

y = int(x)
print(type(y))  # Imprime: <class 'int'>
print(y)        # Imprime: 13

x = '+13'
print(type(x))  # Imprime: <class 'str'>

y = int(x)
print(type(y))  # Imprime: <class 'int'>
print(y)        # Imprime: 13

x = '-13'
print(type(x))  # Imprime: <class 'str'>

y = int(x)
print(type(y))  # Imprime: <class 'int'>
print(y)        # Imprime: -13

# Y lo mismo pasa con float

# Errores:
# Cualquier caracter no numerico y que no sea + o -, o un + o un - ubicados mal, resulta
# en un error de tipo ValueError
# Todas las siguientes tienen errores:

# x = float('--3')        # Doble menos
# x = float('-17,85')     # Coma como separador decimal
# x = int('324746f43343') # Caracter no numerico

# Hay dos formas de evitar que una conversion de string a int o a float de un error que mate el
# programa
# 1. Chequear con un ciclo y con condicionales cada uno de los caracteres de manera manual
# 2. Usar try / except (NO SE VE EN ESTA MATERIA Y NO PUEDE USARSE)
# De todas formas, rara vez se pide realizar este tipo de validaciones en Informática General UCA

#############################
### LECTURAS RECOMENDADAS ###
#############################

# https://github.com/jcausse/clases_uca_ig/blob/main/unidad_1/Teoria/modulo(porcentaje).py
# https://github.com/jcausse/clases_uca_ig/blob/main/unidad_3/Teoria/operadores_logicos.py
