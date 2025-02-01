"""
Ejercicio 3:

Desarrollar una función que reciba un número real como parámetro y que retorne un                           
mensaje si el número es ​“positivo”, “negativo” o “cero”​. Adicionalmente deberá                     
desarrollar otra función, que retorne otro mensaje, si el número recibido es ​“entero                         
natural”, “entero” o “real”​. El programa principal deberá efectuar el ingreso de                       
un número real e imprimir por pantalla los mensajes retornados por las funciones.                        
"""

def signo(x):
    if x > 0:
        ret = 'positivo'
    if x < 0:
        ret = 'negativo'
    if x == 0:
        ret = 'cero'
    return ret

def tipo(x):
    if x == int(x): # int(x) se queda con solo la parte entera. Si x es igual a su parte entera, es un numero entero (no tiene parte fraccionaria)
        if x > 0:
            ret = 'entero natural'
        else:
            ret = 'entero'
    else:
        ret = 'real'
    return ret
 
def main():
    x = float(input('Ingrese un numero: '))
    print(x, 'es', signo(x), 'y', tipo(x))

main()