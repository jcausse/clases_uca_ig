#################
### FUNCIONES ###
#################

# Las funciones son bloques de código que se agrupan y se comportan como una unidad. Esto permite:
# * Hacer una misma tarea múltiples veces sin la necesidad de reescribir el código cada vez.
# * Modularizar los programas, de forma que el código sea más corto, más fácil de leer, y que no tenga repeticiones innecesarias.
# * Simplificar la búsqueda de errores en el código, y evitar cometerlos.

# Es una buena práctica MODULARIZAR los programas a medida que se construyen, de forma que el código quede separado en funciones
# (sin llegar a tener funciones que sean innecesariamente simples) que puedan ser reutilizadas más adelante. Cada una de estas
# funciones debería tener una ÚNICA RESPONSABILIDAD, y cumplir con ella con código claro y razonablemente eficiente.

# Sintaxis:
"""
def <nombre de la funcion> ( <parametro 1>, <parametro 2>, ..., <parametro N> ):
    <CODIGO>
    <CODIGO>
    <CODIGO>
    
    <return> <valor de retorno>
"""

# <nombre de la funcion> es el nombre que se le da a la misma. Este nombre:
# * No puede repetirse.
# * No puede contener espacios, por lo cual las funciones cuyos nombres necesitarían espacios siguen alguna de estas convenciones:
#   * Camel Case: funcionConMultiplesPalabrasEnElNombre
#   * Snake Case: funcion_con_multiples_palabras_en_el_nombre
#       * snake_case es la recomendación oficial de Python (PEP 8).
# * Debe ser significativo, es decir, resumir muy brevemente que hace la funcion.
# * De ser posible, debe ser corto.
# * Cuando las funciones determinan si un valor cumple o no con un criterio, se las suele nombrar is_<SOMETHING> o es_<ALGO>. Por
#   ejemplo, si una función pretende determinar si un número es primo, podría llamarse es_primo. Estas funciones se espera que
#   devuelvan un valor True o False.

# <parametros> son valores que pueden proporcionarse a una función en caso de ser necesarios. La idea es que la función pueda
# modificar su comportamiento en base a estos parámetros, o realizar cálculos o tomar decisiones usando los mismos. Por ejemplo, una
# función es_primo que determina si un número es o no primo debería el número que se quiere verificar.
# Los parámetros:
# * Son opcionales. Una función puede no recibir parámetros, por lo que luego del nombre solo se colocan paréntesis que abren y
#   cierran.
# * Pueden ser la cantidad que uno quiera, pero, en principio, una cantidad fija. Existe una forma de hacer funciones que reciben
#   una cantidad variable de parámetros, pero no es tema de la materia.
# * Cada uno requiere de un nombre, el cual no puede repetirse entre los parámetros de una misma función (es decir, puede haber
#   varias funciones que reciban un parámetro llamado "x", pero no puede haber más de un parámetro "x" dentro de los que recibe
#   una misma función).
# * Python NO verifica los tipos de datos de los parámetros. Si por ejemplo se le pasa a una función es_primo (que, claramente, 
#   espera recibir un número entero) el string "hola" como parámetro, seguramente se obtendrá un error en la ejecución del programa,
#   pero no Python no va a verificar que el tipo de dato sea el correcto a la hora de recibir el parámetro. Se puede indicar, como
#   ayuda al programador, el tipo de dato esperado para cada parámetro (), pero:
#   * Python no lo verifica.
#   * No es tema de la materia.

# <el código> puede ser una o más líneas de código, que son las instrucciones que se ejecutarán al invocar (llamar) a la función.
# Aquí puede haber condicionales, ciclos (temas que vienen más adelante), llamados a input(), a print(), etc.

# <return> es una palabra reservada que indica a Python que debe terminar la ejecución de la función en el momento en el que lo
# encuentra. Una función puede tener ninguno, uno, o múltiples instrucciones return (en Informática General de la UCA, la cátedra
# prohibe múltiples returns en una función, por lo que sólo pueden tener uno o ninguno). 
# Si una función ejecuta todo su código hasta el final, la misma termina cuando ejecuta su última instrucción. No necesita un 
# return explícito al final. En el siguiente ejemplo, el return en saludar2() es innecesario.
"""
def saludar1(nombre):
    print('Hola,', nombre)

def saludar2(nombre):
    print('Hola,', nombre)
    return                  # Es innecesario. Si no se pone, la función igual termina después del print.

saludar1('Juan')            # Hola, Juan
saludar2('Ignacio')         # Hola, Ignacio
"""

