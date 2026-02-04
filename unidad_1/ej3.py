"""
EJERCICIO 3:

Desarrollar un programa que solicite los dos lados de un rectángulo. Luego el programa
debe calcular y mostrar por pantalla el perímetro y área del mismo.

 
  +-------------------------+
  |                         |
  |                         | lado1
  |                         |
  |                         |
  +-------------------------+
          lado2
"""

lado1 = float(input('Ingrese lado 1: '))
lado2 = float(input('Ingrese lado 2: '))

perimetro = lado1 * 2 + lado2 * 2
area = lado1 * lado2

print('Perimetro:', perimetro)
print('Area:', area)
