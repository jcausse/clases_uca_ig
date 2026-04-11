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


def main():
    print('Deben dar verdadero:')
    print(es_perfecto(6))       # True
    print(es_perfecto(28))      # True
    print(es_perfecto(496))     # True
    print(es_perfecto(8128))    # True    

    print('Deben dar falso:')
    print(es_perfecto(8))       # False
    print(es_perfecto(495))     # False
    print(es_perfecto(497))     # False
    print(es_perfecto(9000))    # False

main()
