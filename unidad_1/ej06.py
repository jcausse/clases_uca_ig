"""
Ejercicio 6:

Realizar un programa en el que se ingrese la base y la altura de un triángulo rectángulo                                 
e informe el área y el perímetro del mismo. El programa debe mostrar el resultado con                               
una precisión de 2 dígitos decimales
"""

# Pedir los datos al usuario
base = float(input('Ingrese base: '))
altura = float(input('Ingrese altura: '))

# Calculo el area
area = base * altura / 2

# Calculo el perimetro. Perimetro = base + altura + hipotenusa (T. Pitagoras)
perimetro = base + altura + (base ** 2 + altura ** 2) ** (1/2)
# Otra forma de calcular la hipotenusa es: (base * base + altura * altura) ** (1/2)

# Imprimo datos por pantalla
print('Calculos para un triangulo de base {} y altura {}:'.format(base, altura))
print('<<< Area={:.2f} >>>   <<< Perimetro={:.2f} >>>'.format(area, perimetro))
