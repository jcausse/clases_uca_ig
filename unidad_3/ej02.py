"""
Ejercicio 2:

Desarrollar una función que reciba tres números como parámetros, e imprima en                       
pantalla los números pasados por parámetro de forma ordenada ascendentemente​. La                     
función debe ser invocada desde un programa que solicite el ingreso por teclado de los                             
números.
"""

def mayor(a, b):
    if a > b:
        ret = a
    else:
        ret = b
    return ret

def menor(a, b):
    if a < b:
        ret = a
    else:
        ret = b
    return ret

def imprimir_ordenado(a, b, c):
    maximo = mayor(mayor(a, b), c)
    minimo = menor(menor(a, b), c)
    medio = a + b + c - maximo - minimo
    print('Menor:', minimo)
    print('Medio:', medio)
    print('Mayor:', maximo)

def main():
    a = int(input('Ingrese primer numero: '))
    b = int(input('Ingrese segundo numero: '))
    c = int(input('Ingrese tercer numero: '))

    imprimir_ordenado(a, b, c)

main()