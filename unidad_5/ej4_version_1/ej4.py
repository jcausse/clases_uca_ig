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
# * Un signo de puntuacion
# * Cualquier otra cosa que no sea una letra

def es_letra(c):
    """
    Esta funcion devuelve True o False segun c sea un caracter o no, respectivamente
    """
    return ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z')

def caracter_a_minuscula(caracter):
    """
    Toma un caracter y devuelve:
    * El caracter pasado a minuscula si es una letra mayuscula
    * El mismo caracter si es una letra minuscula o cualquier otro simbolo

    ord: le paso un caracter y me devuelve el numero que lo representa
    chr: le paso un numero, y me devuelve el caracter que es representado por ese numero
    
    Ej:
    caracter_a_minuscula('a')   devuelve 'a'
    caracter_a_minuscula('2')   devuelve '2'
    caracter_a_minuscula('_')   devuelve '_'
    caracter_a_minuscula('T')   devuelve 't'
    """
    if 'A' <= caracter and caracter <= 'Z':         # Si es una mayuscula
        caracter = chr(ord(caracter) + 32)          # Lo convierto, y luego lo devuelvo        
    return caracter                                 # Si ya es minuscula (o es cualquier otro simbolo), lo dejo como esta

# OBS: Como convierto un caracter a mayuscula?
# def caracter_a_mayuscula(caracter):
#     if 'a' <= caracter and caracter <= 'z':
#         caracter = chr(ord(caracter) - 32)     
#     return caracter            

def principioFin(texto):
    palabra_actual = ''
    primera_palabra = ''
    ultima_palabra = ''
    
    for c in texto:                                 # En cada vuelta del ciclo, trae el siguiente caracter a la variable c
        if es_letra(c):                             # Si es una letra, forma parte de una palabra
            c = caracter_a_minuscula(c)             # Convierto la letra actual a una minuscula (si fuere mayuscula), y sino, queda igual                         
            palabra_actual += c                     # La agrego a la palabra actual
        elif palabra_actual != '':                  # Si no es una letra y la palabra actual no esta vacia, la tengo en cuenta
            if primera_palabra == '':               # Si en primera_palabra hay un string vacio
                primera_palabra = palabra_actual    # Guardo la palabra actual, que es la primera, en primera_palabra, que nunca vuelve a ser el string vacio
            ultima_palabra = palabra_actual         # Guardo la palabra actual en ultima_palabra
            palabra_actual = ''                     # Reinicio la palabra actual

    if palabra_actual != '':                        # Caso borde: si el ultimo caracter es una letra, no se copiaba la palabra_actual a ultima_palabra
        ultima_palabra = palabra_actual             # Entonces lo hago a mano
    
    # Cuando no hay mas caracteres, el ciclo corta
    # primera_palabra tiene la primera palabra de toda la frase
    # ultima_palabra tiene la ultima palabra de todas
    return primera_palabra == ultima_palabra        # Si las palabras son iguales, el == da True y devuelve True. Sino, devuelve False

def main():
    res = principioFin("Hombre de poca fe, he dicho! Vamos, vamos hombre!")
    print(res)

main()
