# https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja

# ANIMACION:
# https://www.youtube.com/watch?v=9I2oOAr2okY


########################################################
### Bubble Sort / BBSort / Ordenamiento por burbujeo ###
########################################################

# Es uno de los algoritmos de ordenamiento más sencillos (pero más ineficientes) entre los más estudiados.

# El algoritmo trabaja con una serie de "pasadas", en cada una de las cuales el número mayor (en principio) "asciende"
# (como una burbuja en un vaso de gaseosa) hacia el final de la lista.

# La idea básica de cada pasada es recorrer desde el principio hasta el fin, tomando los elementos de a dos (siempre uno y su 
# posterior), e intercambiándolos (swap), de ser necesario, para lograr que los elementos mayores siempre queden a la derecha.
# Como al final de cada pasada el mayor elemento quedara a la derecha de todo de la lista, en la siguiente pasada, el mismo será
# ignorado (de modo que la segunda pasada tome a todos los elementos menos el último).
# De esta manera, la última pasada solo tomará a los dos primeros elementos.


#################################
### Ejemplo de funcionamiento ###
#################################

# Imaginemos que la lista es:
"""
[1, -2, 7, 3, 0]
"""

################## Primera pasada ################## 

# Inicialmente la lista es:
"""
[1, -2, 7, 3, 0]
"""
# NO HAY ELEMENTOS FIJOS

# Se toma el 1 y el -2. Como 1 > -2 se intercambian. La lista queda:
"""
[-2, 1, 7, 3, 0]
"""

# Se toma el 1 y el 7. Como 1 < 7 no se intercambian. La lista no se modifica:
"""
[-2, 1, 7, 3, 0]
"""

# Se toma el 7 y el 3. Como 7 > 3 se intercambian. La lista queda:
"""
[-2, 1, 3, 7, 0]
"""

# Se toma el 7 y el 0. Como 7 > 0 se intercambian. La lista queda:
"""
[-2, 1, 3, 0, 7]
"""

# Fin de la primera pasada. El mayor elemento (7) quedó en la última posición.

################## Segunda pasada ################## 

# Inicialmente la lista es:
"""
[-2, 1, 3, 0, 7]
"""
# EL ULTIMO ELEMENTO ESTA FIJO

# Se toma el -2 y el 1. Como -2 < 1 no se intercambian. La lista no se modifica:
"""
[-2, 1, 3, 0, 7]
"""

# Se toma el 1 y el 3. Como 1 < 3 no se intercambian. La lista no se modifica:
"""
[-2, 1, 3, 0, 7]
"""

# Se toma el 3 y el 0. Como 3 > 0 se intercambian. La lista queda:
"""
[-2, 1, 0, 3, 7]
"""

# Fin de la segunda pasada. Notar que el 7 NO se toca (pues ya esta ordenado), tomando como ultimo par el 0 y el 3.

################## Tercera pasada ##################

# Inicialmente la lista es:
"""
[-2, 1, 0, 3, 7]
"""
# LOS ULTIMOS DOS ELEMENTOS ESTAN FIJOS

# Se toma el -2 y el 1. Como -2 < 1 no se intercambian. La lista no se modifica:
"""
[-2, 1, 0, 3, 7]
"""

# Se toma el 1 y el 0. Como 1 > 0 se intercambian. La lista queda:
"""
[-2, 0, 1, 3, 7]
"""

# Fin de la tercera pasada (notar que los ultimos dos elementos no se tocan).


################## Cuarta pasada ##################

# Inicialmente la lista es:
"""
[-2, 0, 1, 3, 7]
"""
# LOS ULTIMOS TRES ELEMENTOS ESTAN FIJOS
# Notar que la lista ya esta ordenada, pero el algoritmo debe continuar hasta terminar, por mas que no haya mas intercambios.

# Se toma el -2 y el 0. Como -2 < 0 no se intercambian. La lista no se modifica:
"""
[-2, 1, 0, 3, 7]
"""

# Fin de la cuarta pasada (notar que los ultimos tres elementos no se tocan).

################## FIN ##################

# Como la ultima pasada solo tomo un solo par, fue la ultima. La lista ya esta ordenada.


######################
### Implementación ###
######################

# Recordar que las listas se pasan por referencia, por lo que la función "bubblesort" puede modificar directamente
# la lista al ordenarla, sin necesidad de retornar una nueva lista ordenada.

### COPIAR ESTA IMPLEMENTACIÓN ###
"""
def bubblesort(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                aux = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = aux

# Programa de prueba:
lst = [1, -2, 7, 3, 0]
print(lst)              # [1, -2, 7, 3, 0]
bubblesort(lst)
print(lst)              # [-2, 1, 0, 3, 7]
"""


