# Ciclos (estructuras de repetición)

## Motivación

En muchos ejercicios de la práctica 3 (condicionales) nos pasaba que, por ejemplo, teníamos que convertir un número de _n_ dígitos (se aseguraba por enunciado que el número tendría esa cantidad de dígitos) a base binaria. Si bien, con cierto esfuerzo, uno lograba hacer esos ejercicios y que funcionaran correctamente para números de _n_ dígitos, uno podría preguntarse:

* ¿Qué pasa si utilizo un número de más de _n_ dígitos? Generalmente la conversión falla (convierte mal).
* ¿Cómo puedo hacer que funcione para más de _n_ dígitos? Agrego más código para soportar un número más grande de dígitos, repitiendo el mismo código que ya hice antes pero agregando nuevos casos.
* La respuesta a la pregunta anterior me lleva al mismo problema inicial (la conversión falla si me paso de la cantidad de dígitos estipulada) pero con un _n_ más grande. ¿Cómo puedo hacer para que funcione para un número **arbitrario y no previamente definido** de dígitos?

Además de estas preguntas, uno podría tener ciertas quejas:
* Tengo que escribir _n_ veces el mismo código para que funcione para _n_ dígitos. Ojalá pudiera escribirlo sólo una vez.
* El código queda muy largo.
* El código se hace difícil de leer.
* El código repite operaciones, y cada vez que repito código tengo una nueva chance de equivocarme.

Y finalmente:
* El código es horrible.
* Tiene que haber una mejor forma de hacer esto.

Debe haber una manera de repetir código sin tener que escribirlo varias veces, y que además contemple que la cantidad _n_ de repeticiones es arbitraria. Se llega a la limitación de que es literalmente imposible escribir código que considere todos los posibles valores de _n_.

## Concepto

Las estructuras de repeticion (ciclos) son estructuras que permiten ejecutar un mismo bloque de codigo (su _cuerpo_) multiples veces, de forma que no tenga que escribir varias veces lo mismo.

Un ciclo puede realizarse según:

* El valor de una condicion (significando _condición_ lo mismo que en la unidad de condicionales), que se comprobará antes de iniciar cada ciclo para determinar si se debe o no realizar una nueva iteracion (una ejecución del _cuerpo_ del ciclo).
    * Cuando la condicion es evaluada como verdadera (`True` o un entero distinto de cero), el cuerpo del ciclo vuelve a ejecutarse. 
    * Si no (al ser `False` o un entero igual a cero), se saltea el ciclo, y se sigue ejecutando lo que viene debajo.
 
    Estos ciclos se los menciona de forma coloquial como "_mientras_", o, en inglés `while`.

* Un elemento _iterable_ (es decir, un elemento de algún tipo de dato que tenga sub-elementos dentro, y que para cada uno de sus sub-elementos se pueda realizar una serie de operaciones).

    Estos ciclos realizan una operación o serie de operaciones "_para cada_" (en inglés, _for each_) elemento de la _colección_ se llaman ciclos `for`.

    A los elementos iterables con frecuencia se los suele llamar "secuencias". Pueden ser, por ejemplo, _listas_, _tuplas_, _strings_ (se iteran caracter a caracter), _claves_ o _valores_ de un _diccionario_, rangos (usando `range()`), entre otros. Todos estos elementos los veremos en próximas unidades.

    > **Nota para lectores más avanzados:** Modificar las secuencias (agregar o quitar elementos a una lista, por ejemplo) mientras las mismas están siendo iteradas es una muy mala idea (desde el punto de vista de las buenas prácticas), e incluso puede generar errores de ejecución.

> **Pro Tip:** Como norma general, cuando sabemos de antemano la cantidad de veces que vamos a ejecutar el cuerpo del ciclo (la cantidad de iteraciones a realizar), usamos un ciclo `for`.
> 
> Por el contrario, si no conocemos cuántas veces vamos a iterar, utilizamos un ciclo `while`.
> 
> Como siempre, hay casos que escapan a la norma general.

---

## Ciclos `for` / `for`-`in`

En Python, cuando queremos realizar una operacion multiples veces sobre los sub-elementos de un _iterable_ (_lista_, _string_, _tupla_, _claves_ o _valores_ de un _diccionario_, etc.), generalmente usamos un ciclo `for`.

El ciclo `for` va obteniendo de a uno y **en orden** los elementos internos de un iterable y realizando operaciones para cada uno de ellos.

### Sintaxis

```python
for <variable> in <iterable>:
    <cuerpo>
```

### Ejemplo: Imprimir todos los caracteres de un _string_

```python
string = "Info. Gral. Python UCA"
# En cada iteración, se guarda el siguiente caracter del 
# string en la variable c
for c in string:  
    print(c)
```

El ciclo se termina cuando se imprimió el último caracter, y el programa sigue ejecutando lo que venga debajo.

### Ejemplo más avanzado: Imprimir todos los elementos de una lista

