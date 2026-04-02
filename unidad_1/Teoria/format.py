##################
### IMPORTANTE ###
##################

# En este apunte, los simbolos >< NO tienen nada que ver ni con print ni con format.
# Simplemente los uso para demarcar donde inicia y donde termina un valor reemplazado por format.
# La siguiente funcion prentende mostrar los espacios para hacerlo mas legible y que se entienda mejor.
# Ignorarla, ya que utiliza cosas que no vemos en informatica general

ejemplo_n = 1

def imprimir(s: str) -> None:
    global ejemplo_n
    start = f'Ejemplo {ejemplo_n}:'
    print(start + '\n' + '-' * len(start) + '\n')
    ejemplo_n += 1

    if len(s) > 0:
        print(f'>{s}<')
        print(' ' + '^' * len(s))
        if len(s) >= 10:
            print(' ', end='')
            for i in range(1, len(s) + 1):
                n = i // 10
                print(n if n > 0 else ' ', end='')
            print(' ')
        print(' ', end='')
        for i in range(1, len(s) + 1):
            print(i % 10, end='')
        print(' ')

    print('\n' + '-' * 80 + '\n')

###########################
### NUMEROS ENTEROS (d) ###
###########################

# Imprimir un numero entero con una determinada cantidad de espacios

# Ejemplo 1
# * Si el numero tiene menos digitos que la cantidad de espacios, se rellena con espacios vacios a la izquierda
s = '{:5d}'.format(38)
imprimir(s)

# Ejemplo 2
# * Si el numero tiene mas digitos que la cantidad de espacios, el especificador queda sin efecto
s = '{:5d}'.format(1234567)
imprimir(s)

# Ejemplo 3
# Imprimir un numero con una cantidad de digitos determinada, justificado a la izquierda
s = '{:<5d}'.format(38)
imprimir(s)

# Ejemplo 4
# Imprimir un numero con una cantidad de digitos determinada, rellenando con ceros
s = '{:05d}'.format(38)
imprimir(s)

# Ejemplo 5
# Imprimir la hora en formato hh:mm:ss
horas = 1
minutos = 14
segundos = 7
s = '{:02d}:{:02d}:{:02d}'.format(horas, minutos, segundos)
imprimir(s)

# Ejemplo 6
# Los numeros negativos se imprimen con el - de forma predeterminada, pero los positivos se imprimen
# sin signo de forma predeterminada. Imprimir un numero positivo con signo
s = '{:+d}'.format(38)
imprimir(s)

#################################
### NUMEROS FRACCIONARIOS (f) ###
#################################

# Ejemplo 7
# Imprimir un numero utilizando una cantidad fija de posiciones decimales
# Formato :.<CANTIDAD_DECIMALES>f
# Redondea para arriba si el siguiente decimal es >= 5

from math import pi     # Numero PI 3.14159265....
s = '{:.5f}'.format(pi)
imprimir(s)

# Ejemplo 8
# Imprimir un numero utilizando una cantidad fija de posiciones decimales, y una cantidad fija de posiciones
# de parte entera, y rellenando la parte entera con ceros
# Formato: :<CERO (opcional)><LARGO_TOTAL (opcional)>.<CANTIDAD_DECIMALES>f
# donde LARGO_TOTAL es largo de parte entera + CANTIDAD_DECIMALES + 1 (punto)

x = 25 + pi     # 28.141592...

# Quiero imprimir:
# 00028.14159
# 0: Rellenar con ceros
# 11: Largo total (5 parte entera + 1 punto + 5 decimales)
# .5: Cantidad de decimales
# f: float
s = '{:011.5f}'.format(x)
imprimir(s)

############################
### CADENAS DE TEXTO (s) ###
############################

# Ejemplo 9
# Imprimir una cadena de texto usando una cantidad fija de espacios
s = '{:10s}'.format('Python')
imprimir(s)

# Ejemplo 10
# Imprimir una cadena de texto usando una cantidad fija de espacios, justificado a la derecha
s = '{:>10s}'.format('Python')
imprimir(s)

# Ejemplo 11
# Imprimir una cadena de texto usando una cantidad fija de espacios, centrado
s = '{:^10s}'.format('Python')
imprimir(s)
