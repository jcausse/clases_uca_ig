> Antes de leer esta teórica, se recomienda leer:
> 
> `https://github.com/jcausse/clases_uca_ig/blob/main/unidad_1/Teoria/variables.py`

# Operadores

Un operador es un símbolo que se utiliza en una expresión para representar una operación a realizar entre uno o más operandos.

## Conceptos importantes:

- **Operación**: Algo que vamos a realizar.
    - **Operador**: Qué vamos a hacer. **LA OPERACIÓN QUE REALIZA UN OPERADOR DEPENDE DEL TIPO DE DATO DE SUS OPERANDOS**. Por ejemplo, `+` realiza una suma si sus operandos son numéricos (`int` o `float`), pero realiza una concatenación si sus operandos son cadenas de texto (`str`).
    - **Operando(s)**: El (los) dato(s) con los que vamos a realizar la operación.

- **Expresión**: Conjunto de operaciones que se realizan en un determinado orden, definido por la **precedencia** de los operadores

### Ejemplo

La expresión `3 + 2 * 5` tiene 2 operadores: `+` y `*`. La precedencia es aquello que define en qué orden se hacen las operaciones. Al igual que en matemática, primero se hace la multiplicación y luego la suma.

- Los operandos que aplican a `*` son `2` y `5`.
- Los operandos que aplican a `+` son `3` y el resultado de `2 * 5`.

## Aridad de operadores

La aridad de un operador indica la cantidad de operandos que se necesita para un operador.

- Aridad 1: "Unario". Por ejemplo, `~` y `not` son operadores unarios.

- Aridad 2: "Binario". Por ejemplo, `+`, `and` y `%` son operadores binarios. Obviamente, hay muchos más.

- Aridad 3: "Ternario". `___ if ___ else ___` es el operador ternario de Python, pero no lo vemos en Informática General UCA (y, debido a esto, no puede usarse).

## Operadores de Python

Python tiene distintos operadores, y cada uno de ellos puede tener más de un significado, según el (los) tipo(s) de dato de el (los) operando(s).

| Operador | Nombre                       | Tipo                       |
| -------- | ---------------------------- | -------------------------- |
| +        | Suma o concatenación         | Aritmético                 |
| -        | Resta                        | Aritmético                 |
| *        | Multiplicación               | Aritmético                 |
| **       | Potenciación                 | Aritmético                 |
| /        | División exacta              | Aritmético                 |
| //       | División entera              | Aritmético                 |
| %        | Módulo                       | Aritmético                 |
| <<       | Shift izquierdo              | Bitwise (operador de bits) |
| >>       | Shift derecho                | Bitwise (operador de bits) |
| &        | AND bit a bit                | Bitwise (operador de bits) |
| \|       | OR bit a bit                 | Bitwise (operador de bits) |
| ^        | XOR bit a bit                | Bitwise (operador de bits) |
| ~        | NOT bit a bit                | Bitwise (operador de bits) |
| <        | Menor                        | Comparación                |
| >        | Mayor                        | Comparación                |
| <=       | Menor o igual                | Comparación                |
| >=       | Mayor o igual                | Comparación                |
| ==       | Igual                        | Comparación                |
| !=       | Distinto                     | Comparación                |
| and      | Conjunción                   | Lógico                     |
| or       | Disyunción (inclusiva)       | Lógico                     |
| not      | Negación                     | Lógico                     |
| =        | Asignación                   | Asignación                 |
| +=       | Suma y asignación            | Asignación                 |
| -=       | Resta y asignación           | Asignación                 |
| *=       | Multiplicación y asignación  | Asignación                 |
| **=      | Potenciación y asignación    | Asignación                 |
| /=       | División exacta y asignación | Asignación                 |
| //=      | División entera y asignación | Asignación                 |
| %=       | Módulo y asignación          | Asignación                 |

## Operador `**`

El operador `**` es el operador de potenciación. `a ** b` representa `a` elevado a la potencia `b`.

Notar que, utilizando potencias fraccionarias, esto permite también calcular raíces. Según la propiedad matemática: 

`a ^ (1 / n) = raiz(n, a)` 

(donde `raiz(n, a)` representa a la raíz de índice `n` de `a`)

### Ejemplos

- `2 ** 5` devuelve `32`
- `16 ** 0.5` devuelve `4.0`
- `27 ** (1 / 3)` devuelve `3.0` (notar que `27 ** 1 / 3` devuelve `9.0` pues la potencia se resuelve antes que la división).

## Operador `/`

El operador de división exacta `/` devuelve el resultado de la división de la misma forma que lo veríamos en una calculadora.

Este operador siempre devuelve su resultado de tipo `float`, independientemente de si la división da un número entero o no.

### Ejemplos

- `5 / 2` devuelve `2.5`
- `4 / 2` devuelve `2.0`. Notar que el resultado, por más que es entero, es `float`:
    ```python
    >>> type(4 / 2)
    <class 'float'>
    ```