```python
lst = ['hola', 'buen dia', 3, 3.14, [1, 2, 3]]
# Toma los elementos, uno por uno, y los guarda en la variable elem
for elem in lst:
    print(elem)     # Imprime el elemento actualmente tomado
    x = elem * 2    # Puedo operar con el valor de elem
    print(x)        # Lo que imprime depende del elemento porque 
                    # cambia lo que hace x * 2
```

### Ejemplo más avanzado: Dado un conjunto de lapiceras, imprimir un texto que describa a cada una
```python
conjunto_lapiceras = [
    {'marca': 'bic', 'tipo': 'roller', 'color': 'violeta'},
    {'marca': 'uniball', 'tipo': 'roller', 'color': 'amarillo'},
    {'marca': 'parker', 'tipo': 'pluma', 'color': 'azul'},
    {'marca': 'abcd', 'tipo': 'tipo 1', 'color': 'verde'}
]

i = 1
for lapicera in conjunto_lapiceras:
    print('Lapicera {}: Es una lapicera {}, de marca {}, color {}.'.format(
        i,
        lapicera['tipo'],
        lapicera['marca'],
        lapicera['color']
    ))
    i += 1
```

---

## Funcion `range()`

La función `range()` genera una secuencia de numeros enteros, contiguos (seguidos), con todos los números entre dos valores que recibe como párametros, incluyendo el de inicio, pero **sin incluir el de final**.

Tenemos 3 formas de uso:
* `range(START, STOP, STEP)`

* `range(START, STOP)`

* `range(STOP)`

Siendo:

* `START`: es el valor inicial (que puede ser omitido). Este valor será incluido en la secuencia.

    En caso de que este valor sea omitido, el único parametro que recibe `range()` es el `STOP`, y se toma el valor por _default_ (predeterminado) de `START` el 0 (si omito el valor inicial, inicia desde 0).

* `STOP`: es el valor final (que **no puede ser omitido**). Este valor se excluye de la secuencia, por lo que el ultimo valor de la secuencia será `STOP - 1`.

* `STEP`: `range()` también soporta un último parámetro `STEP`, que indica de cuánto en cuánto generar la secuencia. Los números de la secuencia ya no serían contiguos, sino que tendrían una separación.

    El `STEP` predeterminado es 1 (cuenta de 1 en 1): `0, 1, 2, 3, ...`.

    Si se utiliza `STEP` = 2 (cuenta de 2 en 2): `0, 2, 4, 6, ...`.

    Y así sucesivamente.

### Ejemplo:
```python
# Imprime:
# 5 6 7 8 9
for i in range(5, 10):
    print('{} '.format(i), end='')
print() # Imprime una linea vacia al final, para que se vea mejor
```

### Ejemplo:
```python
# Imprime:
# 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print('{} '.format(i), end='')
print() # Imprime una linea vacia al final, para que se vea mejor
```

### Ejemplo:
```python
# Como START > STOP, se genera una secuencia vacia. No imprime nada.
for i in range(15, 10):
    print('{} '.format(i), end='')
```

### Ejemplo:
```python
# Como START = STOP, se genera también una secuencia vacía. No imprime nada.
# Es como querer imprimir los números empezando por el 10, terminando en 10,
# y sin incluir el 10.
for i in range(10, 10):
    print('{} '.format(i), end='')
```

### Ejemplo:
```python
# Imprime:
# 1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58 61 64 67
for i in range(1, 70, 3): # 3 es el STEP. Cuenta de 3 en 3.
    print('{} '.format(i), end='')
print()
```

> **Nota:** Si imprimimos un `range` usando `print()`, veremos que no se muestra la secuencia completa de números. Esto es porque, si bien es útil entender que `range()` genera algo similar a una lista, no es en realidad tal cosa, sino otro tipo de objeto (que no veremos) que se llama iterador.
>
> Sucede que los `range()` están preparados, en principio, para ser recorridos usando un ciclo `for`, de manera que el `for` pueda obtener cada uno de sus sub-elementos y tomar acciones utilizando cada uno de ellos.

---

## Ciclos `while`

El ciclo `while` nos permite ejecutar un bloque de código, su `cuerpo`, una cantidad indefinida de veces dependiendo de una `condición`. Tambien es muy útil (igual que `for-in-range`) cuando queremos realizar iteraciones (sobre una secuencia) teniendo en consideración los índices de los elementos de la secuencia (lista, tupla, string, etc.). 

Por ejemplo, cuando queremos realizar alguna operación para los elementos de la secuencia, la cual no solamente depende de los elementos en sí, sino también de la posición que ocupan dentro de la secuencia.

