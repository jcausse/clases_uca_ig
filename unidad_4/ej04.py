"""
Ejercicio 4:

Desarrollar una función booleana que reciba como parámetro un número entero positivo
y retorne verdadero (True) o falso (False) según sea el número perfecto o no. Luego
utilizarla en un programa que encuentre y muestre por pantalla los primeros cuatro
números perfectos.
Definición: Un número perfecto es un entero positivo, que es igual a la suma de todos
los enteros positivos (excluido él mismo) que son divisores del número. Por ejemplo, el
primer número perfecto es 6, ya que los divisores de 6 son 1, 2, 3 y 1 + 2 + 3 = 6.
"""

# https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto


def es_perfecto(n):
    suma_divisores = 1              # Arranco en 1 porque, como el 1 divide a cualquier numero, si o si va a estar en la suma

    for i in range(2, n // 2 + 1):  # Como solo necesito ir hasta la mitad, calculo n // 2, y le sumo 1 para que tome ese ultimo numero
        if n % i == 0:              # Si n % i es cero, la division n // i no tiene resto, por lo que i divide a n (i es divisor de n)
            suma_divisores += i     # A la suma de divisores, le agrego i (ya que i es divisor de n)

    return n == suma_divisores      # La expresion n == suma_divisores produce un valor bool, y se devuelve ese valor

###########################################################
# Tests (no son parte del main):

# print('Deben dar verdadero:')
# print(es_perfecto(6))       # True
# print(es_perfecto(28))      # True
# print(es_perfecto(496))     # True
# print(es_perfecto(8128))    # True    

# print('Deben dar falso:')
# print(es_perfecto(8))       # False
# print(es_perfecto(495))     # False
# print(es_perfecto(497))     # False
# print(es_perfecto(9000))    # False
###########################################################

# Programa que encuentra los primeros 4 numeros perfectos

def main():
    contador = 0                # Cantidad de perfectos impresos hasta ahora
    i = 2                       # El numero con el que voy probando (el 1 no es perfecto por definicion)
    
    print('Primeros 4 numeros perfectos:')
    while contador < 4:
        if es_perfecto(i):      # Si encuentro uno perfecto
            print(i)            # Lo imprimo
            contador += 1       # Anoto que ya tuve 1 perfecto mas
        
        i += 1                  # Incremento el numero para probar con el siguiente
    
main()
