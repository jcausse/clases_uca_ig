"""
EJERCICIO 5:

Desarrollar una función cambiaLista que reciba por parámetro una lista lst, y dos
valores enteros a y b que representan los extremos de un intervalo numérico. La función
deberá reemplazar dentro de la lista aquellos valores que se encuentran fuera del
intervalo [a,b] por valores aleatorios que se encuentren dentro del intervalo [a,b].

Desde el programa principal realizar la carga de una lista (puede utilizar alguna función
de carga de los ejercicios anteriores), y luego imprimir la lista en pantalla. A continuación
solicitar el ingreso de dos números enteros a y b e invocar a la función cambiaLista
pasándolo como parámetro los números y la lista. Luego volver a imprimir la lista, ya con
los valores cambiados.
"""

# Recuerdo: la funcion randint(a, b), a diferencia de otras (como por ejemplo range), incluye
# al extremo superior b. Esto quiere decir que randint(1, 3) puede devolver 1, 2 o 3.
# range(1, 3) genera unicamente 1 y 2. Slices [start:end:step] tratan al end igual que range.

from random import randint

# Esta funcion recibe 3 enteros a, b y c, y devuelve:
# - c si a <= c <= b
# - un numero aleatorio en [a, b] si c no cumple la condicion anterior
# Nota: esta funcion supone que a <= b
def transformar_numero(a, b, c):
    if a <= c and c <= b:
        return c
    else:
        return randint(a, b)

def cambiaLista(lst, a, b):
    #for elem in lst: # No funciona, pues al modificar elem estoy modificando una variable que
        #elem = transformar_numero(a, b, elem) # copia al elemento de la lista, no el elemento en si
    # Necesito usar range para acceder a los elementos por su indice, y asi poder modificarlos:
    for i in range(len(lst)):
        lst[i] = transformar_numero(a, b, lst[i])

def main():
    # TODO: cargar lista con una funcion de carga
    lst = [1, 3, -5, 8, 10, -1, 99, 37, -21, -2, -5, 76, 28]
    
    print(lst)

    # Intervalo [a, b]
    a = int(input('Ingrese el extremo inferior del intervalo: '))
    b = int(input('Ingrese el extremo superior del intervalo: '))

    cambiaLista(lst, a, b)

    print(lst)

main()
