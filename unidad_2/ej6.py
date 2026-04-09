"""
Ejercicio 6:

Programar una función booleana que retorne 0 o 1 al azar.  
Utilizarla en un programa en que se solicite al usuario dos alternativas para cada uno de                               
los ítems de una cena: vestimenta, plato y bebida. Luego el programa muestra por                           
pantalla la cena que resulta de elegir cada ítem al azar
"""

"""
IDEA:

La idea principal de este ejercicio es que al multiplicar un string por 1, el mismo queda igual:
- 'hola' * 1 resulta 'hola'
pero, al multiplicar un string por cero, resulta el string vacio:
- 'chau' * 0 resulta ''

Uno puede "elegir al azar" uno de los dos strings obteniendo un numero aleatorio x que sea 0 o 1, y
luego multiplicando x por uno de los strings, y la expresion (1 - x) por el otro.
- Cuando x = 1:
  'hola' * x + 'chau' * (1 - x) ==> 'hola' * 1 + 'chau' * 0 ==> 'hola' + '' ==> 'hola'
- Cuando x = 0:
  'hola' * x + 'chau' * (1 - x) ==> 'hola' * 0 + 'chau' * 1 ==> '' + 'chau' ==> 'chau'
"""

import random

def zero_or_one():
    return random.randint(0, 1)

def main():
    vestimenta_1    = input('Ingrese la primera opcion de vestimenta: ')
    vestimenta_2    = input('Ingrese la segunda opcion de vestimenta: ')
    plato_1         = input('Ingrese la primera opcion de plato: ')
    plato_2         = input('Ingrese la segunda opcion de plato: ')
    bebida_1        = input('Ingrese la primera opcion de bebida: ')
    bebida_2        = input('Ingrese la segunda opcion de bebida: ')

    # Obtener un numero aleatorio entre 0 y 1
    random_num = zero_or_one()
    # Seleccionar una opcion haciendo multiplicacion y concatenacion de strings
    vestimenta = (1 - random_num) * vestimenta_1 + random_num * vestimenta_2

    random_num = zero_or_one()
    plato = (1 - random_num) * plato_1 + random_num * plato_2

    random_num = zero_or_one()
    bebida = (1 - random_num) * bebida_1 + random_num * bebida_2

    print('Cena al azar:')
    print('Vestimenta:', vestimenta)
    print('Plato:', plato)
    print('Bebida:', bebida)

main()
