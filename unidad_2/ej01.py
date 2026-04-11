"""
Funciones:

* se definen usando la palabra "def"
* tienen un NOMBRE, que debe ser significativo: debe indicar que hace la funcion de forma breve
* pueden no recibir PARAMETROS, o tener uno o mas de ellos, en cuyo caso se debe:
  * especificar un nombre para cada uno
  * separarlos con comas

def <NOMBRE> (<PARAMETRO 1>, <PARAMETRO 2>, <PARAMETRO 3>, ..., <PARAMETRO N>):
    <CUERPO>

* puede no retornar nada (no me interesa que devuelva ningun valor), en cuyo caso retornara "None" o retornar
  algun valor en especifico que nosotros indiquemos usando la palabra "return"
  * return 2        # Devuelve el valor 2 de tipo int.
  * return 3.5      # Devuelve el valor 3.5, de tipo float.
  * return          # Devuelve None.
  * no pongo return # La funcion termina cuando se alcanza el final de la misma (y devuelve None).
* una vez alcanzado un return, la ejecucion de la funcion termina (no se sigue ejecutando el codigo de la misma)

* puedo invocar a la funcion mediante su nombre, y poniendo entre parentesis los parametros que necesita recibir.
  * area = area_triangulo(lado1, lado2, lado3)
    * llama a la funcion area_triangulo, pasandole como parametros el lado1, el lado2 y el lado3, en ese orden
    * la funcion retornara un valor (el area del triangulo), que se guardara en la variable "area"
"""

"""
Ejercicio 1:

Programar una función que reciba como parámetros la longitud de los lados de un                           
triángulo y que retorne el área del mismo. Utilizarla en un programa que solicite al                             
usuario los datos, invoque a la función e informe el área calculada. Todos los datos y                               
textos que se muestren por pantalla en este y en todos los ejercicios de la presente guía                                 
deben respetar estrictamente el formato de los ejemplos dados.
"""

def area_triangulo(lado1, lado2, lado3):
    p = (lado1 + lado2 + lado3) / 2
    return (p * (p - lado1) * (p - lado2) * (p - lado3)) ** 0.5

def main():
    lado1 = float(input('Ingrese lado 1: '))
    lado2 = float(input('Ingrese lado 2: '))
    lado3 = float(input('Ingrese lado 3: '))

    area = area_triangulo(lado1, lado2, lado3)

    print('Area:', area)

main()
