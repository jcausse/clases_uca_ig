#############################
### Operadores de strings ###
#############################

###########################################################################################################
# Recordar que los strings son INMUTABLES, por lo que algo como string[2] = "x" (que intenta modificar un #
# caracter en específico del mismo) no es válido y generará un error.                                     #
###########################################################################################################

# Los strings soportan los siguiente operadores que se utilizan en Informática General de la UCA:

### Operador de concatenación ###
# El operador de concatenación es el símbolo +. Se utiliza para unir dos strings. El resultado es un nuevo string,
# y los strings originales no se modifican.

### Ejemplos ###

print("Operador de concatenación:")
x = "Hola"
print(x + "Mundo")  # "HolaMundo"
print("" + "Hola")  # "Hola"
print("Hola" + "")  # "Hola"
# print("Mi numero de la suerte es: " + 9)  # Error: solo se puede concatenar string con string, no otro tipo de dato
#                                           # TypeError: can only concatenate str (not "int") to str
print("Mi numero de la suerte es: " + str(9))  # "Mi numero de la suerte es: 9" (str convierte el número a string para ser concatenado)

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