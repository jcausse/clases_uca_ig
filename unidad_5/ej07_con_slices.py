"""
Ejercicio 7:

Desarrollar una función que reciba por parámetros dos textos: uno “largo” y otro “corto” y                             
retorne la cantidad de veces que se encuentra repetido el texto “corto” dentro del texto                             
“largo”. Desde el programa principal ingresar por teclado el texto largo y el texto corto a                               
buscar, luego invocar a la función y mostrar por pantalla el resultado que retorna.
"""

# Retorna la cantidad de apariciones del texto largo dentro del corto
def apariciones(largo, corto):
    coincidencias = 0
    for i in range(len(largo) - len(corto) + 1):
        if corto == largo[i : i + len(corto)]:
            coincidencias += 1
    return coincidencias

def main():
    largo = input('Ingrese el texto largo: ')
    corto = input('Ingrese el texto corto: ')
    n = apariciones(largo, corto)
    print('El texto corto se encontró {} veces en el texto largo'.format(n))

main()
