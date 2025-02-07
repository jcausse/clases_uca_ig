"""
Ejercicio 10:

Crear una función atributoTriple que recibe por parámetro una lista de números
enteros y retorne un mensaje (Texto) de acuerdo a las características de la lista que
figuran en la tabla 1 (más abajo).

+----------------------------------------------------------------
| MENSAJE | Descripción del atributo de la lista
+------------------------------------------------------------
| ”Un Triple” | Si la lista contiene solamente un conjunto de exactamente tres 
|             | valores iguales consecutivos.
+------------------------------------------
| ”Dos Triples” | Si la lista contiene exactamente dos conjuntos de exactamente
|               | tres valores iguales consecutivos.
+--------------------------------
| “+ Triples” | Si la lista contiene tres o más conjuntos de exactamente tres
|             | valores iguales consecutivos.
+-------------------------------
| “NADA” | Si la lista no cumple con ninguna de las tres especificaciones
|        | anteriores.
+--------------------------------------------------------

Desde el programa principal, invocar a la función cargarListaAleat (desarrollada en
ejercicio 4), crear una lista con can cantidades de valores generados en forma
aleatoria entre un intervalo a y b, inclusive. Los valores can, a y b deberán ser
previamente ingresados por el usuario. Luego, una vez cargada la lista, se deberá pasar
por parámetro la lista cargada a la función atributoTriple y se deberá imprimir el
mensaje que retorna.
"""

#########################################################################################
# Del ejercicio 4:

import random

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

#########################################################################################

"""
IDEA:
Saco un numero.
Si el numero actual es igual al ultimo numero que saque, hay una repeticion. Con un contador, debo ir anotando cuando
hay repeticiones. Cuando el numero de repeticiones llega a 3, es un triple.
Si el numero actual difiere del ultimo numero que saque, esto corta cualquier repeticion que haya. En ese caso, debo
almacenar que el ultimo numero sacado es el actual, y resetear el numero de repeticiones a 1.

[1, 1, 2, 3, 3, 3]
 ^
Ultimo numero:              None    (caso inicial)
Cantidad de repeticiones:   0       (caso inicial)
Triples:                    0
1 == None? No. Entonces:
    Ultimo numero:              1
    Cantidad de repeticiones:   1
    Triples:                    0
    
[1, 1, 2, 3, 3, 3]
    ^
Ultimo numero:              1
Cantidad de repeticiones:   1
Triples:                    0
1 == 1? Si. Entonces:
    Ultimo numero:              1
    Cantidad de repeticiones:   2
    Triples:                    0
    
[1, 1, 2, 3, 3, 3]
    ^
Ultimo numero:              1
Cantidad de repeticiones:   2
Triples:                    0
2 == 1? No. Entonces:
    Ultimo numero:              2
    Cantidad de repeticiones:   1
    Triples:                    0
    
[1, 1, 2, 3, 3, 3]
        ^
Ultimo numero:              2
Cantidad de repeticiones:   1
Triples:                    0
3 == 2? No. Entonces:
    Ultimo numero:              3
    Cantidad de repeticiones:   1
    Triples:                    0
    
[1, 1, 2, 3, 3, 3]
            ^
Ultimo numero:              3
Cantidad de repeticiones:   1
3 == 3? Si. Entonces:
    Ultimo numero:              3
    Cantidad de repeticiones:   2
    Triples:                    0
    
[1, 1, 2, 3, 3, 3]
                ^
Ultimo numero:              3
Cantidad de repeticiones:   2
Triples:                    0
3 == 3? Si. Entonces:
    Ultimo numero:              3
    Cantidad de repeticiones:   3 ---> Llego a 3. Hay un triple! Incremento en 1 el numero de triples
    Triples:                    1
    
    Como el numero de repeticiones llego a 3, "reseteo" el estado del programa al estado inicial, es decir:
        Ultimo numero:              None
        Cantidad de repeticiones:   0
    Esto me permite que, para el proximo numero de la lista, el algoritmo arranque "limpio", y ademas me permite
    que si la lista contiene: [3, 3, 3, 3, 3] no se detecten como dos triples.
"""

def atributoTriple(lst):
    ultimo_numero = None        # Ultimo numero encontrado
    cantidad_repeticiones = 0   # Cantidad de veces que se repitio ese ultimo numero
    triples = 0                 # Cantidad de triples que encontre hasta ahora
    
    i = 0
    while i < len(lst) and triples < 3:         # Recorro la lista hasta el final, o hasta que el numero de triples sea 3
                                                # Esto es porque, el mensaje a retornar para 3 o mas triples es siempre el mismo, por
                                                # lo que, encontrados 3 triples, no tiene sentido seguir buscando.
                                                
        n = lst[i]                              # Saco el siguiente numero de la lista
        if n == ultimo_numero:                  # Si coincide con el anterior
            cantidad_repeticiones += 1          # Aumento el numero de repeticiones
            if cantidad_repeticiones == 3:      # Y si llego a 3
                ultimo_numero = None            # Reseteo las variables para arrancar de nuevo a buscar el proximo triple
                cantidad_repeticiones = 0
                triples += 1                    # Anoto que hubo un triple mas
                
        else:                                   # Si el nuevo numero no coincide con el anterior
            ultimo_numero = n                   # Cambia el ultimo numero
            cantidad_repeticiones = 1           # La cantidad de repeticiones se hace 1, pues el actual cuenta para el posible triple
        
        i += 1
        
    if triples == 0:
        res = 'NADA'
    elif triples == 1:
        res = 'Un Triple'
    elif triples == 2:
        res = 'Dos Triples'
    elif triples >= 3:
        res = '+ Triples'
    
    return res

def main():
    a = int(input('Ingrese valor inicial del intervalo: '))
    b = int(input('Ingrese valor final del intervalo: '))
    can = int(input('Ingrese la cantidad de valores del intervalo: '))

    lst = cargarListaAleat(a, b, can)
    
    print('Lista generada:')
    print(lst)
    
    print(atributoTriple(lst))
    
main()