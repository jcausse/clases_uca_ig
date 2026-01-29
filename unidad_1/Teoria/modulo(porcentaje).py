###########################
### Operador Modulo (%) ###
###########################

### IDEA ###

# El operador modulo (%) devuelve el resto de la division entera entre dos numeros.
# De la misma forma que en la escuela primaria aprendimos a dividir asi:
"""
   22     |  4
 -        +----
   20        5
  ----
    2
"""
# en Informatica, cuando usamos el operador modulo, estamos dividiendo el numero de la izquierda por el de la derecha,
# lo que produce un cociente y un resto, que siempre cumple:
"""
dividendo (22) = divisor (4) * cociente (5) + resto (2)
"""

### VALORES POSIBLES ###

# Notemos que el resto siempre se encuentra en el rango [0, divisor - 1].
# Por ejemplo, si estamos dividiendo por 5, el resto puede ser 0, 1, 2, 3 o 4, pero nunca 5 (ni mayor que 5), pues, si
# el resultado fuese 5 hubieramos podido volver a dividir por 5, y el resto seria 0.

# Ademas, cuando el resto es 0, el dividendo es multiplo del divisor (o, tambien, el divisor divide al dividendo).

### EJEMPLOS ###
"""
print(10 % 3)   # 10 // 3 = 3, y el resto es 1, por lo que imprime 1
print(10 % 2)   # 10 // 2 = 5, el resto es 0, imprime 0
print(10 % 4)   # 10 // 4 = 2, el resto es 2, imprime 2
"""

################################
### Usos del operador modulo ###
################################

# 1. Determinar si un numero es divisible por otro.
#    Si queremos saber si a es divisible por b, basta verificar que el resto de dividir a por b sea 0.
"""
a = 10
b = 6
if a % b == 0:
    print('{} es divisible por {}'.format(a, b))
else:
    print('{} NO es divisible por {}'.format(a, b))
"""

# 2. Determinar si un numero es par o impar.
#    Un numero es par cuando es divisible por 2.
#    Si queremos saber si un numero es par, basta verificar que el resto de dividir el numero por 2 sea 0.
"""
a = 10
if a % 2 == 0:
    print('{} es par'.format(a))
else:
    print('{} es impar'.format(a))
"""

# 3. Determinar si un numero es primo.
#    Un numero es primo cuando es divisible unicamente por 1 y por si mismo.
#    Si queremos saber si un numero es primo, basta verificar que no sea divisible por ningun numero entre 2 y el mismo numero - 1, en principio.
#    Una mejor forma de hacerlo es verificar que no sea divisible por ningun numero entre 2 y el mismo numero dividido por 2.
#    La mejor forma es verificar que no sea divisible por ningun numero entre 2 y la raiz cuadrada del numero.
"""
Este ejemplo requiere del uso de condicionales, ciclos y funciones, que no son tema de esta practica.
Ver guia_4/Teoria/ciclos.py para ver la implementacion.
"""

# 4. Incrementar un contador que se reinicia al llegar a cierto valor.
#    Si queremos incrementar un contador que se reinicia al llegar a cierto valor, basta con usar el operador modulo para que, al llegar al valor,
#    el contador se reinicie a cero.
"""
maximo = 5
valor = 2
print(valor) # Imprime 2

# Incrementamos el valor
valor = (valor + 1) % maximo   # Valor es 2. Al hacer valor + 1 da 3. 3 % 5 = 3, por lo que valor es 3.
print(valor) # Imprime 3

# Incrementamos el valor
valor = (valor + 1) % maximo   # Valor es 3. Al hacer valor + 1 da 4. 4 % 5 = 4, por lo que valor es 4.
print(valor) # Imprime 4

# Incrementamos el valor
valor = (valor + 1) % maximo   # Valor es 4. Al hacer valor + 1 da 5. 5 % 5 = 0, por lo que valor es 0.
print(valor) # Imprime 0

# Incrementamos el valor
valor = (valor + 1) % maximo   # Valor es 0. Al hacer valor + 1 da 1. 1 % 5 = 1, por lo que valor es 1.
print(valor) # Imprime 1
"""
