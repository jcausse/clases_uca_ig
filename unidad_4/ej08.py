"""
Ejercicio 8:

La operación factorial de un número entero no negativo n (expresado como n!) es el
producto que resulta de multiplicar n por todos los enteros inferiores a él hasta el uno 
(0! = 1 por definición). Ejemplo:

    5! = 5 * 4 * 3 * 2 * 1 = 120
    10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
    n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1 = .............

Desarrollar un programa que solicite el ingreso de un número entero, verifique si se trata
de un número mayor o igual a 0 y calcule su factorial. Para el cálculo del factorial se
debe desarrollar una función que reciba como parámetro el número, realice la operatoria
y retorne el resultado. En caso de que el usuario ingrese un número negativo, imprimir
una advertencia.
"""

def factorial(n):
    ret = 1
    for i in range(2, n + 1): # Empieza de 2 para no hacer 1 * 1. Termina en n + 1 para llegar hasta n.
        ret *= i              # Cuando n es 0 o 1 el for no ejecuta y devuelve 1 directamente.
    return ret

def main():
    num = int(input('Ingrese un número entero: '))
    if num >= 0:
        res = factorial(num)
        print('El factorial de {} es: {}.'.format(num, res))
    else:
        print('No se puede calcular el factorial de un número negativo.')

main()
