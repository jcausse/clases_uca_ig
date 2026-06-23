"""
Ejercicio 8:

Desarrollar una función que reciba por parámetro un texto (string) y retorne un nuevo                           
texto (string), con el mismo texto, con todas sus palabras con la primera letra en                             
mayúscula. 
Desde el programa principal ingresar por teclado un texto, invocar a la función y mostrar                             
por pantalla el resultado que retorna la función.

Ejemplo:

Entrada:    Soy el hombre más sabio de la tierra
Salida:     Soy El Hombre Más Sabio De La Tierra
"""

# Funcion booleana que me dice si un caracter es una letra minuscula
def es_minuscula(c):
    return 'a' <= c and c <= 'z'
    
# Funcion booleana que me dice si un caracter es una letra mayuscula
def es_mayuscula(c):
    return 'A' <= c and c <= 'Z'

########################################################################################
# Ayuda:                                                                               #
# - chr: le das un numero (un ordinal), te devuelve el caracter (str de len = 1)       #
# - ord: le das un caracter, te devuelve su numero (su ordinal)                        #
#                                                                                      #
# Suponiendo que c es una mayuscula                                                    #
# chr(ord(c) + 32)                                                                     #
# - ord(c) -> obtiene su valor ASCII (Ejemplo: ord('A') obtiene 65)                    #
# - ord(c) + 32 -> le suma 32 a ese valor ASCII obteniendo el valor ASCII de la        #
#                  minuscula correspondiente (Ejemplo: 65 + 32 = 97 = ord('a'))        #
# - chr(ord(c) + 32) -> convierto ese valor que sume a caracter (chr(97) devuelve 'a') #
########################################################################################

# Funcion que recibe un caracter c y lo convierte a letra minuscula
# Si c no es una letra o ya es minuscula lo deja como esta
def a_minuscula(c):
    if es_mayuscula(c):
        c = chr(ord(c) + 32)
    return c
    
# Funcion que recibe un caracter c y lo convierte a letra mayuscula
# Si c no es una letra o ya es mayuscula lo deja como esta
def a_mayuscula(c):
    if es_minuscula(c):
        c = chr(ord(c) - 32)
    return c

def capitalize(s):
    ret = ''
    primera_letra = True
    for c in s:
        if c == ' ':                    # Si c es espacio:
            ret += ' '                  #   - Agrego un espacio
            primera_letra = True        #   - La letra siguiente es primera letra
        elif primera_letra:             # Si no es espacio pero es primera letra:
            ret += a_mayuscula(c)       #   - Agrego la letra actual pasada a mayuscula
            primera_letra = False       #   - Cambio el flag porque la letra siguiente ya no es primera letra
        else:                           # Si no es ni espacio ni primera letra, es una letra del medio:
            ret += a_minuscula(c)       #   - La agrego pasada a minuscula
        
    return ret
        
def main():
    s = input('Ingrese un texto: ')  
    print('La función ha retornado:', capitalize(s))
    
main()
