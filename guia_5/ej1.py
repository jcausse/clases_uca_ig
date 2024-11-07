"""
Ejercicio 1:

Desarrollar una función que reciba una palabra como parámetro y retorne otra palabra                         
conformada por tres copias de los últimos dos caracteres de la palabra recibida. La                           
palabra que recibida por parámetro debe tener un largo mínimo de dos caracteres en                           
caso contrario deberá retornar una palabra vacía. Desde el programa principal ingresar                       
por teclado una palabra, invocar a la función y mostrar por pantalla el resultado que                             
retorna la función tal como se ilustra en los siguientes ejemplos: 
 
Ingrese una palabra: hola  
La función ha retornado: lalala 
 
Ingrese una palabra: w  
La función ha retornado una palabra vacía
"""

def ejercicio1(palabra):
    if len(palabra) < 2:
        return ''
    return palabra[-2:] * 3 # palabra[-2:] son los últimos 2 caracteres de la palabra. * 3 repite esos 2 caracteres 3 veces.

def main():
    palabra = input('Ingrese una palabra: ')
    resultado = ejercicio1(palabra)
    if resultado == '':
        print('La función ha retornado una palabra vacía')
    else:
        print(resultado)
    
main()
