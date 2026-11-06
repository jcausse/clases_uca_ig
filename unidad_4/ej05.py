"""
Ejercicio 5:

Desarrollar una función booleana que reciba como parámetro un número entero de
cuatro cifras y determine si el número cumple la condición de que la suma de las
unidades y las centenas es igual a la suma de las decenas y las unidades de mil. Luego
realizar un programa que encuentre e imprima un listado con todos los números de 4
cifras que cumplan la condición anteriormente citada. Por ejemplo, el número 7821
cumple esta condición ya que 1 + 8 = 2 + 7.
"""

def cumple_condicion(n):
    """
    Dado un número n de 4 cifras (1000-9999), determina si la suma de las
    unidades y centenas es igual a la suma de las decenas y las unidades de mil
    """
    unidades        = (n // (10 ** 0)) % 10
    decenas         = (n // (10 ** 1)) % 10
    centenas        = (n // (10 ** 2)) % 10
    unidades_mil    = (n // (10 ** 3)) % 10
    
    return unidades + centenas == decenas + unidades_mil

def main():
    for n in range(1000, 10000):
        if cumple_condicion(n):
            print(n)

main()
