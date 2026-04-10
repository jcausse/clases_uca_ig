# Funciones

## Concepto

Las funciones son bloques de código que se agrupan y se comportan como una unidad. Esto permite:
- Hacer una misma tarea múltiples veces sin la necesidad de reescribir el código cada vez.
- Modularizar los programas, de forma que el código sea más corto, más fácil de leer, y que no tenga repeticiones innecesarias.
- Simplificar la búsqueda de errores en el código, y evitar cometerlos.

Es una buena práctica **modularizar** los programas a medida que se construyen, de forma que el código quede separado en funciones
(sin llegar a tener funciones que sean innecesariamente simples) que puedan ser reutilizadas más adelante. Cada una de estas
funciones debería tener una **única responsabilidad** (cumpliendo así con el [_Single Responsibility Principle_](https://www.geeksforgeeks.org/system-design/single-responsibility-in-solid-design-principle/)), e implementarla con código claro y razonablemente eficiente.

## Sintaxis

La sintaxis de Python para las funciones es la que sigue a continuación. Es importante notar que esta es una simplificación de la sintaxis real, ya que Python permite añadir varios modificadores y tipos de parámetros a las funciones (como por ejemplo _keyword arguments_). Sin embargo, como en Informática General UCA dichas _features_ de Python no son parte del programa y están prohibidas por la cátedra, esta simplificación que está a continuación contiene todo lo que necesitamos saber para la materia.

### Resumen de sintaxis
```python
# Nota: aquello entre corchetes angulares <> debe ser completado por nosotros
# Nota: aquello entre corchetes [] es opcional
# Nota: los 3 puntos ... representan a aquellos parámetros entre el 2do y el n-ésimo
#       los puntos NO se ponen, y se separan todos los parámetros a recibir por comas ,

def <nombre de la funcion> ( [<parametro 1>], [<parametro 2>], ..., [<parametro N>] ):
    <CODIGO>
    <CODIGO>
    <CODIGO>
    
    [return <valor de retorno>]
```

### Nombre de la función

`<nombre de la funcion>` es el nombre que se le da a la misma. Este nombre:
- No puede repetirse.
- No puede contener espacios, por lo cual las funciones cuyos nombres necesitarían espacios siguen alguna de estas convenciones:
    - Camel Case: `funcionConMultiplesPalabrasEnElNombre`
    - Snake Case: `funcion_con_multiples_palabras_en_el_nombre`
        - snake_case es la recomendación oficial de Python (PEP 8).
- Debe ser significativo, es decir, resumir muy brevemente qué hace la función.
- De ser posible, debe ser corto.
- Cuando las funciones determinan si un valor cumple o no con un criterio, se las suele nombrar `is_<SOMETHING>` o `es_<ALGO>`. Por ejemplo, si una función pretende determinar si un número es primo, podría llamarse `es_primo`. Estas funciones se espera que devuelvan un valor `True` o `False`.

### Parámetros
`<parametros>` son valores que pueden proporcionarse a una función en caso de ser necesarios. La idea es que la función pueda modificar su comportamiento en base a estos parámetros, realizar cálculos, o tomar decisiones usando los mismos. Por ejemplo, una función `es_primo` que determina si un número es o no primo debería recibir el número que se quiere verificar.

Los parámetros:
- Son opcionales. Una función puede no recibir parámetros, por lo que luego del nombre solo se colocan paréntesis que abren y cierran.
- Pueden ser la cantidad que uno quiera, pero, en principio, una cantidad fija. Existe una forma de hacer funciones que reciben una cantidad variable de parámetros, pero no es tema de la materia.
- Cada uno requiere de un nombre, el cual no puede repetirse entre los parámetros de una misma función (es decir, puede haber varias funciones que reciban un parámetro llamado `x`, pero no puede haber más de un parámetro `x` dentro de los que recibe una misma función).
- **Python NO verifica los tipos de datos de los parámetros**. Si por ejemplo se le pasa a una función `es_primo()` (que, claramente, espera recibir un número entero, es decir, tipo `int`) el texto (tipo `str`) `"hola"` como parámetro, seguramente se obtendrá un error en la ejecución del programa, pero Python no va a verificar que el tipo de dato sea el correcto a la hora de recibir el parámetro.

> **Nota**: Los tipos de datos de los parámetros pueden indicarse, como ayuda al programador ([_Type Hints_](https://www.geeksforgeeks.org/python/type-hints-in-python/)), pero:
    - Python no los verifica (son _hints_, no convierte el tipado en estático).
    - No es parte del contenido de Informática General UCA.

### Código o cuerpo de la función

`<el código>` puede ser una o más líneas de código, que son las instrucciones que se ejecutarán al invocar (llamar) a la función. Aquí puede haber condicionales, ciclos (temas que vienen más adelante), llamados a `input()`, a `print()`, etc.

### Return

`<return>` es una palabra reservada que indica a Python que debe terminar la ejecución de la función en el momento en el que lo encuentra. 
Una función puede tener ninguno, uno, o múltiples instrucciones `return` (en Informática General de la UCA, **la cátedra prohíbe múltiples returns en una función**, por lo que sólo pueden tener uno o ninguno). Si una función ejecuta todo su código hasta el final, la misma termina cuando ejecuta su última instrucción. No necesita un `return` explícito al final. En el siguiente ejemplo, el `return` en `saludar2()` es innecesario.

```python
def saludar1(nombre):
    print('Hola,', nombre)

def saludar2(nombre):
    print('Hola,', nombre)
    return                  # Es innecesario. Si no se pone, la función igual termina después del print.

saludar1('Juan')            # Hola, Juan
saludar2('Ignacio')         # Hola, Ignacio
```

## Definición e invocación

Notar en el ejemplo anterior que `def saludar1(nombre)` y `def saludar2(nombre)` están **definiendo** (declarando que existe y dando el código) las funciones, mientras que `saludar1('Juan')` y `saludar2('Ignacio')` están **invocando** a las funciones (llamándolas).

Al invocar una función:
- La misma debe estar **definida antes de ser invocada**.
- En la invocación, obligatoriamente se le debe dar a cada parámetro un valor. Los valores se asignan a los parámetros en el orden en que aparecen, ya que son **parámetros posicionales**. Ejemplo:

    ```python
    def fun(x, y, z):
        <CODIGO>
    
    fun(2, 3, 4)        # A x se le asigna el valor 2, a y se le asigna el valor 3, y a z se le asigna el valor 4.
    ```

> **Nota**: Es posible utilizar "parámetros por defecto", es decir, hacer que los parámetros tengan un valor por omisión, de forma que no sea obligatorio especificar uno, pero no es parte de la materia y no se permite su uso.

## Valor de retorno

El `<valor de retorno>` es opcional (pues, si bien el valor de retorno se coloca a continuación de un `return`, existe la posibilidad de tener un `return` sin valor que lo acompañe, e incluso existe la posibilidad de que una función no tenga `return`, ya que es opcional). 

El mismo permite que la función devuelva algo a quien la invocó como resultado. Este resultado suele ser:

- Un dato numérico, si la función tenía por objetivo hacer algún cálculo.
- Un valor booleano (`True` o `False`), si la función:
    - Debe informar si su invocación fue exitosa (ejemplo: una función que pretende enviar un dato a través de Internet).
    - Debe informar si un dato recibido cumple o no cumple un criterio (ejemplo: `es_primo` devolverá `True` si el número es primo, o `False` si no lo es).
- Un string (ejemplo: si la función pedía al usuario ingresar un dato por teclado).
- Alguna estructura de datos más compleja (como listas, tuplas, diccionarios, etc.) como las que veremos más adelante.
- O cualquier otra cosa, hay muchísimas posibilidades.

Ahora bien, existe la posibilidad de que la función no tenga `return`, tenga `return` pero sin valor de retorno (`return` a secas), o simplemente el llamante no espere un valor de retorno por parte de la misma. Las funciones `saludar1()` y `saludar2()` anteriores son ejemplos de esto: `saludar1()` no tiene `return`, mientras que `saludar2()` tiene `return`, pero no tiene valor de retorno. Además, no se espera un valor de retorno por parte de una función que tiene por tarea saludar al usuario.
Otro ejemplo de esto es print(), que no devuelve nada.

## NoneType (`None`)

Cuando una función no devuelve nada, para Python devuelve un tipo de dato especial llamado `NoneType` que, al imprimirlo con `print()` se muestra como `None`. 

`None` es aquello retornado cuando una función encuentra un `return` sin valor de retorno (como `saludar2()`), o cuando termina sin un `return` (como es el caso de `saludar1()`). Debido a esto **toda función de Python devuelve algo, ya que ante la ausencia de un valor de retorno explícito devolverá `None`**.

Es posible hacer que una función devuelva `None` a propósito, si quisiéramos, lo que se suele usar para posibles casos de error (sin llegar a usar excepciones, que no son tema de la materia). En este caso, un `return None` podría indicar un error. Ejemplo:

```python
# NOTA: Este ejemplo usa condicionales, que es tema de la unidad 3.

def dividir(a, b):
    if b == 0:          # Si el divisor fuese cero,
        ret = None      # se devuelve None indicando error
    else:               # En caso contrario,
        ret = a / b     # se devuelve el valor de la division
    return ret

print(dividir(5, 2))    # Imprime 2.5
print(dividir(5, 0))    # Imprime None
```
