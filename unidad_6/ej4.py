"""
Ejercicio 4:

Desarrollar un programa que solicite al usuario la carga de tres números enteros. Los
dos primeros representan los extremos de un intervalo de números, el tercero
representa una cantidad. Luego deberá invocar a la función cargarListaAleat donde
se le pasará por parámetro el intervalo (los dos números) y la cantidad (el tercer
número). La función deberá retornar un lista de largo “cantidad”, cargada con números
enteros positivos generados de forma aleatoria y pertenecientes al intervalo.
Luego se deberá calcular el máximo y el mínimo (ver más abajo la nota) de los valores
que contiene la lista y mostrar a ambos por pantalla.

Nota: Las dos funciones (minVal y maxVal) deberán ser desarrolladas. El
mínimo o el máximo se deberán obtener recorriendo la lista con un ciclo.
Considerar resolver el caso de que la lista sea vacía.
    a. minVal: Función que recibe por parámetro una lista y retorna el mínimo
        valor de la lista. Retorna None si la lista está vacía.
    b. maxVal: Función que recibe por parámetro una lista y retorna el máximo
        valor de la lista. Retorna None si la lista está vacía
        
cargarListaAleat: Función que recibe recibe por parámetro tres números (a, b, can) y
retorna una lista con can cantidades de números aleatorios que estén dentro del
intervalo cerrado [a,b]
    a, b: Son valores enteros positivo que determina los límites de un intervalo
        cerrado. No viene en orden (es decir no se sabe si a es menor que b).
    can: Es un número entero positivo que determina la cantidad de números
        aleatorios que debe contener la lista.
"""

import random       # Importamos la libreria random, para poder usar randint

def cargarListaAleat(a, b, can):
    """
    Devuelve una lista de _can_ elementos cargadda con enteros positivos aleatorios
    que estan dentro del intervalo.
    Calcula el maximo y el minimo.
    """
    # Ver que esten en orden, y sino, ordenar a y b (quiero a < b)
    if a > b:       # Si el limite inferior es mayor que el superior, los intercambio
        aux = a     # El valor de a lo guardo en aux, para no perderlo
        a = b       # El valor de b lo transfiero a a, que "pisa" su valor anterior (para eso lo guardo en aux)
        b = aux     # El valor original de a, que quedo en aux, pasa a b
        
    res = []        # Lista a devolver
    
    for _ in range(can):                        # _can_ veces. NOTA: cuando la variable del for no se usa, se suele poner un _
        res.append(random.randint(a, b))        # Generamos un numero aleatorio y lo agrego a la lista
        
    return res      # Devuelvo la lista
        
def minVal(lst):
    """
    Retorna el minimo de una lista, o None si la lista no tiene elementos
    """
    res = None              # Inicio res en None
    
    if len(lst) > 0:        # Solo ejecuto el algoritmo si la lista tiene al menos un elemento
        minimo = lst[0]     # Asumo que el minimo es el primer elemento de la lista (puede no ser verdad, no importa)
        for i in range(1, len(lst)):        # Para cada elemento restante (por eso el range empieza en 1, para saltear el primero)
            if lst[i] < minimo:             # Si el elemento que estoy tomando actualmente es menor que el minimo hasta ahora
                minimo = lst[i]             # Me anoto que el minimo es el actual
        res = minimo                        # Me quedo con el minimo en res para retornarlo
        
    return res
    
def maxVal(lst):
    """
    Retorna el maximo de una lista, o None si la lista no tiene elementos
    """
    res = None              # Inicio res en None
    
    if len(lst) > 0:        # Solo ejecuto el algoritmo si la lista tiene al menos un elemento
        maximo = lst[0]     # Asumo que el maximo es el primer elemento de la lista (puede no ser verdad, no importa)
        for i in range(1, len(lst)):        # Para cada elemento restante (por eso el range empieza en 1, para saltear el primero)
            if lst[i] > maximo:             # Si el elemento que estoy tomando actualmente es mayor que el maximo hasta ahora
                maximo = lst[i]             # Me anoto que el maximo es el actual
        res = maximo                        # Me quedo con el maximo en res para retornarlo
        
    return res

def main():
    a = int(input('Ingrese el inicio del intervalo (numero entero):  '))
    b = int(input('Ingrese el fin del intervalo (numero entero): '))
    can = int(input('Ingrese la cantidad de numeros a generar:  '))
    
    lista = cargarListaAleat(a, b, can)
    print(lista)                                        # Imprimo la lista devuelta
    print('Valor minimo: {}'.format(minVal(lista)))     # Imprimo el valor minimo
    print('Valor maximo: {}'.format(maxVal(lista)))     # Imprimo el valor maximo
    
main()
