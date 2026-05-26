# Índices y Slices aplicados a strings

> **Importante**:
> Recordar que los strings son **inmutables**, por lo que algo como `string[2] = "x"` (que intenta modificar un caracter en específico del mismo) no es válido y generará un error.

---

## Índices

Los índices son números enteros que permiten acceder a un elemento determinado de una secuencia. Formalmente, el índice de un sub-elemento de una secuencia es el ordinal de dicho elemento, indica qué posición ocupa dentro de la secuencia. 

Sirven tanto para strings como para listas y tuplas (Unidad 6) y demás secuencias que no vemos en la materia.

Los índices van entre corchetes `[]`. De esta manera, `sec[ix]` denota el elmento en la posición `ix` de la secuencia `sec`.

## Valores válidos para los índices

### Índices no negativos (`>= 0`)

Para toda secuencia, su primer elemento es el correspondiente al ordinal cero (**la numeración de los sub-elementos de la secuencia comienza desde cero**) y su **último elemento es aquel cuyo ordinal es igual al largo de la secuencia** (la cantidad de sub-elementos que tiene, dado por `len`), **decrementado en 1**.

### Índices negativos (`< 0`)

Lo descrito en el párrafo anterior es válido para la mayoría de los lenguajes de programación (como `C`, `Java`, etc.). Además de éstos, Python agrega la posibilidad de acceder a la secuencia en su orden inverso (de derecha a izquierda) utilizando valores negativos como índices, donde:

* El índice `-1` denota al primer elemento de derecha a izquierda, que es el último de izquierda a derecha.
* El resto de los elementos se numeran `-2`, `-3`, `-4`, etc.
* Aquel índice negativo cuyo valor absoluto sea igual al largo de la secuencia (cuyo valor sea `-len(sec)` para una secuencia `sec`) denota al último elemento de derecha a izquierda, que es el primero de izquierda a derecha.


Para convertir un índice negativo a uno positivo, se puede usar la función `len()`, que devuelve la cantidad de elementos del iterable, y sumarle (que termina restando, ya que sumar un número negativo es, matemáticamente, como hacer una resta) el índice negativo deseado. Por ejemplo, para convertir el índice `-3` a uno positivo, se puede usar `len(string) - 3`.

### Resumen

De esta manera para una secuencia `sec` cuya longitud es `l` (de forma tal que `l = len(sec)`), los índices válidos para `sec` son aquellos del conjunto:

`{-l, -l+1, -l+2, ..., -2, -1, 0, 1, 2, ..., l-3, l-2, l-1}`

### Ejemplo

Por ejemplo, una secuencia de longitud `4` tiene por índices válidos:

`{-4, -3, -2, -1, 0, 1, 2, 3}`.

donde aquel con índice `0` o índice `-4` es el primer elemento (de izquierda a derecha) y aquel con índice `3` o índice `-1` es el cuarto y último elemento (de izquierda a derecha).

```python
x = "Hola"      # Indices validos: -4, -3, -2, -1, 0, 1, 2 y 3

print(x[0])     # Imprime "H"
print(x[1])     # Imprime "o"
print(x[2])     # Imprime "l"
print(x[3])     # Imprime "a"

print(x[-1])    # Imprime "a"
print(x[-2])    # Imprime "l"
print(x[-3])    # Imprime "o"
print(x[-4])    # Imprime "H"
```

### Utilidad

Utilizar índices negativos permite recorrer las secuencias en orden inverso de forma más fácil que con índices positivos. Esto es muy usado en ejercicios de la guía.

### Índices inválidos (`IndexError`)

