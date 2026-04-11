"""
Ejercicio 7:

Desarrollar un programa que permita ingresar las notas de una cantidad indefinida de
alumnos. Considerar notas enteras en el rango de 1 a 10 e ignorar las notas no válidas
(fuera el rango) ingresadas. La carga finaliza cuando la nota ingresada es 0. A
continuación el programa deberá mostrar la cantidad de alumnos aplazados (nota menor
a 4), la cantidad de alumnos aprobados (nota entre 4 y 7 inclusive) y la cantidad de
alumnos que promocionan la materia (nota superior a 7). En cada caso, se mostrará el
porcentaje del total de notas válidas cargadas que cada caso representa y el promedio
general de todas las notas. Ejemplo:

Ingrese nota: 5
Ingrese nota: 4
Ingrese nota: 4
Ingrese nota: 11
Ingrese nota: 2
Ingrese nota: 8
Ingrese nota: 8
Ingrese nota: 2
Ingrese nota: 7
Ingrese nota: 9
Ingrese nota: 0
Cantidad de aplazos: 2 (22.22%)
Cantidad de aprobados: 4 (44.44%)
Cantidad de promocionados: 3 (33.33%)
Promedio general: 5.44
"""

def main():
    # Variables contadoras (cuentan cantidades, de a 1): Empiezan en 0 porque la cuenta empieza en 0
    aplazados = 0               # Cantidad de aplazados                             (nota < 4)
    aprobados = 0               # Cantidad de aprobados pero que no promocionaron   (4 <= nota < 7)
    promocionados = 0           # Cantidad de promocionados                         (7 <= nota)
    alumnos_totales = 0         # Cantidad de alumnos totales procesados
    
    # Variables acumuladoras
    suma_total_notas = 0        # Variable que suma todas las notas, para dividirla por la cantidad de alumnos y obtener el promedio

    salir = False               # Esta varibale es un FLAG (bandera). Es una variable booleana que me permite controlar
                                # el comportamiento de mi programa. En este caso, me indica si debo o no seguir en el ciclo

    while not salir:            # Mientras la variable salir se mantenga en False (not False es True) (mientras NO deba salir)
        nota = int(input('Ingrese nota: '))         # Hago que el usuario ingrese una nota. Pueden pasar 3 cosas:

        # 1. La nota puede ser 0. En ese caso, el usuario desea salir
        if nota == 0:           # Si la nota es 0, el usuario quiere salir
            salir = True        # Cambio el flag de salir a True indicando que se debe salir del ciclo (not True es False)
                                # Cuando la condicion del ciclo se hace False, el mismo termina

        # 2. La nota es una nota 1-10 (nota valida)
        if 1 <= nota and nota <= 10:        # Si la nota esta entre 1 y 10
            alumnos_totales += 1            # Marco que tuve un alumno mas
            suma_total_notas += nota        # Agrego la nota a la suma total de notas

            if nota < 4:                    # Si es menor que 4, esta aplazado
                aplazados += 1
            elif nota < 7:                  # Si es menor que 7 (pero dada la condicion anterior, fue >= 4), aprueba
                aprobados += 1
            else:                           # Si no aplazo ni aprobo, entonces su nota es >= 7, promociona
                promocionados += 1
                

        # 3. La nota es invalida (menor que 1 o mayor que 10). En este caso no hay codigo porque simplemente la ignoro y no hago nada

    print('Cantidad de aplazos: {} ({:.2f}%)'.format(aplazados, aplazados / alumnos_totales * 100))
    print('Cantidad de aprobados: {} ({:.2f}%)'.format(aprobados, aprobados / alumnos_totales * 100))
    print('Cantidad de promocionados: {} ({:.2f}%)'.format(promocionados, promocionados / alumnos_totales * 100))
    print('Promedio general: {:.2f}'.format(suma_total_notas / alumnos_totales))

main()
