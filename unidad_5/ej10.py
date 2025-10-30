"""
Ejercicio 10:

Desarrollar una función que reciba un texto t y una palabra p como parámetros, y                             
retorne verdadero si encuentra al menos una palabra en t conformada exactamente                       
con los mismos caracteres que conforman p sin importar el orden de los mismos en la                               
palabra. Desde el programa principal ingresar por teclado el texto y la palabra, invocar a                             
la función y mostrar por pantalla un mensaje que indique si cumple o no con la                               
condición.
"""

def verificar_palabra(p_texto, p):
    """
    Verifica si la palabra del texto, p_texto, esta formada exactamente por los caracteres
    de la otra palabra, p.
    No puede haber ningun caracter en p_texto que no este en p, ni viceversa (sin importar las
    repeticiones que cada caracter tenga en cada palabra, los caracteres pueden estar tanto 
    una sola vez como repetidos en ambas palabras, sin cambiar el resultado.)
    Se asume que tanto p_texto como p estan en minusculas.
    Ejemplos:
    - p_texto = 'baila', p = 'bala' devuelve False
    - p_texto = 'alla', p = 'al' devuelve True
    - p_texto = 'casa', p = 'saca' devuelve True
    - p_texto = 'alla', p = 'halla' devuelve False
    """
    # Verifico que todos los caracteres de p_texto esten en p
    cumple = True                           # Arranco asumiendo que van a cumplir la condicion
    i = 0
    while i < len(p_texto) and cumple:      # Para cada caracter en p_texto
        if p_texto[i] not in p:             # Si el caracter no esta en p, deja de cumplir
            cumple = False                  # Al hacer cumple = False, se corta el ciclo
        i += 1

    # Verifico que todos los caracteres de p esten en p_texto. Esto puede ser mas eficiente, pero lo
    # hacemos asi por simplicidad
    if cumple:                              # Solo hago la verificacion en el caso de que lo anterior
        i = 0                               # lo siga cumpliendo
        while i < len(p) and cumple:        # Para cada caracter en p
            if p[i] not in p_texto:         # Si el caracter no esta en p_texto, deja de cumplir
                cumple = False              # Al hacer cumple = False, se corta el ciclo
            i += 1
    
    return cumple                           # Si cumple se hizo false, devuelve False (porque no cumple)
                                            # Caso contrario, devuelve el True inicial

# Casos de prueba:
"""
print(verificar_palabra('baila', 'bala'))   # False
print(verificar_palabra('alla', 'halla'))   # False
print(verificar_palabra('alla', 'al'))      # True
print(verificar_palabra('casa', 'saca'))    # True
print(verificar_palabra('casa', 'casa'))    # True
"""

def verificar_texto(t, p):
    cumple = False
    i = 0
    inicio = 0                                      # Indice de inicio para recortar la palabra
    fin = 0                                         # Indice de fin para recortar la palabra
    while i < len(t) and not cumple:                # Para cada caracter en el texto, y mientras no se cumpla la condicion
        if t[i] == ' ':                             # Si es un espacio, aca termina una palabra y arranca otra
            fin = i                                 # Marco el fin de la palabra actual
            # Si la palabra actual cumple la condicion, verificar_palabra me devuelve True, por lo que la variable cumple
            # se hace True, y el ciclo corta. Si devuelve False, cumple se mantiene en False, y continua el ciclo
            cumple = verificar_palabra(t[inicio:fin], p)
            inicio = i + 1                          # Marco el inicio de la palabra siguiente
        i += 1
    
    # Verifico la ultima palabra aparte, pero solo si no hubo una palabra antes que cumpla
    if not cumple:
        cumple = verificar_palabra(t[inicio:len(t)], p)

    return cumple

def main():
    t = input('Ingrese texto: ')
    p = input('Ingrese palabra: ')
    if verificar_texto(t, p):
        print('Se cumple la condicion.')
    else:
        print('NO se cumple la condicion.')

main()