# Notar, además, que def saludar1(nombre) y def saludar2(nombre) están DEFINIENDO (declarando que existe y dando el código) las
# funciones, mientras que saludar1('Juan') y saludar2('Ignacio') están INVOCANDO a las funciones (llamándolas).
# Al invocar una función:
# * La misma debe estar definida ANTES de ser invocada.
# * En la invocación, obligatoriamente se le debe dar a cada parámetro un valor. Los valores se asignan a los parámetros
#   en el orden en que aparecen. Ejemplo:
"""
def fun(x, y, z):
    <CODIGO>
    
fun(2, 3, 4)        # A x se le asigna el valor 2, a y se le asigna el valor 3, y a z se le asigna el valor 4.
"""
#   Existe una forma de utilizar "parámetros por defecto", es decir, hacer que los parámetros tengan un valor por omisión, de forma
#   que no sea obligatorio especificar uno, pero no es parte de la materia.

# El <valor de retorno> es opcional (pues, si bien el valor de retorno se coloca a continuación de un "return", existe la posibilidad
# de tener un "return" sin valor que lo acompañe, e incluso existe la posibilidad de que una función no tenga "return", ya que es
# opcional). Permite que la función devuelva algo a quien la invocó como resultado. Este resultado suele ser:
# * Un dato numérico, si la función tenía por objetivo hacer algún cálculo.
# * Un valor booleano (True o False), si la función:
#   * Debe informar si su invocación fue exitosa (ejemplo: una función que pretende enviar un dato a través de Internet).
#   * Debe informar si un dato recibido cumple o no cumple un criterio (ejemplo: es_primo devolverá True si el número es primo, o 
#     False si no lo es).
# * Un string (ejemplo: si la función pedía al usuario ingresar un dato por teclado).
# * Alguna estructura de datos más compleja (como listas, tuplas, diccionarios, etc.).
# * O cualquier otra cosa, hay muchísimas posibilidades.

# Ahora bien, existe la posibilidad de que la función no tenga "return", tenga "return" pero sin valor de retorno ("return solo"), o
# simplemente el llamante no espere un valor de retorno por parte de la misma. Por ejemplo, las funciones saludar1() y saludar2() son
# ejemplos de esto. saludar1() no tiene return. saludar2() tiene return, pero no tiene valor de retorno. Además, no se espera un valor
# de retorno por parte de una función que tiene por tarea saludar al usuario.
# Otro ejemplo de esto es print(), que no devuelve nada.

# CUANDO UNA FUNCIÓN NO DEVUELVE NADA, PARA PYTHON DEVUELVE UN TIPO DE DATO ESPECIAL QUE SE LLAMA "NoneType", Y QUE AL IMPRIMIRLO
# APARECE "None" EN LA PANTALLA. ES POR ESTO QUE TODA FUNCIÓN EN PYTHON SIEMPRE DEVUELVE ALGO, A LO SUMO DEVOLVERÁ None. Esto sucede
# tanto cuando una función encuentra un "return" sin valor de retorno (como saludar2), o cuando termina sin un "return" (como es el
# caso de saludar1).
# Podemos hacer que una función devuelva None a propósito, si quisiéramos, lo que se suele usar para posibles casos de error (sin
# llegar a usar excepciones, que no son tema de la materia). En este caso, un "return None" podría indicar un error. Ejemplo:

"""
# NOTA: Este ejemplo usa condicionales, que es tema de la unidad 3. Se recomienda ver dicha unidad primero.

def dividir(a, b):
    if b == 0:
        ret = None      # Marca que es un caso de error
    else:
        ret = a / b
    return ret

print(dividir(5, 2))    # 2.5
print(dividir(5, 0))    # None
"""