## Operador `//`

El operador de división entera `//` devuelve el resultado de la división entera o "división de escuela primaria", de la misma manera en la que lo hacíamos nosotros antes de conocer sobre la existencia de los números con coma.

Este operador siempre devuelve su resultado de tipo `int` cuando los operandos son enteros.

### Ejemplos

- `5 // 2` devuelve `2`.
- `4 // 2` devuelve `2`.

### Ejemplo avanzado

Este operador es el que, por ejemplo, usaríamos para obtener el elemento "del medio" de una lista. Notar que el siguiente código da un error:

```python
lista = [1, 5, 9, 8, 6]
print(lista[len(lista) / 2])
```

El error se debe a que los índices en una lista siempre deben ser números enteros, y `len(lista) / 2` devuelve `2.5`. El error permanece incluso cuando la lista tiene una cantidad par de elementos.

```python
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    print(lista[len(lista) / 2])
          ~~~~~^^^^^^^^^^^^^^^^
TypeError: list indices must be integers or slices, not float
```

Utilizando el operador `//` se resuelve el problema,

```python
lista = [1, 5, 9, 8, 6]
print(lista[len(lista) // 2])
```

El código de arriba imprime `9`.

## Operador `%`

[Ver el archivo dedicado](https://github.com/jcausse/clases_uca_ig/blob/main/unidad_1/Teoria/modulo(porcentaje).md).

## Operador `=`

El operador asignación es de los últimos en el orden de precedencia, lo que quiere decir que es el último en aplicarse. Siempre que en una expresión aparezca `=`, todas las demás operaciones se resuelven primero.

Este operador es binario y lleva:
- A la izquierda, una variable.
- A la derecha, un literal (un dato dado de forma directa) o una expresión.

`=` asigna el valor resultante de la expresión de la derecha a la variable que está a la izquierda. Esto es importante entenderlo pues uno tiende a pensar en `=` como un "igual en matemática", pero no lo es. Una forma de ver la diferencia es considerar la siguiente expresión:

`x = x + 1`

- En matemática es o una ecuación sin solución, o una igualdad falsa `x = x + 1 => x - x = 1 => 0 = 1, Absurdo!`.
- En programación, lo que realmente quiere decir es "tomar el valor actual de la variable `x`, sumarle 1, y guardar el resultado de la suma en la misma variable `x`.

Es importante notar el orden de las cosas. Supongamos que `x` vale `2`.

- Primero se toma el valor ACTUAL de `x` para hacer la cuenta (`2`).
- Segundo se incrementa en `1` (da `3`).
- Tercero se guarda el resultado (`3`) en `x`.

### Ejemplo avanzado

Consideremos:

```python
def cuadrado(x):
    return x * x

x = 2
x = cuadrado(x)
```

Es importante entender que cuando el valor de `x` es pasado a la función, se pasa el valor que `x` tenía hasta ese momento ANTES de ejecutar la línea `x = cuadrado(x)`, es decir, `2`. La asignación de `x` a su nuevo valor (`4`) se realiza DESPUÉS de que la función se haya ejecutado y haya retornado.

## Operadores `+=`, `-=`, `*=` etc.

Es muy común querer realizar una operación sobre una variable para luego guardar el resultado en la misma variable, es decir, modificar el valor de una variable. Por ejemplo (avanzado), muchas veces cuando hacemos un ciclo `while` queremos modificar la variable `i` para pasar a la siguiente iteración.

Con los operadores que vimos hasta ahora, incrementar en `1` el valor de `x` lo podíamos lograr mediante:

`x = x + 1`

Esto hacía:
- Tomar el valor de `x`.
- Sumarle `1`.
- Guardarlo nuevamente en `x`.

Debido a que estas operaciones son muy comunes, Python (como muchos otros lenguajes) ofrece una sintaxis reducida para hacer esto mismo, mediante el operador de suma y asignación `+=`.

- `x += 1` equivale a `x = x + (1)` (incremento en 1).
- `x += -5` equivale a `x = x + (-5)`
- `x -= 1` equivale a `x = x - 1` (decremento en 1).

Notar que la expresión a la derecha de `+=` aparece entre paréntesis. Esto no es casual, y toma más sentido cuando consideramos el operador `*=`. 

Supongamos que `x = 2`. Si `x *= 5 + 2` fuese equivalente a `x = x * 5 + 2`, el resultado debiera ser `12`. Ahora bien, el resultado de `x *= 5 + 2` es en realidad `14`, pues equivale a `x = x * (5 + 2)`. Siempre se hace la expresión a la derecha antes que la operación de asignación.

## Operadores lógicos (`and`, `or` y `not`)

[Ver el archivo dedicado](https://github.com/jcausse/clases_uca_ig/blob/main/unidad_3/Teoria/operadores_logicos.py).
