"""
Ejercicio 7:

Desarrollar una función inserOrd que reciba dos parámetros (una lista lst y un
número num). La lista lst de números enteros positivos recibida por parámetro se
encuentra cargada y ordenada en forma ascendente, y el parámetro num, recibido por
parámetro, es un número entero positivo. La función debe insertar el valor de num dentro
de la lista de forma ordenada.

Aclaración: No se puede insertar (en cualquier lugar) y ordenar luego debido a que
el costo de computo a nivel ordenamiento es superior al de insertar ordenado.
Desde el programa principal, cargar una lista ordenada (puede utilizar alguna función de
ejercicios anteriores para cargar la lista) e imprimirla en pantalla (con otra función).
Luego solicitar el ingreso de un valor entero desde el teclado (para ser insertado en la
lista), y a continuación invocar inserOrd (pasandole la lista y el número a insertar).
Luego volver a imprimir en pantalla la lista (con el valor insertado en forma ordenada).
"""


# IDEA:

# Si la lista es [3, 6, 11, 18, 21, 25, 32] y se quiere insertar el 19, el mismo va entre
# el 18 (índice 3) y el 21 (índice 4).

# Insertar un elemento de forma ordenada en una lista esencialmente consta de 2 operaciones:
# 1. Buscar la posición (el índice) donde va a quedar el elemento.
# 2. Insertar el elemento en esa posición llamando al método insert(), que toma el elemento
#    y la posición de inserción.

# Paso 1: Buscar la posición
# Si la lista es l = [3, 6, 11, 18, 21, 25, 32] y quiero insertar 19, empiezo desde el principio
# de la lista y voy comparando:
# - l[0] = 3 es menor que 19, entonces el 19 tiene que ir más adelante
# - l[1] = 6 es menor que 19, entonces el 19 tiene que ir más adelante
# - l[2] = 11 es menor que 19, entonces el 19 tiene que ir más adelante
# - l[3] = 18 es menor que 19, entonces el 19 tiene que ir más adelante
# - l[4] = 21 es mayor que 19, entonces el 19 tiene que ocupar el lugar del 21 (la posición 4), y
#             todos los elementos que le siguen (incluído el 21) son desplazados un lugar a la
#             derecha de forma automática al insertar 19 en la posición 4.
# El índice de inserción va a ser 4.

# Paso 2: Insertar en la lista.
# Basta con llamar a l.insert(<índice de inserción>, <elemento a insertar>).
# En nuestro caso: l.insert(4, 19)

# Caso Borde 1: Insertar al principio.
# l = [2, 3, 4] y quiero insertar 1
# - l[0] = 2 es mayor que 1, entonces el 1 tiene que ocupar la posición 0 (la primera), y
#            hay que hacer l.insert(0, 1)
# La lista queda: l = [1, 2, 3, 4].

# Caso Borde 2: Insertar al final.
# En toda lista, los índices (positivos) válidos para la lista van entre 0 y len(lista) - 1.
# Es decir, si la lista contiene 5 elementos (len(lista) = 5), los índices válidos son
# {0, 1, 2, 3, 4}.
# En el caso de la inserción, para una lista de 5 elementos, insertar en la posición 4 no implica
# que el nuevo elemento queda al final, implica que el nuevo elemento pasa a ocupar la posición 4,
# pero el que actualmente ocupa dicha posición se corre un lugar a la derecha. Ejemplo:
"""
>>> l = [1, 2, 3, 4, 5]
>>> l.insert(len(l) - 1, 6) # len(l) - 1 es 4
>>> l
[1, 2, 3, 4, 6, 5]
"""
# Para la inserción "se habilita un índice más", que coincide con la len de la lista. De esta manera,
# para una lista de 5 elementos se puede hacer insert con índice 5

# Caso Borde 3: Inserción de elemento repetido
# lst = [1, 2, 3] y quiero insertar num = 2
# - lst[0] = 1 es menor que 2, entonces el 2 tiene que ir más adelante
# - lst[1] = 2 no es menor que 2, es igual, entonces el 2 que voy a insertar se inserta en la
#              posición donde estaba el otro 2, y el 2 original y el 3 se mueven a la derecha.


def inserOrd(lst, num):
    i = 0
    while i < len(lst) and lst[i] < num:
        i += 1
    lst.insert(i, num)

