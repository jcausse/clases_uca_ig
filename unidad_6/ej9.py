"""
Ejercicio 9:

Desarrollar la función cargarLstAlu que retorne una lista con los datos de alumnos
(lista de lista). Por cada alumno se cargará en una lista el DNI, nombre y edad, como se
muestra el siguiente ejemplo:
    [[2698705, 'James Howlett', 18], [38698705, 'Jakie chan', 22], [35698705, 'Jean Grey', 22]]

Desarrollar la función ordenarAluXDNI que reciba por parámetro la lista generada en
cargarLstAlu y la ordene en forma descendente por DNI.

Desde el programa principal invocar a cargarLstAlu donde se cargará la lista de datos
de los alumnos. Una vez terminada la carga imprimir la lista por pantalla. Luego invocar
a ordenarAluxDNI, que ordenará la lista por DNI. A continuación volver a imprimir la
lista para verificar que su orden sea el correcto.
"""

def obtener_alumno():
    """
    Pide al usuario que ingrese un alumno.
    Cuando el usuario no quiere ingresar mas alumnos deja un campo sin completar (oprime enter directamente).
    Retorna:
    * Una lista de 3 elementos con el DNI (int), nombre (string), edad (int) del alumno; en ese orden, si el usuario
      ingreso un alumno
    * None si el usuario no quiere ingresar mas alumnos.
    """
    # Cuidado: para chequear que el usuario no ingreso nada, debemos ver si el input() devuelve un string vacio ('').
    #          En ese caso, debemos retornar None. En caso contrario, agregamos la info a la lista, previo hacer las
    #          conversiones pertinentes (pasar DNI y edad a int). Recordar que input() devuelve un string.
    
    # NOTA:    Estos ifs anidados (que podrian ser muchos mas si se piden mas campos) no son una buena practica, pero,
    #          para evitar hacer esto, deberia usar returns multiples, lo cual la catedra NO permite (cada funcion puede
    #          solamente tener 1 return)
    
    ret = None                                                  # Valor a retornar
    
    dni = input('Ingrese el DNI del alumno: ')                  # Pido DNI
    if dni != '':                                               # Si no se ingreso nada no entro al if y devuelve None
        dni = int(dni)                                          # Ante DNI valido, lo convierto a int
        nombre = input('Ingrese el nombre del alumno: ')        # Pido nombre
        if nombre != '':                                        # Si no se ingreso nada no entro al if y devuelve None
            edad = input('Ingrese la edad del alumno: ')        # Pido edad
            if edad != '':                                      # Si no se ingreso nada no entro al if y devuelve None
                edad = int(edad)                                # Ante edad valida, la convierto a int
                ret = [dni, nombre, edad]                       # Ya se ingreso todo. Armo la lista con los datos.
                
    return ret
    
def cargarLstAlu():
    """
    Carga alumnos hasta que el usuario no quiera ingresar mas.
    """
    ret = []                            # Lista de alumnos
    
    alumno = obtener_alumno()           # Pido al usuario un alumno:
    while alumno != None:               # Si el usuario ingreso un alumno
        ret.append(alumno)              # Lo agrego a la lista de alumnos
        alumno = obtener_alumno()       # Pido uno nuevo
        
    return ret

INDICE_DNI = 0                                  # Indica en que posicion de una lista de alumno se encuentra el DNI

def bubblesort(lst):                            # Ver archivo 'bubblesort.py' en la carpeta de Teoria.
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            if lst[j][INDICE_DNI] < lst[j + 1][INDICE_DNI]:   # < para descendente. Al ser lista de listas, lst[j] es una lista [DNI, nombre, edad]
                aux = lst[j]                                  # Como quiero comparar por DNI uso lst[j][0] para obtener el DNI de la lista de alumno
                lst[j] = lst[j + 1]
                lst[j + 1] = aux

def main():
    alumnos = cargarLstAlu()
    print(alumnos)
    bubblesort(alumnos)
    print(alumnos)
    
main()
