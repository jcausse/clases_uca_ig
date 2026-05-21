# Strings - Cadenas de Caracteres

## Concepto, Motivación e Historia

Un _string_ es un objeto pensado para representar una colección ordenada de caracteres con alguna codificación determinada (generalmente [Unicode](https://en.wikipedia.org/wiki/Unicode), que es la que utiliza Python). A esta colección con un orden la llamamos una **cadena de caracteres**.

El soporte para cadenas de caracteres no es algo que introduce Python, sino que ya estaba implementado en lenguajes anteriores (como C, en el cual el intérprete estándar de Python está escrito), pero con ciertas limitaciones.

En C, por ejemplo, las cadenas de caracteres no son un tipo de dato especial (no existe un tipo `str` como en Python), sino que una cadena está conformada por un montón de caracteres contiguos en la memoria y un caracter especial que marca el fin de la cadena. 

Además, el soporte para cadenas de C está (en principio) limitado a la codificación de caracteres [ASCII](https://en.wikipedia.org/wiki/ASCII), que es anterior a la codificación Unicode y muchísimo más limitada (en la cantidad y variedad de caracteres representados), y de la cual Unicode extiende. **El hecho de que Unicode extienda al estándar ASCII quiere decir que agregar nuevos caracteres por sobre los ASCII, pero que la codificación de los caracteres que ASCII ya incluía no cambia, de manera que Unicode sea retrocompatible con ASCII**.

### Codificación ASCII

Por simplicidad, la mayoría de los ejercicios de la materia asumen que trabajamos con caracteres ASCII justamente para hacer que los ejercicios sean mas sencillos de programar.

Dentro de los caracteres ASCII:

- No hay letras acentuadas (á, é, Á, É, etc.)
- No hay enie (ñ).
- No hay algunos de los símbolos que se utilizan en español, como `¿` o `¡`.

Ahora bien, **¿qué es una codificación?**

Una codificación de caracteres es una función biyectiva que a cada caracter representable para un determinado grupo de caracteres le asigna un valor numérico. Como la computadora internamente trabaja con datos numéricos, tiene sentido asociar caracteres a valores numéricos ya que provee una forma inmediata de representar los caracteres en la memoria.

El hecho de que esta función sea **biyectiva** implica que:

- Es **inyectiva**, lo cual implica que a cada caracter de la codificación le asigna un valor numérico distinto (no hay dos caracteres que compartan codificación).
- Es **sobreyectiva**, lo cual implica que para cada caracter de la codificación existe un número que lo representa (y que es el resultado de aplicar la función de "mapeo" a ese caracter).

Dicha función resulta de un dominio discreto (finito y con elementos claramente distinguidos), lo que hace ideal su representación en forma de tabla. 

Cuando utilizamos la codificación ASCII, dicha tabla de representación es la famosa [Tabla ASCII](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/960px-ASCII-Table-wide.svg.png).

## Usos prácticos de la codificación

Analicemos cómo podemos utilizar esta codificación para resolver ejercicios.

### Funciones `ord()` y `chr()` de Python

`ord()` y `chr()` son dos funciones directamente asociadas a la codificación. 

En los párrafos anteriores se mencionó que una codificación es esencialmente una función biyectiva entre un grupo de caracteres dado como dominio y los números naturales como codominio.

Dicha función biyectiva es `ord()`. Esta función toma un caracter como parámetro y devuelve un número entero que es aquel que representa a ese caracter en la codificación Unicode. Ahora bien, como Unicode es compatible con ASCII, dicho número también es el que representa al caracter en la tabla ASCII. De aquí se obtiene que, por ejemplo:

- `ord('A')` devuelve `65` pues 65 es la codificación de la letra A mayúscula en la tabla ASCII.
- `ord('@')` devuelve `64` pues 64 es la codificación de @ en la tabla ASCII.
- `ord('s')` devuelve `115` pues 115 es la codificación de la letra s minúscula en la tabla ASCII.

Como `ord()` es una función biyectiva, admite inversa. `chr()` es la función inversa de `ord()`, por lo que dado un número entero devuelve el caracter que es representado por dicho número. Entonces:

- `chr(65)` devuelve `A`.
- `chr(64)` devuelve `@`.
- `chr(115)` devuelve `s`.

A modo de resumen, el nombre de la función indica aquello que obtenemos de ella (lo que devuelve).

| **Función** | **Nombre**  | **Recibe** | **Devuelve**                |
|-------------|-------------|------------|-----------------------------|
| `ord()`     | _ordinal_   | Caracter   | El número que lo representa |
| `chr()`     | _character_ | Número     | El caracter que representa  |

### Análisis de la Tabla ASCII

Hay 3 "propiedades" intrínsecas de la propia codificación elegida al crear el estándar ASCII que son interesantes y son la clave para resolver varios de los ejercicios. Conviene memorizarlas.

<u>Primera propiedad</u>

Las letras mayúsculas y minúsculas y los dígitos están contiguos en la tabla.

- A la letra `A` le sigue la `B`... hasta la `Z`.
- A la letra `a` le sigue la `b`... hasta la `z`.
- Al digito `0` le sigue el `1`... hasta el `9`.

Consecuencia inmediata de esto es que los ordinales son consecutivos, de forma que: 

- `ord('B') = ord('A') + 1`.
- `ord('b') = ord('a') + 1`.
- `ord('1') = ord('0') + 1`.

Mucho cuidado, que el bloque de los dígitos, de las mayúsculas y de las minúsculas no son consecutivos entre sí.

<u>Segunda propiedad</u>

Las codificaciones de las letras minúsculas (los números que representan a las minúsculas) son mayores que las de las mayúsculas. Esto implica que el bloque de letras mayúsculas aparece antes en la tabla que el bloque de las minúsculas.

<u>Tercera propiedad</u>

La diferencia entre la codificación de cualquiera de las 26 letras mayúsculas del alfabeto inglés y su respectiva minúscula es siempre `32` (dado que son contiguas). De esta forma, se cumple que:

- `ord('a') = ord('A') + 32`
- `ord('A') = ord('a') - 32`
- `ord('t') = ord('T') + 32`
- `ord('T') = ord('t') - 32`

y así sucesivamente para cada letra del abecedario.

### Conversiones entre mayúsculas y minúsculas

Debido a las propiedades anteriores, convertir una letra a minúscula puede hacerse mediante los siguientes pasos:

```python
s_mayuscula = 'S'
ord_s_mayuscula = ord('S')
ord_s_minuscula = ord('S') + 32
s_minuscula = chr(ord('S') + 32)
```

Esto podemos resumirlo en la siguiente expresion para cualquier letra mayúscula almacenada en una variable `letra_mayus`:

```python
letra_minus = chr(ord(letra_mayus) + 32)
```

De la misma forma se realiza la conversión de minúsculas a mayúsculas:

```python
letra_mayus = chr(ord(letra_minus) - 32)
```

Por otro lado, los operadores de comparacion pueden comparar strings. Para el caso particular de los caracteres, que en Python son representados por objetos `str` (strings) unitarios (es decir, cuya `len` es igual a `1`), la comparación se hace mediante la codificación de cada caracter. De esta manera:

- `'A' < 'a'` resulta verdadero por segunda propiedad.
- `'T' > 'e'` resulta falso por la misma razón.
- `'T' > 'E'` y `'t' > 'e'` son ambas verdaderas (comparar dos letras mayúsculas o dos letras minúsculas coincide con su comparación alfabética).
- `'0' < '2'` es verdadero.
- `'3' < '1'` es falso.
- `'2' < 'A'` es verdadero dado el orden de la tabla ASCII.

La comparación que nos interesa a los efectos de conversión es aquella que nos permita decidir si una letra es mayúscula o minúscula. Para ello:

- La expresión `'A' <= c and c <= 'Z'` resulta verdadera solo cuando `c` es una letra mayúscula, y falsa en caso contrario.
- La expresión `'a' <= c and c <= 'z'` resulta verdadera solo cuando `c` es una letra minúscula, y falsa en caso contrario.

De esta forma, es posible programar las funciones _booleanas_ `es_mayuscula` y `es_minuscula`, que son muy útiles para los ejercicios:

```python
def es_mayuscula(c):
    return 'A' <= c and c <= 'Z'

def es_minuscula(c):
    return 'a' <= c and c <= 'z'
```

Combinando estas funciones con la conversión anteriormente explicada, podemos programar dos funciones igualmente útiles:

- `a_minuscula`, que toma un caracter `c` cualquiera y:
  - Si `c` es una letra mayúscula, devuelve su respectiva minúscula. 
  - Si `c` ya es una letra minúscula o es otro caracter, lo devuelve sin modificarlo.
- `a_mayuscula`, que toma un caracter `c` cualquiera y:
  - Si `c` es una letra minúscula, devuelve su respectiva mayúscula. 
  - Si `c` ya es una letra mayúscula o es otro caracter, lo devuelve sin modificarlo.

```python
def a_minuscula(c):
    if es_mayuscula(c):
        c = chr(ord(c) + 32)
    return c

def a_mayuscula(c):
    if es_minuscula(c):
        c = chr(ord(c) - 32)
    return c
```