########################################
### Explicación de la implementación ###
########################################
"""
def bubblesort(lst):
    for i in range(0, len(lst) - 1):                # i es una variable que le va a indicar cuantos elementos ignorar.
                                                    # Para i = 0 no se ignoran elementos (no hay fijos)
                                                    # Para i = 1 se ignora el ultimo elemento (hay 1 fijo)
                                                    # Para i = 2 se ignoran los ultimos dos elementos (hay 2 fijos)
                                                    # ...
                                                    # Para i = len(lst) - 2 (ultimo valor) se fijan todos los elementos menos los
                                                    # ultimos dos (ultima pasada)
                                                    # Finalmente, i es el NUMERO DE PASADA.
                                                    
                                                    # DENTRO DE UNA MISMA PASADA:
                                                    
        for j in range(0, len(lst) - i - 1):        # j dicta que par de elementos tomar. Se toma el j-esimo y su siguiente.
                                                    # Tiene un -i pues i lo que indica es la cantidad de elementos a ignorar desde el
                                                    # final (aquellos que estan fijos). En cada pasada, se ignora un elemento más.
                                                    # Tiene un -1 porque se toman un elemento y su siguiente. Si no se pone el -1, se
                                                    # podria llegar a tomar el ultimo elemento (que no tiene siguiente) y dar error.
            
            if lst[j] > lst[j + 1]:                 # Si para un par de elementos, el j-esimo es mayor que su siguiente (j + 1)-esimo
                aux = lst[j]                        # Los elementos se intercambian (de la misma forma que se ve en el ejercicio 4)
                lst[j] = lst[j + 1]                 # Ver: https://github.com/jcausse/clases_uca_ig/blob/main/unidad_6/ej4.py
                lst[j + 1] = aux
"""


#############################################
### Ordenamiento ascendente y descendente ###
#############################################

# Notar que la siguiente línea del bubblesort:
"""
if lst[j] > lst[j + 1]:
"""
# Controla los swaps (los intercambios) entre elementos consecutivos.
# La idea de esta línea es que si un elemento es mayor que su siguiente, ese par de elementos se intercambien
# de manera que los mayores siempre queden a la derecha.
# Al terminar de correr todo el algoritmo, los números mayores siempre se habrán desplazado a la derecha, por lo que
# el orden de la lista será de menor a mayor (orden ascendente).

# De forma análoga, si logramos que los intercambios se den cuando el elemento anterior es menor que el elemento siguiente,
# lo que sucederá es que los elementos menores quedarán a la derecha, por lo que, al terminar el algoritmo, la lista quedará
# ordenada de mayor a menor (orden descendente).

# Entonces, lo único que debemos cambiar para alterar el orden de ordenamiento es el signo de la comparación:

# PARA ORDEN ASCENDENTE: intercambiar si el anterior es mayor al siguiente:
"""
if lst[j] > lst[j + 1]:
"""

# PARA ORDEN DESCENDENTE: intercambiar si el anterior es menor al siguiente:
"""
if lst[j] < lst[j + 1]:
"""


##############
### Prueba ###
##############

def bubblesort(lst):
    print('+---------------------------------+')
    print('|           BUBBLE SORT           |')
    print('+---------------------------------+')
    print('|')
    
    for i in range(0, len(lst) - 1):
        
        print('+---- INICIANDO PASADA {} -----'.format(i))
        
        for j in range(0, len(lst) - i - 1):
            
            print('+-> Comparando {} vs {}'.format(lst[j], lst[j + 1]))
            
            if lst[j] > lst[j + 1]:
                
                print('+-----> Intercambio!')
                
                aux = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = aux
           
        print('|')
          
    print('+---------------------------------+')

# Programa de prueba:
lst = [1, -2, 7, 3, 0]
print('Lista antes de ordenar: {}\n'.format(lst))       # [1, -2, 7, 3, 0]
bubblesort(lst)
print('\nLista despues de ordenar: {}'.format(lst))     # [-2, 1, 0, 3, 7]

"""
# Prueba más larga:
lst = [-21, 22, -37, -42, -2, -11, -40, 21, -4, -36, -49, 49, 10, -2, -31, 44, 50, 20, 39, -10, -34, -39, 0, 31, 33, 19, -35, 27, 34, -4]
print('Lista antes de ordenar: {}\n'.format(lst))
bubblesort(lst)
print('\nLista despues de ordenar: {}'.format(lst))
"""
