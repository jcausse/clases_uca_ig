"""
Ejercicio 9:

Desarrollar un programa que solicite al usuario el ingreso de un número natural de una                             
cantidad impar de cifras (al menos 3 cifras). Luego el programa deberá informar la                           
cantidad de cifras del número ingresado, la primera y la última cifra del número                           
ingresado, como así también su cifra central.
"""

"""
IDEA:

NUMERO:     2 3 5 8 9 = 2*(10**4) + 3*(10**3) + 5*(10**2) + 8*(10**1) + 9*(10**0)
POTENCIA:   4 3 2 1 0

Si me quiero quedar con el digito N de un numero:
dig_N = (num // (10 ** N)) % 10
"""

# Ingreso el numero
num = int(input('Ingrese un numero de al menos 3 cifras, con cantidad impar de cifras: '))

# Calculo el ultimo digito (menos significativo) (no necesito saber la cantidad)
ultimo_digito = (num // (10 ** 0)) % 10                     # Es lo mismo que num % 10, solo que uso la formula general

# Calcular la cantidad de digitos que tiene el numero, lo cual me va a permitir calcular
# el digito de la izquierda (el primero) y el del medio. Recordar que la cantidad de digitos es impar.
cant_digitos = len(str(num))

# Calculo el primer digito (mas significativo)
primer_digito = (num // (10 ** (cant_digitos - 1))) % 10    # En este caso, el % 10 no hace nada, pero es parte del algoritmo

# Calculo el digito del medio
digito_central = (num // (10 ** ((cant_digitos - 1) // 2))) % 10

# Imprimo el resultado como se pide
print('El numero ingresado tiene {} cifras.'.format(cant_digitos))
print('La primera cifra es {}, la ultima es {} y la central es {}.'.format(primer_digito, ultimo_digito, digito_central))

#########################################################################################################

########################################
### EXTRAS (usa cosas mas avanzadas) ###
### No se recomienda leer antes de   ###
### llegar a la guia 3               ###
########################################

"""
######################################
# Extra 2: funcion que calcula y
# devuelve una cifra determinada de
# un numero dado

def get_num_digit(num, digit):
    return (num // (10 ** digit)) % 10

######################################

num = int(input('Ingrese un numero de al menos 3 cifras, con cantidad impar de cifras: '))
num_digits  = len(str(num)) # Numero impar

######################################
# Extra 1: validar cantidad de digitos
if num_digits < 3 or num_digits % 2 == 0:
    print('El numero debe tener una cantidad impar de digitos, y al menos 3 digitos.')

else:
######################################

    # Sin funciones (practica 1):
    #mas_sig     = (num // (10 ** (num_digits - 1))) % 10
    #medio       = (num // (10 ** (num_digits // 2))) % 10
    #menos_sig   = (num // (10 ** 0)) % 10

    # Con funciones (practica 2):
    mas_sig     = get_num_digit(num, num_digits - 1)
    medio       = get_num_digit(num, num_digits // 2)
    menos_sig   = get_num_digit(num, 0)

    print('Numero:', num)
    print('Digito mas significativo: ', mas_sig)
    print('Digito del medio: ', medio)
    print('Digito menos significativo: ', menos_sig)
"""
