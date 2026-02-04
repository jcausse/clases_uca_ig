"""
EJERCICIO 11:

Desarrollar un programa que solicite al usuario el ingreso de un número natural en base
10 (de no más de 5 cifras) y lo convierta a un número octal (en base 8).
"""

n = int(input('Ingrese un numero decimal (maximo 5 cifras): '))

s = ''  # En este string voy a ir armando el resultado

s = str(n % 8) + s      # Calculo los restos y voy armando el resultado en un string, por simplicidad
n = n // 8

s = str(n % 8) + s 
n = n // 8

s = str(n % 8) + s 
n = n // 8

s = str(n % 8) + s 
n = n // 8

s = str(n % 8) + s 
n = n // 8

s = str(n % 8) + s 
n = n // 8              # El cociente de la ultima operacion debe dar cero

print('Numero en octal:', int(s))  # Al convertir a int, elimino los posibles ceros a la izquierda

####################################################################################################

# COMO LO HAGO PARA UN NUMERO DE CANTIDAD ARBITRARIA DE DIGITOS? CON UN CILO (A PARTIR DE LA GUIA 4)
"""
n = int(input('Ingrese un numero decimal (maximo 5 cifras): '))
s = ''  # En este string voy a ir armando el resultado

while n > 0:                # Mientras que n sea mayor que cero, puedo seguir dividiendo
    s = str(n % 8) + s      # Obtengo el proximo digito
    n = n // 8              # Divido n para avanzar

print('Numero en octal:', int(s))
"""
