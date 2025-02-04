"""
Ejercicio 4:

Desarrollar una función booleana "principioFin" que reciba como parámetro un texto y                       
detecte si la primera palabra del texto es exactamente igual a la última.  
Por Ejemplo:  
    “Barón!, urgente ya ha nacido! Es un varón!”        → False  
    “Entre que ya se vienen los hombres de enfrente”    → False  
    “Hombre de poca fe, he dicho! Vamos, vamos hombre!” → True 
Desde el programa principal ingresar por teclado un texto, invocar a la función y mostrar                             
por pantalla un mensaje que indique si cumple o no con la condición.
"""

# PALABRA: toda secuencia de caracteres letra (a-z y A-Z unicamente) que estén separados por:
# * Un espacio (lo más común)
# * Un signo de exclamación / interrogación
# * Cualquier otra cosa

# Por ahora, NO podemos usar listas (porque es tema de la unidad 6)

def es_letra(c):
    """
    Dado un caracter, devuelve True si es una leta (a-z o A-Z) o False en caso contrario
    """
    ret = False             # Asumo que no es letra
    if 'a' <= c <= 'z':     # Es minuscula?
        ret = True              # Entonces es letra
    elif 'A' <= c <= 'Z':    # Es mayuscula?
        ret = True              # Entonces es letra
    return ret              # Si fue minuscula o mayuscula, ret se puso en True. Sino, se mantuvo en False.

    # Una mejor forma de hacer todo esto en una sola linea:
    # return ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z')

def primera_palabra(texto):
    """
    DIAGRAMA DE FLUJO DE ESTA FUNCION: https://github.com/jcausse/clases_uca_ig/blob/main/unidad_5/ej4_primera_palabra.png
    
    Dado un texto, obtiene la primera PALABRA del mismo.
    """
    indice_inicio = 0               # Aca voy a guardar el primer caracter que ES una letra
    indice_fin = 0                  # Aca voy a guardar el ultimo caracter que ES una letra al encontrar uno que no es letra
    i = 0
    
    encontrado = False
    while not encontrado and i < len(texto):        # Para cada caracter, y hasta que encuentre una letra, avanzo en el string
        if es_letra(texto[i]):                      # Encuentro una leta ---> No avanzo y salgo del while
            encontrado = True
        else:                                       # No encuentro letra ---> Avanzo y no salgo del while
            i += 1 

    indice_inicio = i                               # El indice de inicio es el de la primera letra que encontre, y no lo vuelvo a tocar
    indice_fin = i                                  # El indice de fin, por ahora, es el de la primera letra (podria ser una palabra de 1 letra)
    i += 1
    
    encontrado = False
    while not encontrado and i < len(texto):        # Para cada caracter, y hasta que encuentre algo que NO sea letra, avanzo en el string
        if es_letra(texto[i]):                      # Encuentro una letra ---> Ahora es la ultima letra encontrada (la palabra, por ahora,
            indice_fin = i                          # termina aca)
            i += 1
        else:                                       # Encuentro algo que no es letra ---> El caracter anterior es la ultima letra cde la primera
            encontrado = True                       # palabra
            
    return texto[indice_inicio : indice_fin + 1]    # Recorto y retorno

"""
# Prueba de la funcion primera_palabra()
# NO es parte del ejercicio

primera = primera_palabra('¡Hola! Buenos dias.')
print(primera)          # 'Hola'
print(len(primera))     # 4

primera = primera_palabra('buenos dias')
print(primera)          # 'buenos'
print(len(primera))     # 6

primera = primera_palabra('hola')
print(primera)          # 'hola'
print(len(primera))     # 4

primera = primera_palabra('')
print(primera)          # ''
print(len(primera))     # 0
"""

