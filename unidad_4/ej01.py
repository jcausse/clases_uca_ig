"""
Ejercicio 1:

Desarrollar un programa en el que se ingrese por teclado números enteros hasta que
se hayan ingresado 5 números pares e informar por pantalla si alguno de ellos es
también múltiplo de cuatro.
"""

CANTIDAD_PARES = 5

def get_even_number():
    done = False            # Flag de que el ingreso es valido
    while not done:         # Mientras el flag no este en True
        num = int(input('Ingrese numero entero: '))
        if num % 2 == 0:    # Si es par
            done = True     # Marco que la entrada fue valida, lo que hace que pueda salir del ciclo
    return num              # El ciclo while anterior me ASEGURA que, si llego hasta aca, "num" es par

def main():
    for i in range(CANTIDAD_PARES):
        num = get_even_number() # No retorna hasta que no se ingrese un numero par
        print('Numero Par. ', end='')
        if num % 4 == 0:
            print('Tambien es multiplo de 4. ', end='')
        print('Cantidad de numeros pares ingresados: {}'.format(i + 1))
    
main()
