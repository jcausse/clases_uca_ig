"""
Ejercicio 7:

Desarrollar una función que reciba por parámetros dos textos: uno “largo” y otro “corto” y                             
retorne la cantidad de veces que se encuentra repetido el texto “corto” dentro del texto                             
“largo”. Desde el programa principal ingresar por teclado el texto largo y el texto corto a                               
buscar, luego invocar a la función y mostrar por pantalla el resultado que retorna.
"""

# Retorna si el texto 1 contiene al texto 2 de forma exacta a partir del caracter n
# Por ejemplo, si txt1 = 'murcielago', n = 6, txt2 = 'lago', retorna True
# Por ejemplo, si txt1 = 'murcielago', n = 6, txt2 = 'lagos', retorna False
# Por ejemplo, si txt1 = 'murcielago', n = 5, txt2 = 'lago', retorna False
# Por ejemplo, si txt1 = 'murcielago', n = 3, txt2 = 'ciel', retorna True
# Por ejemplo, si txt1 = 'murcielago', n = 3, txt2 = 'cielo', retorna False
# Si txt2 = '', retorna True para cualquier n valido y cualquier txt1
# Si n no es un indice valido para txt1, retorna False
def coincide_texto(txt1, n, txt2):
    if len(txt2) > len(txt1):               # txt2 no puede estar contenido en txt1 si es mas largo
        ret = False
    elif n < 0 or n >= len(txt1):           # Chequeo la validez de n
        ret = False
    elif txt2 == '':                        # Si n era valido y txt2 es vacio, retorna verdadero
        ret = True                          # (el string vacio siempre esta contenido)
    else:                                   # Caso general (ver ejemplo mas abajo)
        ix1 = n     # Indice txt1
        ix2 = 0     # Indice txt2

        # Si coinciden (ver ejemplo)
        while ix1 < len(txt1) and ix2 < len(txt2) and txt1[ix1] == txt2[ix2]:
            ix1 += 1    # Incremento los indices para seguir comparando
            ix2 += 1

        # Caso 1:   Se acabo el txt2 -> Retorna True. Si logro consumir el txt2 completo sin
        #           interrumpir el ciclo, es porque hubo una coincidencia
        if ix2 == len(txt2):
            ret = True

        # Caso 2:   No se acabo el txt pero si se acabo el txt1 -> No puede haber coincidencia
        #           porque al haberse cortado antes no puede contener a txt2 completo
        # Caso 3:   No se acabo ninguno de los dos, por lo que el ciclo se corto por 3ra
        #           condicion (falta de coincidencia)
        # Notar que el caso 2 y el 3 coinciden en lo que tienen que hacer
        else:
            ret = False

    return ret

"""
Ejemplo del caso general:

0 1 2 3 4 5 6 7 8 9
m u r c i e l a g o

0 1 2 3
l a g o

Si n = 6, busco que:
- txt1[6] == txt2[0]    (txt1 busco a partir de n, txt2 a partir de 0)
- txt1[7] == txt2[1]
- txt1[8] == txt2[2]
- txt1[9] == txt2[3]

---> Si alguna comparacion falla se corta el ciclo
---> Si se acaba el txt1 y no coincidieron todos los caracteres de txt2, debe dar False
---> Si se acaba el txt2 y coincidieron todos, se corta el ciclo y devuelve True

Condiciones del ciclo:
ix1 < len(txt1) -------------> Que no me pase del txt1
ix2 < len(txt2) -------------> Que no me pase del txt2
txt1[ix1] == txt2[ix2] ----> Que coincidan los caracteres
"""

# Retorna la cantidad de apariciones del texto largo dentro del corto
def apariciones(largo, corto):
    coincidencias = 0
    for i in range(len(largo)):
        if coincide_texto(largo, i, corto):
            coincidencias += 1
    return coincidencias

def main():
    largo = input('Ingrese el texto largo: ')
    corto = input('Ingrese el texto corto: ')
    n = apariciones(largo, corto)
    print('El texto corto se encontró {} veces en el texto largo'.format(n))

main()
