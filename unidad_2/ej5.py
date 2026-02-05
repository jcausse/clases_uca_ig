"""
Ejercicio 5:

Programar una función que reciba como parámetros 2 números naturales y retorne un
número natural al azar comprendido entre estos 2 números (inclusive). Debe asumirse
que esta función será invocada de manera que el primer parámetro representa el límite
inferior del intervalo y el segundo el límite superior.

Utilizarla en un programa que solicite al usuario los límites del intervalo e invoque a la
función tres veces de la siguiente manera:

5.1.    Invocarla con los extremos del intervalo ingresados por teclado y mostrar en
        pantalla el valor generado.
5.2.    Invocarla como en el punto 5.1, pero usando como extremo inferior el valor
        generado en 5.1.
5.3.    Invocarla como en el punto 5.2, pero usando como extremo superior el valor
        generado en 5.2.
"""

import random

def numero_aleatorio(inf, sup):
    return random.randint(inf, sup)

def main():
    inf = int(input('Ingrese el limite inferior (numero natural): '))
    sup = int(input('Ingrese el limite superior (numero natural): '))

    # 5.1
    num = numero_aleatorio(inf, sup)
    print('1-Limite inferior {}, limite superior {}. Numero generado: {}'.format(inf, sup, num))

    # 5.2
    inf = num                           # Guardo el valor anterior en inf
    num = numero_aleatorio(inf, sup)    # Y despues vuelvo a generar el numero
    print('2-Limite inferior {}, limite superior {}. Numero generado: {}'.format(inf, sup, num))

    # 5.3
    sup = num                           # Guardo el valor anterior en sup
    num = numero_aleatorio(inf, sup)    # Y despues vuelvo a generar el numero
    print('3-Limite inferior {}, limite superior {}. Numero generado: {}'.format(inf, sup, num))


main()
