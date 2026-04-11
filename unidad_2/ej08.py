"""
Ejercicio 8:

Dado la función main(), completar el programa programando las funciones crearFila                     
y crearRectangulo de modo que al ejecutar el programa dibuje un rectangulo de                         
asteriscos. La función main() no debe ser modificada.

crearFila recibe como parámetro un número natural ancho y retorna un string                       
conformado por una cantidad ancho de asteriscos.  
crearRectangulo recibe como parámetros dos números naturales ancho y alto, y                     
retorna un string que al ser mostrado por pantalla dibuja un rectángulo de ancho por                             
alto asteriscos. Esta función invoca a crearFila para crear el string de cada fila. 
"""

def crearFila(ancho):
    return "*" * ancho

def crearRectangulo(ancho, alto):
    return (crearFila(ancho) + "\n")* alto

def main(): 
    ancho = int(input('Ingrese ancho: ')) 
    alto = int(input('Ingrese alto: ')) 
    print(crearRectangulo(ancho, alto))

main()