Las condiciones de los ciclos `while` suelen tener como complejidad que son proposiciones lógicas compuestas (es decir, son varias condiciones unidas por conectivos lógicos). Por esto se recomienda repasar el uso de los operadores lógicos `and`, `or` y `not`, que pueden encontrarse en [este archivo](https://github.com/jcausse/clases_uca_ig/blob/main/unidad_3/Teoria/operadores_logicos.py).

### Sintaxis

```python
while <condicion booleana>:
    <cuerpo>
```

### Ejemplo:

Supongamos que queremos pedir a un usuario que ingrese un número par positivo, y queremos validar el número ingresado, de manera que si el mismo ingresa un número impar o un número negativo, la entrada sea rechazada y se le vuelva a pedir otro número.

Esto no podríamos, en principio, hacerlo con un ciclo `for-in`, debido a que:
* No tenemos un elemento iterable que recorrer, sino que el ciclo que vamos a escribir estará basado en una condición.
* No tenemos forma de conocer cuántas veces se va a ejecutar el ciclo (no podemos predecir cuántas veces puede equivocarse el usuario).

```python
def get_positive_even_number():
    # Flag de que el ingreso es valido
    done = False

    # Mientras el flag no este en True        
    while not done:     
        num = int(input('Ingrese un numero par positivo: '))
        
        # Si cumple todas las condiciones
        if num > 0 and num % 2 == 0:
            # Marco que la entrada fue valida, lo que hace que pueda salir del ciclo
            done = True

        # Si no cumple ALGUNA de las condiciones (and)
        else:
            # Muestro un mensaje de error
            print('El numero {} es invalido.'.format(num)) 

    return num  # El ciclo while anterior me ASEGURA que, si llego hasta aca, "num" es valido

x = get_positive_even_number()
print(x)
```

### Ejemplo:

Desarrollar la función `index(s, c)` que devuelva el índice de la primera aparición del caracter `c` en el string `s`. Si `c` no está en `s`, deberá devolver `None`.

La mejor solución usando `for-in-range` es la siguiente:

```python
def index_ineficiente(s, c):
    ret = None
    found = False
    for i in range(len(s)):
        # return i  ---> Seria lo ideal, pero
        # no se nos permite usar mas de un return :(
        if not found and s[i] == c:
            found = True
            ret = i
    return ret
```

Esto es muy ineficiente, porque una vez encontrada la primera coincidencia de `c` en `s`, sigue recorriendo el string, lo que podría evitarse, retornando justo cuando se encuentra la primera coincidencia.

> **Nota:** Recordar que en Informática General UCA **no está permitido**:
> * Usar más de un `return` por función.
> * Usar `break` para romper ciclos.
> * Usar `continue`.

Debido a estas limitaciones, no hay una forma eficiente y a la vez permitida de resolver este problema usando `for`. Lo haremos usando `while`:

```python
def index(s, c):
    # Indice para recorrer el string
    i = 0
    
    # Valor de retorno (si "c" no esta en "s", "ret = i" no se ejecuta, y devolvemos None)
    ret = None

    # Flag que me permite cortar el ciclo cuando encuentre la primera aparicion de "c" en "s"
    found = False       
    
    # El ciclo tiene 2 condiciones que deben cumplirse a la vez (por el and)
    # * "found" debe ser False (not found). Este es el flag, que al encontrar la aparicion lo
    #   cambiamos a True, y corta el ciclo poque esta condicion deja de cumplirse.
    # * i < len(s) para evitar pasarnos de la maxima longitud.
    while not found and i < len(s):
        if s[i] == c:       # Cuando encuentro la aparicion
            ret = i         # Me guardo el indice (sobreescribo ret)
            found = True    # Seteo el flag
        i += 1
    return ret          # Devuelve el indice (si ret fue sobreescrito), o None

print(index('hola', 'l'))                   # 2
print(index('hola buenos dias ', ' '))      # 4
print(index('buenos dias', 'w'))            # None
```

### Ejemplo:

Escribir una función que permita decidir si un número es o no primo. Una primera versión podría ser:

```python
def es_primo_1(n):
    if n <= 1                   # El 1 no es primo
        primo = False
    else:
        primo = True            # Flag para cortar el ciclo cuando se encuentre un divisor
        i = 2                   # Empezando en 2, vamos a buscar divisores
        while primo and i <= n // 2:    # Puede cortar porque i > n // 2, o porque primo es False
            if n % i == 0:
                primo = False
            i += 1
    return primo
```

Más eficiente: se ha demostrado que, en lugar de buscar divisores hasta la mitad del número, lo podemos hacer hasta su raíz cuadrada.

```python
def es_primo_2(n):
    if n <= 1                   # El 1 no es primo
        primo = False
    else:
        primo = True            # Flag para cortar el ciclo cuando se encuentre un divisor
        i = 2                   # Empezando en 2, vamos a buscar divisores
        while primo and i <= int(n ** 0.5):  # Puede cortar porque i > n // 2, o porque primo es False
            if n % i == 0:
                primo = False
            i += 1
    return primo
```

Aún más eficiente: Descartar todos los números pares.

```python
def es_primo_3(n):
    if n <= 1:              # 1 o menores no son primos
        primo = False
    elif n == 2:            # El 2 es primo
        primo = True
    elif n % 2 == 0:        # Todo par mayor que 2 es primo
        primo = False
    else:
        primo = True
        i = 3
        while primo and i <= int(n ** 0.5):
            if n % i == 0:
                primo = False
            i += 2          # Pruebo solo con los impares
    return primo
```
