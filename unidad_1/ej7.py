"""
Ejercicio 7:

Desarrollar un programa en el que se ingresen dos números enteros positivos y que                           
genere y muestre un tercer número que esté compuesto por las unidades del primer                           
número y por las decenas del segundo.
"""

# Ingresamos los numeros
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

# Calculamos las unidades de num1
unidad_num1 = num1 % 10                     # Un numero (0 - 9) que representa las unidades de num1

# Calculamos la decena de num2
decena_num2 = ((num2 // 10) % 10)           # Un numero (0 - 9) que representa las decenas de num2

# Calculamos el resultado final, que se compone de:
# - decena de num2 (multiplicado por 10 para que quede como decena)
# - unidad de num1 (sin multiplicar, para que quede como unidad)
resultado = decena_num2 * 10 + unidad_num1

# Mostramos el resultado como se pide
print('El numero resultante es: {}'.format(resultado))
