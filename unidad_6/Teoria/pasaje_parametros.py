### Pasaje de parámetros por valor (o por copia)

# Los tipos de datos simples (int, float, bool, str, etc.) se pasan a las funciones por valor.
# Esto quiere decir que la funcion recibe una copia del valor original, que guardará en una
# nueva variable visible únicamente por sí misma, y la cual será destruida una vez la función
# retorne. 
# Cualquier modificacion que se haga a la variable dentro de la funcion:
# - no se verá reflejada en la variable original
# - no se verá reflejada en otras funciones que utilicen una variable con el mismo nombre (pues
#   son todas independientes)
# - no conservará (en principio) el valor una vez que la función haya finalizado su ejecución,
#   incluso si la función es vuelta a llamar luego

# Ejemplo:
"""
def fun(x):
    x = 2   # Modifica su propia copia, no la original

x = 1
print(x)  # Imprime: 1
fun(x)
print(x)  # Imprime: 1
"""

### Pasaje de parámetros por referencia

# Las colecciones (como listas y diccionarios), al  pasarse a una funcion, se pasan por
# REFERENCIA. Esto quiere decir que la funcion no recibe una copia de la coleccion, sino que
# recibe una referencia a la coleccion original que se creo en otro lado (en el programa
# principal o en otra funcion). Debido a esto:
# TODA MODIFICACION QUE SE HAGA A LA COLECCION DENTRO DE LA FUNCION SERA VISIBLE POR LAS 
# DEMAS FUNCIONES QUE UTILICEN ESA COLECCION.

# Ejemplo:
"""
def fun(lst):
    lst.append(2)   # Este 2 se agrega a la lista original, no a una copia

lst = [1]
print(lst)  # Imprime: [1]
fun(lst)
print(lst)  # Imprime: [1, 2]
"""

# Ejemplo:
"""
def fun(diccionario):
    diccionario['despedida'] = 'chau'

diccionario = {'saludo': 'hola'}
print(diccionario)  # Imprime: {'saludo': 'hola'}
fun(diccionario)
print(diccionario)  # Imprime: {'saludo': 'hola', 'despedida': 'chau'}
"""
