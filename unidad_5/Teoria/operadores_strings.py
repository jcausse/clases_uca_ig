#############################
### Operadores de strings ###
#############################

###########################################################################################################
# Recordar que los strings son INMUTABLES, por lo que algo como string[2] = "x" (que intenta modificar un #
# caracter en específico del mismo) no es válido y generará un error.                                     #
###########################################################################################################

# Los strings soportan los siguientes operadores que se utilizan en Informática General de la UCA:

### Operador de concatenación ###
# El operador de concatenación es el símbolo +. Se utiliza para unir (concatenar) dos strings. El resultado es un nuevo string,
# y los strings originales no se modifican.

### Ejemplos ###

print("Operador de concatenación:")
x = "Hola"
print(x + "Mundo")  # "HolaMundo"
print("" + "Hola")  # "Hola" (concatenar con el string vacio no cambia en nada)
print("Hola" + "")  # "Hola"
# print("Mi numero de la suerte es: " + 9)      # Error: solo se puede concatenar string con string, no otro tipo de dato
#                                               # TypeError: can only concatenate str (not "int") to str
print("Mi numero de la suerte es: " + str(9))   # "Mi numero de la suerte es: 9" (str convierte el número a string para ser concatenado)

print("--------------------------------------\n")

### Operador de repetición ###
# El operador de repetición es el símbolo *. Se utiliza para repetir un string un número determinado de veces.
# El resultado es un nuevo string, y el string original no se modifica.

### Ejemplos ###

print("Operador de repetición:")
print("Hola" * 3)   # "HolaHolaHola"
y = "Buen Dia"
print(y * 2)        # "Buen DiaBuen Dia"
z = "Adios"
print(5 * z)        # "AdiosAdiosAdiosAdiosAdios"
print(z * 0)        # "" (multiplicar por 0 da como resultado un string vacío)
print(z * -4)       # "" (multiplicar por un número negativo da como resultado un string vacío)

print("--------------------------------------")

### Comparación de strings ###
# Los operadores de comparación == y != nos pueden informar si dos strings son iguales. Estos operadores, al igual que en cualquier
# otro de sus usos, devuelven un resultado de tipo 'bool' (True o False).
# Notar que dos strings son iguales si ambos tienen la misma longitud (la misma len), y son iguales caracter a caracter (distinguiendo
# entre mayúsculas y minúsculas).

### Ejemplos ###

print("Comparación:")
print('hola' == 'chau')     # False
print('' != ' ')            # True
print('python' == 'python') # True
print('python' == 'Python') # False

# Los operadores <, <=, > y >= comparan los strings de manera que un string es menor que otro cuando:
# * Ambos coinciden, pero uno es más corto, y entonces el más corto es menor
#   EJEMPLO: 'mate' < 'mates'
# * Ambos difieren en algún caracter, y entonces será menor aquel que tenga el caracter con el menor código ASCII en la primera
#   vez que difieran. Ver tabla ASCII en: 
#   https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/800px-ASCII-Table-wide.svg.png?20221024154539
#   EJEMPLOS:
#   * 'buenos+dias' < 'buenos,dias'     pues el símbolo + está antes que la , en la tabla ASCII.
#   * 'Saludos' < 'saludos'             pues la S mayúscula está antes que la s minúscula
#   * 'Arte' < 'veloz'                  pues la A mayúscula está antes que la v minúscula              
#   NOTA: Las mayúsculas SIEMPRE vienen antes que las minúsculas en la tabla ASCII. Por esto, si en algún ejercicio se pide ordenar
#         de forma alfabética dos strings es necesario que los mismos estén o ambos en mayúsculas, o ambos en minúsculas.

### Utilidad ###
# Cuando los strings están únicamente formados por letras, y son siempre todas mayúsculas o todas minúsculas, estos operadores
# comparan strings de forma alfabética ascendente. De esta forma, y usando ciclos, se resuelve el problema de ordenar palabras en
# orden alfabético.
