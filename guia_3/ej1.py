"""
Ejercicio 1:

Desarrollar una función que reciba como parámetros dos números y un string con alguno                           
de los cuatro caracteres (+,-,*,/) y retorne el resultado de la operación. Desde el                           
programa principal el usuario ingresará los datos que serán pasados como parámetros a                         
la función y mostrará el resultado retornado por la misma.
"""

def calcular(num1, num2, op):
    ret = None
    if op == '+':
        ret = num1 + num2
    elif op == '-':
        ret = num1 - num2
    elif op == '*':
        ret = num1 * num2
    elif op == '/':
        ret = num1 / num2
    elif op == '**':                                # Extra
        ret = num1 ** num2
    elif op == '%':                                 # Extra
        ret = num1 % num2
    return ret

def main():
    num1 = int(input('Ingrese numero 1: '))
    num2 = int(input('Ingrese numero 2: '))
    op = input('Ingrese la operación (+, -, *, /, **, %): ') # ** y % son extra, no se pedian

    print(num1, op, num2, '=', calcular(num1, num2, op))

main()