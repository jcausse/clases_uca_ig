"""
Ejercicio 2:

Programar la función ​raiz ​que recibe como parámetros un radicando ​x (​número real​) y                           
un índice ​n (​número natural​). La función deberá ​retornar la raíz ​n ​(enésima) de ​x​.                             
Utilizarla en un programa que solicite al usuario el radicando real y el índice natural.                             
Luego invocar a la función ​raiz ​e informar la raíz calculada.
"""

def raiz(radicando, indice):
    return radicando ** (1 / indice)

def main():
    radicando = float(input('Ingrese el radicando (numero real): ')) 
    indice = int(input('Ingrese el índice (numero natural): '))

    resultado = raiz(radicando, indice)
 
    print('La raiz de indice', indice, 'de', radicando, 'es =', resultado)

main()
