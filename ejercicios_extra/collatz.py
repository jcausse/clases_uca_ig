# Ejercicio: Escribir un programa que permita mostrar la cantidad de pasos hasta llegar al 1
# para un numero n cualquiera, segun la conjetura de Collatz

# https://en.wikipedia.org/wiki/Collatz_conjecture

# Hacer un programa principal main que permita al usuario ingresar un numero y muestre por pantalla:
# - Todos los numeros por los que paso hasta llegar al 1
# - La cantidad de pasos totales

# Por ejemplo, para n = 3 imprime las siguientes 4 lineas:

# Valor de n inicial: 3
# Numeros generados:
# 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Cantidad de pasos: 7

# Al imprimir los numeros, imprimir 15 por linea de salida

#######################################################################################################

def collatz(n):
    if n % 2 == 0:
        ret = n // 2
    else:
        ret = 3 * n + 1
    return ret
    
def main():
    n = int(input('Ingrese el valor de n: '))
    pasos = 0

    print('Valor de n inicial: {}'.format(n))
    
    # Iterar hasta que n sea 1 (mientras que n sea mayor que 1)
    while n > 1:
        
        # Contar el paso
        pasos += 1
        
        # Calcular el siguiente n
        n = collatz(n)
        
        # Imprimir el n
        print(n, end='')
        
        # Solo imprimir la flecha cuando no se haya llegado al final
        if n > 1:
            print(' -> ', end='')
        
        # Saltar a la linea de abajo cada vez que se hayan impreso ya 15 numeros
        if pasos % 15 == 0:
            print()
    
    print('\nCantidad de pasos: {}'.format(pasos)) # Solo para que se vea un salto de linea
    
main()
