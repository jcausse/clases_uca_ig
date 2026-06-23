"""
Ejercicio 3:

Desarrollar una función esPrimo que reciba como parámetro un valor numérico y
determine si dicho número es primo o no, retornando verdadero (True) o falso (False)
respectivamente. Luego utilizar la función en un programa que solicite al usuario el
ingreso de una cantidad cant (número natural) y que muestre por pantalla dos listados:
primero un listado de los números primos comprendidos entre 1 y cant y luego otro
listado con los primeros cant números primos. Ambos listados se deben imprimir por
pantalla a 10 columnas
"""

def es_primo(n):
    # Casos particulares:
    if n < 2:           # Los negativos, el 0 y el 1 no son primos
        ret = False
    elif n == 2:        # El 2 es primo
        ret = True
    elif n % 2 == 0:    # Ningun par que sea > 2 es primo porque es
        ret = False     # divisible por 2
    
    # Caso general: Todos los numeros primos > 2 son impares. Este caso
    # solo trabaja con impares 
    else:
        ret = True                          # Chequeo optimista: ASUMO que es primo, y luego verifico que lo sea
        posible_divisor = 3                 # Empiezo a probar desde el 3

        # Mientras no me pase de la raiz cuadrada del numero y no me haya dado 
        # previamente que no es primo (ret no debe ser False)
        while posible_divisor < n ** (1/2) and ret == True:
            print('Probando con', posible_divisor, '...')
            if n % posible_divisor == 0:    # Si efectivamente n es divisible por el numero que pruebo
                ret = False                 # Entonces no es primo
                print('----> No es primo!')
            posible_divisor += 2            # Pruebo con el proximo impar

    return ret

# Oportunidad de mejora (opcional):
# 1. Fijarme que no sea par ni multiplo de 3. Entonces los posibles divisores seran todos de la forma 6k-1 o 6k+1.

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

def primos_hasta_n(n):              # n es el numero maximo a probar
    print('Primos entre 1 y {}:'.format(n))
    
    impresos = 0                    # Cantidad que imprimi hasta ahora (esto es para hacer que cada 10 cambie de linea). VER COMENTARIOS AL FINAL
    
    for i in range(2, n):           # Para cada numero entre 2 y n (el 1 nunca es primo por definicion matematica)
        if es_primo(i):             # Llama a la funcion es_primo(), y le pasa el numero. Si la func. devuelve True, es primo y entra al if. Si devuelve False no entra
            
            ##############################################################
            print('{:<10d}'.format(i), end='')  # VER COMENTARIOS AL FINAL
            impresos += 1                       # VER COMENTARIOS AL FINAL
            if impresos % 10 == 0:              # VER COMENTARIOS AL FINAL
                print()                         # VER COMENTARIOS AL FINAL
            ##############################################################
            
    print()                                     # Print vacio para que al final deje un espacio y la salida se vea ordenada
    
def primeros_n_primos(n):           # n es la cantidad de primos que quiero encontrar
    print('Primeros {} primos:'.format(n)) 
    
    i = 2                           # Proximo numero con el que voy a probar (empieza en 2)
    encontrados = 0                 # Numeros primos que encontre hasta ahora (contador)
    while encontrados < n:          # Mientras la cantidad de primos que encontre no llegue a la cantidad pedida
        if es_primo(i):             # Pruebo con el siguiente numero. Si es primo:
            encontrados += 1        # Incremento el contador (ya encontre uno mas). CUIDADO: Si me olvido esta linea, se forma un ciclo infinito.
            
            ##############################################################
            print('{:<10d}'.format(i), end='')  # VER COMENTARIOS AL FINAL
            if encontrados % 10 == 0:           # VER COMENTARIOS AL FINAL
                print()                         # VER COMENTARIOS AL FINAL
            ##############################################################
            
        i += 1                      # Avanzo al siguiente numero. CUIDADO: Si me olvido esta linea (o si la pongo dentro del if), se forma un ciclo infinito.
        
    print()                                     # Print vacio para que al final deje un espacio y la salida se vea ordenada
        
def main():
    n = int(input('Ingrese cantidad (numero natural): '))
    primos_hasta_n(n)
    primeros_n_primos(n)
    
