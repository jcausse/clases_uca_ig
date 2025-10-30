"""
Ejercicio 1:

Desarrollar la función estaEnLista qué recibe por parámetro un número entero num y
una lista de enteros lst. La función debe retornar True si num se encuentra dentro de
lst, caso contrario deberá retornar False.
estaEnLista deberá ser desarrollada (y probada) de tres formas distintas, según el
siguiente criterio:
1.1. estaEnLista1 Utilizando sólo el operador IN para verificar si se encuentra un
    elemento en la lista.
1.2. estaEnLista2 Recorriendo la lista con un ciclo for y realizando comparaciones
    elemento a elemento  para verificar si se encuentra un elemento en la lista.
1.3. estaEnLista3 Recorriendo la lista con un ciclo while y realizando
    comparaciones elemento a elemento para verificar si se encuentra un elemento
    en la lista.
"""

# in
def estaEnLista1(num, lst):
    return num in lst                   # Devuelvo lo que me devuelve in (que ya es True o False)

# for
def estaEnLista2(num, lst):
    ret = False                         # Asumo que no lo voy a encontrar
    for elem in lst:                    # Para cada elemento en la lista
        if elem == num:                 # Si el elemento actual de la lista es el numero que estoy buscando
            ret = True                  # Cuando lo encuentro marco ret en True
    return ret                          # Si lo encontre, ret se hizo True, devuelvo True. Sino, devuelvo el False inicial

# while
def estaEnLista3(num, lst):
    # Idem funcion anterior, pero con un while
    ret = False
    i = 0
    while i < len(lst) and ret == False:                # Solo sigo iterando cuando no lo encontre
        if lst[i] == num:
            ret = True
        i += 1
    return ret

def main():
    print('Todos False:')
    print(estaEnLista1(10, []))                            # False
    print(estaEnLista1(10, [9, 11, 12, 13]))               # False
    print(estaEnLista1(-1, [1]))                           # False

    print(estaEnLista2(10, []))                            # False
    print(estaEnLista2(10, [9, 11, 12, 13]))               # False
    print(estaEnLista2(-1, [1]))                           # False

    print(estaEnLista3(10, []))                            # False
    print(estaEnLista3(10, [9, 11, 12, 13]))               # False
    print(estaEnLista3(-1, [1]))                           # False

    print('Todos True:')
    print(estaEnLista1(10, [10]))                          # True
    print(estaEnLista1(10, [9, 10, 11, 12]))               # True
    print(estaEnLista1(10, [10, 11, 12]))                  # True
    print(estaEnLista1(10, [8, 9, 10]))                    # True

    print(estaEnLista2(10, [10]))                          # True
    print(estaEnLista2(10, [9, 10, 11, 12]))               # True
    print(estaEnLista2(10, [10, 11, 12]))                  # True
    print(estaEnLista2(10, [8, 9, 10]))                    # True

    print(estaEnLista3(10, [10]))                          # True
    print(estaEnLista3(10, [9, 10, 11, 12]))               # True
    print(estaEnLista3(10, [10, 11, 12]))                  # True
    print(estaEnLista3(10, [8, 9, 10]))                    # True

main()