Cualquier intento de acceso a un índice inválido en una secuencia resultará en un error de tipo `IndexError`. Python verifica la validez de los índices a la hora de acceder a los elementos de las secuencias`. Por ejemplo:

```python
x = "Hola"      # Indices validos: -4, -3, -2, -1, 0, 1, 2 y 3
print(x[4])     # IndexError: string index out of range
print(x[-5])    # IndexError: string index out of range
```

## Índices aplicados a strings

Un string es una secuencia que se itera por sus caracteres (sus sub-elementos son sus caracteres individuales, en orden), de manera tal que, al acceder mediante un índice a una posición determinada, se está accediendo a aquel caracter que ocupa esa posición en el string.

---

## Slices

Un _slice_ es una secuencia que se forma a partir de una porción de otra secuencia, delimitada por ciertos índices de la secuencia original. 

Los slices se utilizan para obtener una partición de distintos elementos que puedan iterarse, por ejemplo:
 * Listas
 * Strings
 * Tuplas

## Componentes de un slice

Un slice se compone de: `[inicio:fin:paso]` (y tiene esa sintaxis).

* `inicio`: Es el índice de inicio de la partición. Todos los elementos desde este índice en adelante son tomados al momento de generar la partición. 

  El inicio puede omitirse (siempre poniendo los dos puntos, pero omitiendo el número que va en ese lugar), en cuyo caso se asume que es `0` para pasos positivos, o `-1` para pasos negativos.

* `fin`: Es el índice de fin de la partición. Indica el elemento hasta el cual llegará la partición. Es importante tener en cuenta que el **elemento final no es incluído en la partición (llega hasta el elemento anterior)** (de forma similar a lo que ocurría con `range`). **Para incluir el elemento final en un slice se debe usar `len` de la secuencia sin restarle 1** como índice de fin.

  El final también puede omitirse, en cuyo caso se asume que es el último elemento del iterable (para pasos positivos), o el primero (para pasos negativos). Al igual que en el inicio, se agregan los dos puntos, pero no se pone el número que va en el lugar del fin.

* `paso`: Es el salto que se da entre los índices de `inicio` y `fin` (coloquialmente, "de a cuánto en cuánto saltar").

  También puede omitirse. En este caso, no es necesario poner los dos puntos finales, y se asume que el paso es `1` si el mismo se omite.

  * Cuando el paso es positivo (o se omite) el recorrido es de izquierda a derecha (orden natual).
  * Cuando el paso es negativo, el recorrido es de derecha a izquierda (orden inverso).

> **Muy importante**: A diferencia de los accesos a un elemento específico, que generan un `IndexError` en el caso de que el índice no esté dentro del rango [contemplado arriba](#valores-válidos-para-los-índices), los slices no generan errores por índices fuera de rango. Simplemente no incluyen a los elementos o generan strings vacíos. 
>
> Por ejemplo, un slice sobre un string de longitud 10 cuyo índice de fin sea 500 incluirá simplemente los elementos que contenga el string hasta el final del mismo, y nada más. Por esto, genera el mismo efecto terminar el slice en 10 que en 500 en este caso.

## Ejemplos de slices

Para los siguientes ejemplos, considerar el siguiente string de longitud 10.

```python
# Indices:  0123456789
string =   "Hola Mundo"

print(len(string)) # Imprime 10
```

### Ejemplos usando todo
```python
print(string[0:7])      # "Hola Mu"
print(string[0:8:2])    # "Hl u"
print(string[0:9:2])    # "Hl ud"
print(string[1:9:2])    # "oaMn"
print(string[5:5])      # "" (desde 5, hasta 5, sin incluir el 5)
print(string[5:2])      # "" (inicio mayor que fin y paso > 0, no incluye nada)
print(string[3:180])    # "a Mundo" (al pasarse de rango no genera error, solo 
                        # llega hasta donde puede)
print(string[100:200])  # "" (indices fuera de rango, no incluye nada)
```

### Ejemplos omitiendo inicio
```python
print(string[:7])      # "Hola Mu"
print(string[:8:2])    # "Hl u"
print(string[:9:2])    # "Hl ud"
```

### Ejemplos omitiendo fin

```python
print(string[6:])             # "undo"
print(string[6:len(string)])  # "undo" (es equivalente al ejemplo anterior)
print(string[2::3])           # "lMd"
print(string[2::2])           # "l ud"
```

### Ejemplos usando índices negativos

```python
print(string[-1])    # No es un slice, sino que simplemente accede al 
                     # último elemento
print(string[-7])    # "a"
print(string[-7:])   # Denota (del -7, que es la "a", como vimos), hasta
                     # el final. Imprime "a Mundo".
print(string[-2:])   # Denota (del -2, que es la "d", como vimos), hasta
                     # el final. Imprime "do".
print(string[-7:-2]) # "a Mun" (recordar que no incluye el último elemento)
```

### Ejemplos usando paso negativo

```python
print(string[::-1])     # "odnuM aloH" (imprime el string al revés)
print(string[::-2])     # "onMao" (imprime el string al revés, saltando de a 2)
print(string[-2:-8:-1]) # "dnuM a"
print(string[3:-4:-1])  # "" (inicio menor que fin, pero se está recorriendo 
                        # en sentido inverso, no incluye nada)
print(string[-4:3:-1], ".", sep="")  # "uM ." (el . al final es para que se vea
                                     # que el espacio esta incluyendose)
print(string[-5:2:-1])  # "M a"
```

### Utilidad: Invertir strings

Para invertir un string, basta con usar un slice con inicio y fin implícitos (omitidos) pero paso negativo de uno en uno (paso `-1`).

```python
string = "Este es un archivo teorico de Python"
string_invertido = string[::-1]
print(string_invertido)     # Imprime "nohtyP ed ociroet ovihcra nu se etsE"
```
