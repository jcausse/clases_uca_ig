"""
Ejercicio 5:

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
# range(1, 3) genera unicamente 1 y 2. Slices [start:end:step] tratan al end igual que range
# (es decir, no incluyen el end, sino que incluyen hasta end - 1).

from random import randint

def transformar_numero(a, b, c):
    """
    Esta funcion recibe 3 enteros a, b y c, y devuelve:
    - c si a <= c <= b
    - un numero aleatorio en [a, b] si c no cumple la condicion anterior
    Nota: esta funcion supone que a <= b
    """
    if a <= c and c <= b:
        res = c
    else:
        res = randint(a, b)
    return res

def cambiaLista(lst, a, b):
    """
    for elem in lst:                                    # No funciona, pues al modificar elem estoy modificando una variable que
        elem = transformar_numero(a, b, elem)           # copia al elemento de la lista, no el elemento en si
    """
    # Necesito usar range para acceder a los elementos por su indice, y asi poder modificarlos:
    
    for i in range(len(lst)):                           # Para cada indice valido en la lista
        lst[i] = transformar_numero(a, b, lst[i])       # Cambio al i-esimo elemento por lo que devuelva transformar_numero
                                                        # Si el numero esta entre a y b, devuelve el mismo numero y no hay cambios
                                                        # Si el numero no esta entre a y b, devuelve un nuevo numero en [a, b] y la
                                                        # lista cambia

def cargar_lista():
    """
    Pide al usuario numeros par cargar una lista
    Cuando el usuario no ingrese nada (deje la entrada vacia) termina
    """
    res = []
    listo = False                                       # Bandera para cortar el ciclo
    while not listo:                                    # Mientras listo no sea True
        nuevo_num = input('Ingrese un numero: ')        # Pido al usuario que ingrese un numero, pero lo dejo como string
        if nuevo_num == '':                             # Si el usuario no ingresa nada (solo oprime enter) dejara la entrada vacia
            listo = True                                # Si no ingreso nada, termino
        else:                                           # Si se ingreso un numero
            res.append(int(nuevo_num))                  # Lo convierto a entero y lo agrego a la lista
    return res

def main():
    # Pido una lista y la muestro por pantalla
    lst = cargar_lista()
    print('Lista ingresada: ')
    print(lst)

    # Intervalo [a, b]
    a = int(input('Ingrese el extremo inferior del intervalo: '))
    b = int(input('Ingrese el extremo superior del intervalo: '))

    # La modifico (recordar que las listas se pasan por referencia y NO por copia)
    cambiaLista(lst, a, b)

    # Muestro la lista luego de modificarse
    print(lst)

main()