main()

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# ALGORITMO PARA IMPRIMIR A 10 COLUMNAS (LO VEMOS DE MANERA INCREMENTAL)

# Recomendacion: ver especificadores de formato en:
# https://pyformat.info
# SIEMPRE CON EL FORMATO "NEW".

# Supongamos que queremos imprimir a 10 columnas los numeros del 0 al 86.
# Debe quedar:

"""
0   1   2   3   4   5   6   7   8   9
10  11  12  13  14  15  16  17  18  19
...
70  71  72  73  74  75  76  77  78  79
80  81  82  83  84  85  86
"""

# Notar que se imprimen siempre 10 numeros, y al imprimir 10 numeros se salta a la linea de abajo

### Paso 1: Imprimo los numeros del 0 al 86 

"""
i = 0
for i in range(87):
    print(i)
"""

### Paso 2: Imprimo una separacion (para que queden bien)

# Por ejemplo, puedo hacer que los numeros se impriman ocupando cada uno 8 caracteres, de manera que si el numero es:
# * 1: se imprime el 1 y se dejan 7 espacios
# * 123: se imprime 123 y se dejan 5 espacios

# Esto lo puedo hacer de manera autmatica con el format poniendo entre las llaves el especificador de formato 10d, de la siguiente forma:
# print('{:10d}'.format(i))
# * Las llaves {} le indican a format que, en ese lugar, debe poner el valor de la variable
# * El : dentro de las llaves indica que lo que viene a continuacion es un especificador de formato (que indica el formato a darle al valor de la variable)
# * El 10 indica que se debe imprimir el valor utilizando un ancho de 10 caracteres
# * La letra d indica que el valor a imprimir es un numero entero (esta parte puede omitirse)

# De forma automatica, esto alinea los caracteres a la derecha. Para alinearlos a la izquierda se pone despues de los : el signo de menor (<), quedando:
# print('{:<10d}'.format(i))

"""
i = 0
for i in range(87):
    print('{:<10d}'.format(i))
"""

# Notar que, como este fragmento de codigo imprime un numero debajo del otro, no se va a ver la diferencia con el paso anterior

### Paso 3: Hacer que todos lo numeros aparezcan uno al lado del otro

# Notemos que, en el paso anterior, todos los numeros aparecian uno debajo del otro. Esto es porque, por default, print() salta a la siguiente linea cada vez
# que se ejecuta. Si queremos que 10 de los numeros se impriman uno debajo del otro, esto no puede pasar. Para lograr el comportamiento final, debemos hacer que:
# (1) Cada print, de manera predeterminada, no salte de linea
# (2) Cada 10 prints, imprimir un salto de linea nosotros, de manera manual

# El apartado (1) sera el objetivo de esta parte, mientras que el (2), el de la parte 4.

# Para lograr que los print() no obedezcan al comportamiento predeterminado de poner un salto de linea al final, debemos indicarle que no lo haga utilizando el
# parametro especial "end". Este parametro permite decirle a print() lo que queremos que imprima al final de la linea. De forma predeterminada, "end" es un
# salto de linea (\n). Para decirle que no imprima nada (asi no salta de linea ni introduce caracteres indeseados), le decimos a print() que el "end" es un string
# vacio. Asi:
# * print('Hola') imprime "Hola" y salta a la siguiente linea
# * print('Hola', end='') imprime "Hola" y NO salta de linea

"""
i = 0
for i in range(87):
    print('{:<10d}'.format(i), end='')
"""

# Notar que aca se visualizan los espacios del paso anterior

### Paso 4:

# Hacemos que, cada 10, se imprima un enter. Esto lo logro verificando si (i + 1) % 10 == 0 e imprimiendo enter en ese caso.

"""
i = 0
for i in range(87):
    print('{:<10d}'.format(i), end='')
    if (i + 1) % 10 == 0:       # El + 1 es para que imprima el enter antes de la proxima vuelta
        print()                 # El print vacio no imprime nada, pero SI salta de linea
print()                         # Pongo otro print vacio para dejar un espacio
"""

# ------------------------------------------------------------------------------------------------------------------------------------------------- #
