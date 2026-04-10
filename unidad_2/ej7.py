"""
Ejercicio 7:

Programar la función justificado que reciba una frase fra y un valor natural ancho
como parámetros. La función debe retornar un string de un tamaño total ancho, que
comienza y termina con comillas simples y que contiene a la frase fra, justificada a la
derecha y rellena con espacios a la izquierda.
Utilizarla en un programa en que se solicite al usuario la frase y el ancho deseado, se
invoque a la función y se imprima por pantalla el valor retornado.
"""

"""
IDEA:

En Python, se pueden multiplicar strings por numeros enteros para repetir el string.

'hola' * 2 resulta 'holahola'
'hola' * 5 resulta 'holaholaholaholahola'

y al usar cero o numeros negativos como multiplicadores, resulta el string vacio (len("") = 0)

'hola' * 0 resulta ''
'hola' * -1 resulta ''
'hola' * -5 resulta ''
'hola' * -500 resulta ''

Esto me permite "suprimir" strings, que es justo lo que se hace en este ejercicio. Cuando el ancho
provisto es menor o igual al necesario para contener a la frase y las dos comillas, entonces
cantidad_espacios resulta cero o negativa, por lo que " " * cantidad_espacios resulta en el string 
vacio "".
"""

def justificado(fra, ancho):
    # Determinar la cantidad de espacios que va a haber a la izquierda de la frase
    cantidad_espacios = ancho - len(fra) - 2

    # Armar el string de retorno
    # Se compone de:
    # - Comilla
    # - Una cantidad variable de espacios (se repite el espacio cantidad_espacios veces)
    # - La frase
    # - Comilla
    ret = "'" + " " * cantidad_espacios + fra + "'"

    # Retornar el resultado
    return ret

def main():
    frase = input('Ingrese la frase: ')
    ancho = int(input('Ingrese el ancho total a ser usado: '))

    resultado = justificado(frase, ancho)

    print(resultado)

main()
