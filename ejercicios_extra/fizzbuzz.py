"""
FizzBuzz: https://en.wikipedia.org/wiki/Fizz_buzz

Parte 1: Implementar un programa con un ciclo for que imprima todos 
los números del 1 al 100 inclusive.

Parte 2: Modificar el programa de manera tal que, para cada número:
- Si el número no es múltiplo ni de 3 ni de 5, imprima el mismo número
- Si es múltiplo de 3 pero no de 5, imprima "Fizz"
- Si es múltiplo de 5 pero no de 3, imprima "Buzz"
- Si es múltiplo de 3 y de 5, imprima "FizzBuzz"

Parte 3: Hacer otra versión, pero con un while.
"""

def fizzbuzz_for():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:   # <--- Este chequeo DEBE ir primero
            print('FizzBuzz')           # porque sino los otros chequeos por multiplo de 3
        elif n % 3 == 0:                # o de 5, si dan True, impiden al de FizzBuzz que
            print('Fizz')               # imprima su mensaje
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

def fizzbuzz_while():
    n = 1
    while n <= 100:
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)
        n += 1

def main():
    # fizzbuzz_for()
    fizzbuzz_while()

main()
