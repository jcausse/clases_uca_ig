"""
Ejercicio 5:

Desarrollar la función rotacion que a partir de un string pasado como parámetro                         
genere y retorne un nuevo string en donde la primera mitad del string cambia con la                               
segunda mitad. Desde el programa principal ingresar por teclado un texto, invocar a la                           
función y mostrar por pantalla el resultado que retorna la función. Para el caso que el                               
texto ingresado no sea de longitud par y mayor a dos, se deberá pedir al usuario que                                 
realice el ingreso nuevamente, dándole al mismo todas las oportunidades que sean                       
necesarias (validación del ingreso).
"""

def ingresar_texto():
    """
    Permite ingresar un string que debe ser de longitud par y mayor a dos.
    En caso de que el usuario lo ingrese mal, debera reingresarlo, y la funcion solo retorna
    cuando el ingreso sea correcto
    """
    res = ''
    valido = False                              # Indico que el texto ingresado hasta ahora no es valido
    while not valido:                           # Mientras el texto no sea valido
        res = input('Ingrese un texto: ')       # Le pido al usuario que ingrese el texto

        # Validacion
        if len(res) <= 2:                       # En el caso en el que la longitud no sea mayor a dos, le aviso al usuario
            print('La longitud del texto debe ser mayor que 2')
        elif len(res) % 2 == 1:                 # En el caso en el que la longitud sea impar, le aviso al usuario
            print('El texto debe tener una cantidad par de caracteres')
        else:                                   # En caso de que paso todas las validaciones (todo estuvo bien)
            valido = True                       # Indico que el texto ahora es valido. Esto rompe el ciclo (not valido es False)
    
    return res

def rotacion(texto):
    primeraMitad = texto[: len(texto) // 2]     # Recordar teoria de slices (ver Unidad 5 -> Teoria -> slices_indices.py)
    segundaMitad = texto[len(texto) // 2 :]
    return segundaMitad + primeraMitad

def main():
    texto = ingresar_texto()
    print('La función ha retornado:', rotacion(texto))

main()
