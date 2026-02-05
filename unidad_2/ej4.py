"""
Ejercicio 4:

Programar las funciones areaCirc, areaCuad y areaNegra.

areaCirc recibe como parámetro el diámetro de un círculo y calcula y retorna el área del mismo.
areaCuad recibe como parámetro el lado de un cuadrado y calcula y retorna el área del mismo.
areaNegra recibe como parámetro el lado de un cuadrado de una figura (como la dada a continuación) y calcula y retorna el área negra resultante.

Luego utilizar las funciones en un programa que solicitará al usuario el lado del cuadrado
y mostrará por pantalla el valor correspondiente para el área de color negra y además
indicará el porcentaje que éste área representa con respecto al área total del cuadrado.
Notar que dado el lado del cuadrado, la proporción de tamaño entre este y los círculos
siempre es la misma y esta proporción se debe deducir con los valores del ejemplo dado
a continuación.
"""

import math

# AreaCirculo = pi * radio^2 = pi * (diametro / 2)^2
# pi es math.pi
def areaCirc(diametro):
    return math.pi * (diametro / 2) ** 2

def areaCuad(lado):
    return lado * lado

# AreaNegra = AreaCuadrado - AreaCirculoGrande - 2 * AreaCirculoChico
def areaNegra(lado):
    return areaCuad(lado) - areaCirc((2 / 3)  * lado) - 2 * areaCirc((1 / 3)  * lado)

def main():
    lado = float(input('Ingrese el lado: '))            # Pido el lado
    area_negra = areaNegra(lado)                        # Calculo el area negra
    porcentaje = area_negra * 100 / areaCuad(lado)      # Calculo el porcentaje
    
    # :.2f le indica a Python que imprima redondeado a 2 decimales
    print('El area negra es {:.2f} y es un {:.2f}% del area total del cuadrado'.format(area_negra, porcentaje))

main()
