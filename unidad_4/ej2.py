"""
Ejercicio 2:

Desarrollar un programa en el que se ingresen por teclado una cantidad indefinida de
números enteros positivos hasta que se ingrese 0. A continuación el programa debe
indicar por pantalla cuál fue el mayor y cuál el menor.
"""

def main():
    print('Ingrese numeros enteros positivos (finalice con 0):')

    maximo = 0                          # Aca guardo el maximo encontrado. Empieza en 0 porque cualquier numero
                                        # positivo que el usuario ingrese es mas grande que 0
    minimo = None                       # Aca guardo el minimo. Empiezo en None para indicar que no tengo valor

    done = False                        # Flag que indica si debo seguir o salir del ciclo
    while done == False:                # Mientras el flag siga en False
        n = int(input('> '))            # Ingreso un numero
        if n == 0:                      # Solamente cuando el numero sea 0, cambio el valor
            done = True                 # del flag a True, lo que va a provocar que el ciclo se rompa
        elif n < 0:                     # Le mostramos un mensaje al usuario si ingresa un numero negativo
            print('Recuerde que solo puede ingresar numeros positivos')
        else:
            if n > maximo:              # Si el usuario ingresa un numero mayor que el maximo
                maximo = n              # me quedo con ese numero como mi nuevo maximo
            if minimo == None or n < minimo:    # Si me ingresaron None o un numero menor que el minimo
                minimo = n              # me quedo con ese numero como menor
    
    if minimo == None:                  # Si nunca entre al else de arriba, el minimo va a seguir siendo None
        print('No se ingreso ningun numero positivo')                   # No hubo numeros validos
    else:                               # Si entre al menos 1 vez, el minimo va a ser un int
        print('El mayor es', maximo, 'y el menor es', minimo, '.')      # Imprimo lo que me piden

main()
