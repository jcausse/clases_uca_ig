"""
Ejercicio 6:

Desarrollar una función booleana que retorne verdadero (True) en el caso de que una                           
frase recibida como parámetro sea palíndroma y falso (False) si no lo es. Una frase es                               
palíndroma cuando leída al derecho o al revés dice lo mismo. Desde el programa                           
principal ingresar por teclado una frase, invocar a la función y mostrar por pantalla un                             
mensaje que indique si la frase es o no es palíndroma.
"""

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

def quitar_acento(c):
    """
    Recibe un caracter, y, si es una vocal acentuada, la devuelve sin acentuar.
    Ej:
        quitar_acento('Ú') devuelve 'U'
        quitar_acento('1') devuelve '1'
        quitar_acento('á') devuelve 'a'
        quitar_acento('a') devuelve 'a'
    """
    if c == 'á':
        res = 'a'
    elif c == 'é':
        res = 'e'
    elif c == 'í':
        res = 'i'
    elif c == 'ó':
        res = 'o'
    elif c == 'ú':
        res = 'u'
    elif c == 'Á':
        res = 'A'
    elif c == 'É':
        res = 'E'
    elif c == 'Í':
        res = 'I'
    elif c == 'Ó':
        res = 'O'
    elif c == 'Ú':
        res = 'U'
    else:
        res = c
    return res

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

def preparar_frase(frase):
    """
    Esta funcion elimina todo lo que no sea una letra (espacios, numeros, signos de puntuacion, etc.),
    quedandose con todas las palabras juntas. Ademas, convierte todo a minuscula y quita acentos.
    Ej:
        preparar_frase('Así Ramona va, no Marisa') devuelve 'asiramonavanomarisa'
    """
    res = ''
    for c in frase:             # Para cada caracter en la frase
        c = quitar_acento(c)    # Le quito el acento (si tiene) para que es_letra() la reconozca
        if es_letra(c):         # Si es una letra
            res += caracter_a_minuscula(c)  # La paso a minuscula y la agrego
    return res

"""
# Casos de prueba para preparar_frase()

print(preparar_frase('Así Ramona va, no Marisa'))   # 'asiramonavanomarisa'
"""

def es_palindromo(frase):
    """
    Devuelve True si la frase es palindroma (se lee igual del derecho que del reves), o False en caso contrario.
    
    Esta version no es la mas eficiente, y lo que hace es chequear si al invertir la frase coincide con la frase
    (con el slice [::-1] del derecho.
    
    NOTA:
    Esta funcion pretende ser SIMPLE, por mas que no sea la forma mas eficiente de hacerlo.
    La forma mas eficiente es leer con dos indices: de izq. a der. y de der. a izq.. En este caso:
    * Si en algun momento difieren, no es palindroma
    * Si los indices llegan al centro y no difieren las frases, es palindroma
    """
    frase = preparar_frase(frase)       # Preparo la frase
    if frase == frase[::-1]:            # Si la frase coincide con si misma dada vuelta
        res = True                      # Es palindroma
    else:
        res = False                     # Sino, no
    return res

def es_palindromo_eficiente(frase):
    """
    Version eficiente de la funcion anterior
    """
    frase = preparar_frase(frase)
    i = 0
    palindroma = True                               # Asumo que es palindroma
    while palindroma and i < len(frase) // 2:       # Mientras lo sea, y hasta que llegue a la mitad del string
        if frase[i] != frase[len(frase) - i - 1]:   # Comparo cada caracter con su homologo en la segunda mitad (primero
            palindroma = False                      # vs ultimo, segundo vs penultimo, tercero vs antepenultimo, ... )
        i += 1
    return palindroma                               # Si no coinciden deja de ser palindroma. Si llega al medio y coinciden, es.

"""
# Casos de prueba

print(es_palindromo('Sólo dí sol a los ídolos'))        # True
print(es_palindromo('No deseo ese don'))                # True
print(es_palindromo('Somos o no somos'))                # True
print(es_palindromo('Así Mario oirá misa'))             # True
print(es_palindromo('La pala'))                         # False
print(es_palindromo('Así Ramona va, no Marisa'))        # True
print('------------------------------------')
print(es_palindromo_eficiente('Sólo dí sol a los ídolos'))        # True
print(es_palindromo_eficiente('No deseo ese don'))                # True
print(es_palindromo_eficiente('Somos o no somos'))                # True
print(es_palindromo_eficiente('Así Mario oirá misa'))             # True
print(es_palindromo_eficiente('La pala'))                         # False
print(es_palindromo_eficiente('Así Ramona va, no Marisa'))        # True
"""

def main():
    texto = input('Ingrese una frase: ')
    if es_palindromo(texto):
        print('La frase es palíndroma!')
    else:
        print('La frase no es palíndroma')

main()
