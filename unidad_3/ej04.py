"""
Ejercicio 4:

Desarrollar una función booleana que reciba como parámetro dos números enteros (que                       
no están en orden) y valide si la resta entre el número mayor y el número menor es un                                     
valor que se encuentra entre ambos números (es decir, la diferencia es mayor e igual que el                                 
más chico y menor e igual que el más grande de los valores recibidos). Escribir un programa                                 
que ingrese por teclado los dos valores, invoque a la función y muestre por pantalla si                               
cumplen o no con la condición.
"""

def condicion(a, b):
    # Si a < b, los intercambio para que el mas grande quede en a y el mas chico en b
    if a < b:                           # Suponer a = 3, b = 9
        aux = a                         # Guardo el valor de a en una nueva variable (aux = 3)
        a = b                           # Paso el valor de b (9) a la variable a (a = 9)
        b = aux                         # Paso el valor guardado auxiliarmente (3) a b (b = 3)

    # Sabiendo que ahora a >= b
    dif = a - b                         # Defino en una variable la diferencia entre a y b
    return b <= dif and dif <= a        # Si b <= dif <= a, la expresion da True y se retorna True
                                        # Si no cumple, la expresion da False y se retorna False

def main():
    a = int(input('Ingrese un número A: '))
    b = int(input('Ingrese un número B: '))

    if condicion(a, b):                 # condicion(a, b) devuelve True o False (es funcion booleana)
        print('SI cumple condicion.')   # Cuando me devuelve True
    else:
        print('NO cumple condicion.')   # Cuando me devuelve False

main()
