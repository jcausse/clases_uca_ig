"""
Ejercicio 6:

Programar una función booleana que retorne 0 o 1 al azar.  
Utilizarla en un programa en que se solicite al usuario dos alternativas para cada uno de                               
los ítems de una cena: vestimenta, plato y bebida. Luego el programa muestra por                           
pantalla la cena que resulta de elegir cada ítem al azar
"""

from random import randint

def zero_or_one():
    return randint(0, 1)

def main():
    vestimenta_1    = input('Ingrese la primera opcion de vestimenta: ')
    vestimenta_2    = input('Ingrese la segunda opcion de vestimenta: ')
    plato_1         = input('Ingrese la primera opcion de plato: ')
    plato_2         = input('Ingrese la segunda opcion de plato: ')
    bebida_1        = input('Ingrese la primera opcion de bebida: ')
    bebida_2        = input('Ingrese la segunda opcion de bebida: ')

    random_num = zero_or_one()
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