def ultima_palabra(texto):
    """
    Dado un texto, obtiene la ultima PALABRA del mismo.
    El algoritmo es analogo al de primera_palabra(), solo que:
    * En lugar de recorrer de izquierda a derecha, recorro de derecha a izquierda
    * Debido a esto, el que marco como indice_inicio es el indice de la primera letra de derecha a izquierda, y el que marco como
      indice_fin es el indice ultimo caracter de derecha a izquierda, de forma tal que se da algo como esto:
      
      texto = ¡Hola! Buenos dias.
                            ^  ^
                            |  |
                            |  +--- indice_inicio
                            |
                            +------ indice_fin
    """
    indice_inicio = 0               # Aca voy a guardar el primer caracter (derecha a izquierda) que ES una letra
    indice_fin = 0                  # Aca voy a guardar el ultimo caracter (derecha a izquierda) que ES una letra al encontrar uno que no es letra
    i = -1                          # i empieza en -1 (pues voy de derecha a izquierda)
    
    encontrado = False
    while not encontrado and i >= -len(texto):      # Para cada caracter, y hasta que encuentre una letra, avanzo en el string (der a izq)
        if es_letra(texto[i]):                      # Encuentro una leta ---> No avanzo y salgo del while
            encontrado = True
        else:                                       # No encuentro letra ---> Avanzo y no salgo del while
            i -= 1 

    indice_inicio = i                               # El indice de inicio es el de la primera letra que encontre, y no lo vuelvo a tocar
    indice_fin = i                                  # El indice de fin, por ahora, es el de la primera letra (podria ser una palabra de 1 letra)
    i -= 1
    
    encontrado = False
    while not encontrado and i >= -len(texto):      # Para cada caracter, y hasta que encuentre algo que NO sea letra, avanzo (der a izq) en el string
        if es_letra(texto[i]):                      # Encuentro una letra ---> Ahora es la ultima letra encontrada (la palabra, por ahora,
            indice_fin = i                          # termina aca)
            i -= 1
        else:                                       # Encuentro algo que no es letra ---> El caracter anterior es la ultima letra cde la primera
            encontrado = True                       # palabra
    
    palabra_invertida = texto[indice_inicio : indice_fin - 1 : -1]          # Recorto (y la palabra queda invertida)
    return palabra_invertida[::-1]                                          # Invierto la palabra y retorno

"""
# Prueba de la funcion ultima_palabra()
# NO es parte del ejercicio

ultima = ultima_palabra('¡Hola! Buenos dias.')
print(ultima)          # 'dias'
print(len(ultima))     # 4

ultima = ultima_palabra('buenos dias')
print(ultima)          # 'dias'
print(len(ultima))     # 4

ultima = ultima_palabra('hola')
print(ultima)          # 'hola'
print(len(ultima))     # 4

ultima = ultima_palabra('')
print(ultima)          # ''
print(len(ultima))     # 0
"""

def caracter_a_minuscula(caracter):
    """
    Toma un caracter y devuelve:
    * El caracter pasado a minuscula si es una letra mayuscula
    * El mismo caracter si es una letra minuscula o cualquier otro simbolo
    
    Ej:
    caracter_a_minuscula('a')   devuelve 'a'
    caracter_a_minuscula('2')   devuelve '2'
    caracter_a_minuscula('_')   devuelve '_'
    caracter_a_minuscula('T')   devuelve 't'
    """
    if 'A' <= caracter <= 'Z':  # Si es una mayuscula
        res = chr(ord(caracter) + 32)       # Lo convierto
    else:                       # Si ya es minuscula (o es cualquier otro simbolo)
        res = caracter                      # Lo dejo como esta
    return res

"""
# Casos de prueba de caracter_a_minuscula()

print(caracter_a_minuscula('a'))
print(caracter_a_minuscula('2'))
print(caracter_a_minuscula('_'))
print(caracter_a_minuscula('T'))
"""

def a_minuscula(palabra):
    """
    Recibe un string y lo convierte todo en minuscula.
    Nota: embebiendo la funcion caracter_a_minuscula en esta misma funciona igual para 1 solo caracter que 
          para un string mas largo, pero se pretende mostrar con esto el concepto de modularizacion
    """
    res = ''                        # String nuevo que voy a devolver (recordar que los strings son inmutables, no puedo modificar el original)
    for caracter in palabra:        # Para cada caracter
        res += caracter_a_minuscula(caracter)       # Lo convierto, si es necesario
    return res

def principioFin(texto):
    if texto == '':                                                                     # EXTRA: para el texto vacio devuelvo False
        res = False                                                                     # (pues no tiene palabras)
        
    elif a_minuscula(primera_palabra(texto)) == a_minuscula(ultima_palabra(texto)):     # Si la primera y la ultima coinciden pasadas a minuscula
        res = True                                                                      # Cumple condicion
        
    else:                                                                               # Sino
        res = False                                                                     # NO cumple condicion
    return res

    # Tambien funciona:
    # return a_minuscula(primera_palabra(texto)) == a_minuscula(ultima_palabra(texto))

"""
# Casos de prueba de la funcion principioFin():

print(principioFin('Barón!, urgente ya ha nacido! Es un varón!'))                               # False
print(principioFin('Entre que ya se vienen los hombres de enfrente'))                           # False
print(principioFin('Hombre de poca fe, he dicho! Vamos, vamos hombre!'))                        # True
print(principioFin('_____¡esTA es una prueba adicional de este ejercicio ESTa---...._+_+_+'))   # True
print(principioFin('buenas'))                                                                   # True
print(principioFin(''))                                                                         # False
"""

def main():
    texto = input('Ingrese un texto: ')
    if principioFin(texto):
        print('El texto cumple la condición.')
    else:
        print('El texto NO cumple la condición.')

main()
