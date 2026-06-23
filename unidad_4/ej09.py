"""
Ejercicio 9:

Desarrollar una función booleana que reciba como parámetro un número entero positivo
(de hasta nueve cifras) y retorne verdadero (True) si es capicúa o falso (False) en caso
contrario. Un número capicúa es aquel que leído de izquierda a derecha es igual que
leído de derecha a izquierda. Por ejemplo 82428 es capicúa.
Desarrollar un programa que solicite un número por teclado e informe si éste es capicúa
o no según el resultado retornado por la función.

Ayuda: Para programar la función considere invertir el número y luego compararlo con el
número original, si resultan iguales, entonces es capicúa.
"""

def capicua(n):
    cant_digitos = len(str(n))                  # Cantidad de digitos del numero
    num_invertido = 0                           # Aca voy a dejar el numero dado vuelta
    for i in range(cant_digitos):               # Para cada exponente i
        digito = ((n // (10 ** i)) % 10)        # Obtengo el i-esimo digito correspondiente al exponente
        peso = 10 ** (cant_digitos - 1 - i)     # Calculo el nuevo peso de ese digito al dar vuelta el numero
        num_invertido += digito * peso          # Agrego al numero invertido el digito con su nuevo peso
    return num_invertido == n                   # Si n es igual al invertido, n es capicua

def main():
    n = int(input('Ingrese un numero: '))
    if n < 0:
        print('El numero no puede ser negativo.')
    elif capicua(n):
        print('{} es capicua.'. format(n))
    else:
        print('{} no es capicua.'. format(n))

main()
