# Listas

## Indice

- [Listas](#listas)
  - [Indice](#indice)
  - [Concepto](#concepto)
  - [Sintaxis](#sintaxis)
    - [Ejemplo](#ejemplo)
    - [Ejemplo](#ejemplo-1)
  - [Creación de listas con `list()`](#creación-de-listas-con-list)
  - [Acceso a elementos](#acceso-a-elementos)
    - [Rango de índices](#rango-de-índices)
    - [Ejemplo](#ejemplo-2)
  - [Slices](#slices)
  - [Modificación de elementos](#modificación-de-elementos)
  - [Agregado e Inserción de elementos](#agregado-e-inserción-de-elementos)
    - [Método `append`](#método-append)
    - [Método `insert`](#método-insert)
    - [Operadores `+` y `+=`](#operadores--y-)
    - [Nota importante sobre `+` y `+=`](#nota-importante-sobre--y-)
  - [Eliminación de elementos](#eliminación-de-elementos)
    - [Método `pop`](#método-pop)
    - [Método `remove`](#método-remove)
  - [Iteración](#iteración)
    - [Por Elementos](#por-elementos)
    - [Por Índices](#por-índices)
  - [Operador de membresía](#operador-de-membresía)
    - [Ejemplo](#ejemplo-3)
    - [Caso de uso: eliminar todas las apariciones de un elemento](#caso-de-uso-eliminar-todas-las-apariciones-de-un-elemento)

## Concepto

Una lista es una estructura de datos que permite almacenar una colección **ordenada** y **mutable** de elementos. En algunos lenguajes de programación, es requisito que todos los elementos de una lista sean del mismo tipo de dato, pero no es el caso de Python. Python permite crear listas **heterogéneas**, donde cada elemento puede potencialmente tener un tipo de dato distinto de los demás, incluso existiendo la posibilidad de contener listas como elementos de otras listas, creando así estructuras multidimensionales.

Algunos conceptos importantes a tener en cuenta sobre las listas en Python:

- **Ordenada**: Los elementos dentro de una lista mantienen el orden en el que fueron insertados. Cada elemento tiene una posición específica (**índice**) que se utiliza para acceder a él. Al igual que en los _strings_, los índices comienzan en `0` y terminan en una posición menor en 1 al tamaño de la lista (`len(lista) - 1`). También, al igual que los _strings_ soportan índices negativos para acceder a los elementos desde el final de la lista. Los mismos comienzan en `-1` (último elemento de izquierda a derecha, que es el primero de derecha a izquierda), y terminan en `-len(lista)` (primer elemento de izquierda a derecha, que es el último de derecha a izquierda).
- **Mutable**: Los elementos de una lista pueden ser modificados (cambiar un elemento o valor por otro), se puede agregar nuevos elementos, y eliminarlos después de la creación de la lista. Puede ser modificada dinámicamente a lo largo del programa.
- **Heterogénea**: Las listas en Python pueden contener elementos de distintos tipos de datos simultáneamente.

## Sintaxis

Las listas se definen utilizando corchetes `[]` y separando los elementos por comas `,`. La sintaxis es:

```python
<variable> = [ <elemento 1> , <elemento 2> , <elemento 3>, ... ]
```

Notar que:

- Los elementos se encierran entre corchetes `[]`. La lista queda entonces definida con los elementos entre los corchetes.
- Los elementos se separan por comas `,` unos de otros.

### Ejemplo

La siguiente lista almacena una colección de notas de un examen (de tipo `float`).

```python
notas = [7.0, 4.5, 9.25, 2.5, 10.0, 5.25, 8.0]
```

Notar que: 

- Los elementos están ordenados, el primer elemento es `7.0`, el segundo `4.5`, y así sucesivamente.
- Los valores pueden repetirse (un alumno podría sacarse más de una vez la misma nota).

### Ejemplo

La siguiente lista almacena información de distintos vehículos, donde cada elemento es una lista que contiene los datos del auto [patente, marca, modelo, año]:

```python
autos = [
    ['AA123BB', 'Audi', 'R8', 2021],
    ['ABC123', 'Toyota', 'Corolla', 1997]
]
```

Notar que:

- En este caso, los elementos de la lista `autos` son a su vez listas.
- La cantidad de elementos de la lista `autos` es 2, y la cantidad de elementos de cada una de sus sublistas es 4. Los elementos internos de las sublistas no cuentan como elementos de la lista original, `autos`.
- Debido a que la cantidad de elementos de la lista `autos` es 2, entonces `len(autos)` devuelve 2.

## Creación de listas con `list()`

La función `list()` también nos permite crear listas vacías (en caso de que no le pasemos parámetros), o convertir otros iterables (como un _string_ o un _range_) en listas:

```python
lista_vacia = list()
print(lista_vacia) # Imprime []

texto = "Hola"
lista_caracteres = list(texto)
print(lista_caracteres) # Imprime ['H', 'o', 'l', 'a']

lista_numeros = list(range(2, 19, 2))
print(lista_numeros)    # Imprime [2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Para crear una lista vacía, sin embargo, no es necesario utilizar `list()`, sino que lo más común es crearla usando `[]`:

```python
nueva_lista_vacia = []
```

## Acceso a elementos

El acceso a los elementos de una lista se realiza a través de sus **índices**, de la misma manera que accedíamos a los caracteres específicos de un _string_.

Como vimos en el apunte de [Índices y Slices](https://github.com/jcausse/clases_uca_ig/blob/main/unidad_5/Teoria/3_slices_indices.md), los índices son números enteros que indican la posición de un elemento, comenzando desde `0` para el primer elemento, o desde `-1` para el último elemento (recorriendo de derecha a izquierda).

```python
<variable> = [ <elemento 1> , <elemento 2> , <elemento 3>, ... ]     # Define una lista
<variable>[<indice>]    # Accede al elemento en la posicion <indice>
```

Acceder a un índice que está fuera del rango válido de la lista (ya sea del rango positivo o del negativo) genera un error `IndexError`.

### Rango de índices

Recordemos que una lista de `n` (donde `n = len(lista)`) elementos tiene los siguientes índices válidos:

- **Índices positivos**: `0` hasta `n-1` (inclusive).
- **Índices negativos**: `-1` hasta `-n` (inclusive).

Por ejemplo, para una lista de tamaño 5, los índices positivos válidos son del 0 al 4, y los negativos del -1 al -5.

### Ejemplo

```python
notas = [7, 4, 9, 2, 10, 5, 8]
print(notas[0])             # Imprime 7 (primer elemento)
print(notas[2])             # Imprime 9 (tercer elemento)
print(notas[-1])            # Imprime 8 (ultimo elemento)
print(notas[10])            # Genera IndexError
```

## Slices

Al ser las listas secuencias, también soportan la notación de **slices** vista en el apunte de [Índices y Slices](https://github.com/jcausse/clases_uca_ig/blob/main/unidad_5/Teoria/3_slices_indices.md), que permite obtener sublistas. Por ejemplo:

```python
notas = [7, 4, 9, 2, 10, 5, 8]
print(notas[1:4])       # Imprime [4, 9, 2]

nombres = ['Martin', 'Pedro', 'Camila', 'Juan', 'Abril', 'Jose']
print(nombres[-4:])     # Imprime ['Camila', 'Juan', 'Abril', 'Jose']
print(nombres[-4::-1])  # Imprime ['Camila', 'Pedro', 'Martin']
```

> **Nota:** Cuando se aplica un _slice_ a una lista, incluso si dicho _slice_ tomara todos los elementos de la lista (por ejemplo como `nombres[:]`), el resultado siempre es una **nueva lista completamente independiente de la original**. Esto quiere decir que **cualquier posterior modificación sobre la lista resultante del _slice_ no generará cambio alguno sobre la lista original**.
>
> Esto es **MUY** importante entenderlo, ya que suele ser una trampa muy común en ejercicios de finales teóricos.

## Modificación de elementos

Dado que las listas son **mutables**, podemos usar los índices para modificar un elemento existente:

```python
notas = [7, 4, 9, 2, 10, 5, 8]
notas[0] = 10           # Modifica el primer elemento
print(notas)            # Imprime [10, 4, 9, 2, 10, 5, 8]
```

---

## Agregado e Inserción de elementos

Para agregar elementos a una lista, en esta materia utilizamos los métodos `append` e `insert`, o el operador de concatenación.

### Método `append`

Dada una variable de tipo lista, el método `<variable>.append(<elemento>)` agrega un elemento al **final** de la lista. Modifica la lista original, es decir, no retorna una lista nueva sino que el nuevo elemento pasa a formar parte de la lista que ya se tenía.

Como al agregar un elemento a la lista la misma se agranda, también cambia la `len`.

```python
l = [1, 2]
print(l)                # Imprime [1, 2]
print(len(l))           # Imprime 2

l.append(3)
print(l)                # Imprime [1, 2, 3]
print(len(l))           # Imprime 3

l.append(4)
l.append(5)
l.append(6)
print(l)                # Imprime [1, 2, 3, 4, 5, 6]
print(len(l))           # Imprime 6
```

### Método `insert`

Dada una variable de tipo lista, el método `<variable>.insert(<indice>, <elemento>)` inserta un elemento en la posición especificada por `<indice>`. El elemento que estaba en esa posición y aquellos en las siguientes posiciones se desplazan un lugar hacia la derecha.

```python
l = ['a', 'b', 'd', 'e']
print(l)                # Imprime ['a', 'b', 'd', 'e']
                        #           0    1    2    3
print(len(l))           # Imprime 4

# Inserta la 'c' en el indice 2 (la posicion que actualmente ocupa la 'd')
l.insert(2, 'c')
print(l)                # Imprime ['a', 'b', 'c', 'd', 'e']
                        #           0    1    2    3    4
print(len(l))           # Imprime 5
```

Como casos particulares, podemos considerar:
- **Insertar al principio:** Utilizar la función `insert` utilizando `0` como índice, provoca que el elemento a insertar pase a ocupar la posición `0`, estableciéndose como el nuevo primer elemento de la lista.
- **Insertar al final:** Si utilizáramos `len(lista) - 1` (que es el último índice válido de la lista) como índice de inserción, el elemento pasaría a ocupar el ante-último lugar. 

  Recordemos que el índice que se le pasa a `insert` es aquel que queremos que el nuevo elemento ocupe, por lo tanto, si a `insert` le proveemos el índice donde actualmente se encuentra el último elemento, el nuevo elemento ocupará su lugar, pero aquel que era anteriormente el último elemento será desplazado a la derecha 1 lugar, y quedará como último elemento otra vez.
  
  Para que logremos insertar al final, `insert` permite excepcionalmente utilizar un índice mayor en 1 al último válido, de esta manera indicándole que queremos que ocupe una posición siguiente a la última posición válida actual. Al utilizar `len(lista)` como índice (que para realizar un acceso a elemento generaría un `IndexError`), el nuevo elemento se inserta al final de la misma.

  De esta manera, para una lista `l`, `l.insert(len(l), <elem>)` inserta `<elem>` al final de `l`, lo que es exactamente equivalente a `l.append(<elem>)`.

```python
l = ['a', 'b', 'c', 'd']

l.insert(0, 'x')
print(l)                # Imprime ['x', 'a', 'b', 'c', 'd']

l.insert(len(l), 'y')
print(l)                # Imprime ['x', 'a', 'b', 'c', 'd', 'y']
```

### Operadores `+` y `+=`

El operador `+` funciona igual que en _strings_. Dadas dos listas, las concatena y genera una nueva lista resultado de la concatenación. Notar que esta lista generada es independiente de las dos primeras, de modo que cualquier modificación posterior sobre ellas no generará ningún efecto en la resultante de la concatenación. Por ejemplo:

```python
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

l3 = l1 + l2
print(l3)               # Imprime [1, 2, 3, 'a', 'b', 'c']

l1.append(4)
l2.append('d')

print(l1)               # Imrpime [1, 2, 3, 4]
print(l2)               # Imprime ['a', 'b', 'c', 'd']
print(l3)               # Imprime [1, 2, 3, 'a', 'b', 'c'] (igual que antes)
```

El operador `+=` hace lo mismo, pero en lugar de crear una lista nueva, modifica la lista de la izquierda. Por ejemplo:

```python
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

l1 += l2

print(l1)               # Imprime [1, 2, 3, 'a', 'b', 'c']
print(l2)               # Imprime ['a', 'b', 'c']
```

> **Nota:** Solamente pueden concatenarse iterables a las listas. Suponiendo `l = [1, 2, 3]`, las siguientes operaciones fallan:
>
> - `l += 4` (pretende agregar un `4` al final)
>   ```python
>   Traceback (most recent call last):
>    File "<python-input-1>", line 1, in <module>
>      l += 4
>   TypeError: 'int' object is not iterable
>   ```
>
> - `l = 1 + l` (pretende agregar un `1` al principio, generando una nueva lista)
>   ```python
>   Traceback (most recent call last):
>     File "<python-input-2>", line 1, in <module>
>       l = 1 + l
>           ~~^~~
>   TypeError: unsupported operand type(s) for +: 'int' and 'list'
>   ```
>
> Las formas correctas de cumplir con la intención expuesta son, respectivamente:
>
> - `l += [4]` (ahora `[4]` es una lista de un solo elemento).
> - `l = [1] + l` (ahora `[1]` es una lista de un solo elemento).




### Nota importante sobre `+` y `+=`

Antes de leer este apartado, leer: [Pasaje de Parámetros](https://github.com/jcausse/clases_uca_ig/blob/main/unidad_6/Teoria/pasaje_parametros.py).

La problemática que a continuación se plantea es muy importante tenerla en cuenta para exámenes finales teóricos.

En unidades anteriores se hablaba de que, por ejemplo, dado una variable numérica `i`, la operación `i = i + 1` es equivalente a `i += 1` (ambas incrementan en 1 la variable).

Si bien esto puede parecer que aplica también a las listas, eso es un **error**. La causa del error es la sutil pero muy importante diferencia de que el operador `+` genera una nueva lista y el `+=` modifica la lista original. De esta manera:

Considerar que se tienen:
- `l1 = [1, 2, 3]`
- `l2 = ['a', 'b', 'c']`

Entonces:
- La operación `l1 += l2` efectivamente modifica la lista `l1`.
- La operación `l1 = l1 + l2`, que parece lo mismo, en realidad lo que hace es generar una nueva lista que es la concatenación de `l1` con `l2` y luego reemplaza a la lista `l1` original con la nueva lista creada.

Si bien esto parece ser lo mismo (uno podría pensar que en todos los casos de uso es lo mismo modificar una lista que cambiarla su versión modificada), esto genera un error particular muy grave y muy difícil de detectar a la hora de pasar listas por parámetro.

Considerar el siguiente par de ejemplos:

```python
def foo(l):
  l += [4, 5]
  print(l)        # [1, 2, 3, 4, 5]

def main():
  l = [1, 2, 3]
  print(l)        # [1, 2, 3]
  foo(l)
  print(l)        # [1, 2, 3, 4, 5]

main()
```

```python
def foo(l):
  l = l + [4, 5]
  print(l)        # [1, 2, 3, 4, 5]

def main():
  l = [1, 2, 3]
  print(l)        # [1, 2, 3]
  foo(l)
  print(l)        # [1, 2, 3]

main()
```

Lo que pasó fue que `l += [4, 5]` en el primer ejemplo modificó la lista original. Pero en el segundo ejemplo pasó algo diferente:
- Se concatenó `l` con `[4, 5]`, generando `[1, 2, 3, 4, 5]`.
- La lista resultado de la concatenación fue una **nueva lista independiente de `l`**.
- Dicha nueva lista fue creada dentro de la función `foo`, por lo que es **local** a la función.
- Se utilizó la nueva lista para **reemplazar** sobre la variable `l` a la referencia que se tenía sobre la lista original de `main`.
- Al imprimir la lista, fue la nueva lista la que fue impresa.
- La función terminó, por lo que la lista nueva creada dentro de ella fue destruida.
- La lista original `l` nunca se modificó.

## Eliminación de elementos

Para eliminar elementos de una lista, utilizamos los métodos `pop` y `remove`.

### Método `pop`

El método `<variable>.pop(<indice>)` elimina y devuelve el elemento en la posición especificada por `<indice>`. 

Si no se especifica ningún índice, elimina y devuelve el **último** elemento de la lista (es equivalente a `<variable>.pop(-1)`).

Si se pasa un índice inválido o se intenta hacer un `pop()` sin parámetros sobre una lista vacía, genera un `IndexError`.

```python
l = ['a', 'b', 'c', 'd']

elemento = l.pop(1)
print(elemento)         # Imprime 'b'
print(l)                # Imprime ['a', 'c', 'd']

ultimo = l.pop()
print(ultimo)           # Imprime 'd'
print(l)                # Imprime ['a', 'c']

print(l.pop())          # Imprime 'c', l queda como ['a']
print(l.pop())          # Imprime 'a', l queda como []
print(l.pop())          # IndexError: pop from empty list
```

### Método `remove`

El método `<variable>.remove(<elemento>)` busca la **primera aparición** del elemento especificado y la elimina. 

Si el elemento aparece más de una vez, se elimina la primera aparición, y las siguientes no son eliminadas (un llamado exitoso a `remove` elimina siempre 1 solo elemento).

Si el elemento no se encuentra en la lista, genera un error `ValueError`.

```python
l = ['a', 'b', 'c', 'b', 'd']

l.remove('b')           # Elimina la primera 'b'
print(l)                # Imprime ['a', 'c', 'b', 'd']

l.remove('x')           # ValueError: list.remove(x): x not in list

l.remove('b')           # Elimina la 'b' que quedaba
print(l)                # Imprime ['a', 'c', 'd']

l.remove('b')           # ValueError: list.remove(x): x not in list
                        # Nota: Siempre dice x sin importar que elemento sea.
```

## Iteración

Para iterar una lista, podemos recorrerla por sus elementos o por sus índices.

Supongamos que tenemos la siguiente lista:

```python
l = [10, 20, 30]
```

### Por Elementos

Se toman los elementos de la lista uno por uno.
Esta es la forma más común y directa. Se puede realizar mediante un ciclo `for`:

```python
for elemento in l:      # Toma cada elemento y lo guarda en la variable elemento
    print(elemento)     # Imprime el elemento
```

La salida es:

```
10
20
30
```

### Por Índices

Se genera un rango numérico basado en la longitud de la lista (usando `len()`), iterando sobre los índices de la lista en lugar de sus elementos. Esto es útil si necesitamos conocer la posición del elemento o si queremos modificar los elementos de la lista mientras la iteramos (reemplazando mediante el acceso por índice).

```python
# len(l) es 3, por lo que range(len(l)) genera 0, 1, 2
for i in range(len(l)):
    print(f'En el indice {i} esta el elemento {l[i]}')
```

La salida es:

```
En el indice 0 esta el elemento 10
En el indice 1 esta el elemento 20
En el indice 2 esta el elemento 30
```

## Operador de membresía

El operador de membresía `in` nos permite conocer si un elemento pertenece a una lista. Este operador retorna un valor de tipo `bool` (`True` o `False`) indicando si el elemento está presente en la lista o no.

También podemos combinar el operador `not` con el de membresía `in` para obtener la negación del resultado.

### Ejemplo

```python
l = ['manzana', 'banana', 'pera']
print('banana' in l)    # Imprime True porque 'banana' esta en l
print('uva' in l)       # Imprime False porque 'uva' no esta en l

print('banana' not in l)# False (es falso que 'banana' no esta en l)
print('uva' not in l)   # True (es cierto que 'uva' no esta en l)
```

### Caso de uso: eliminar todas las apariciones de un elemento

Suponer que se tiene una lista como la siguiente:

```python
l = ['a', 'b', 'b', 'b', 'c', 'b', 'd', 'e', 'b', 'f', 'b']
```

Al utilizar `remove` para un elemento, se elimina siempre la primera aparición del elemento. Si el elemento no aparece en la lista, `remove` genera un error `ValueError` que aborta el programa.

Para poder eliminar un elemento de forma segura, primero se debe verificar que exista dentro de la lista, usando el operador de membresía, `in`:

```python
if <elemento> in <lista>:
    <lista>.remove(<elemento>)
```

Esto puede generalizarse con un ciclo para que elimine de forma segura todas las apariciones del elemento, de la siguiente forma:

```python
while <elemento> in <lista>:
    <lista>.remove(<elemento>)
```

Por ejemplo, para eliminar todas las letras `'b'` de la lista `l` anterior:

```python
l = ['a', 'b', 'b', 'b', 'c', 'b', 'd', 'e', 'b', 'f', 'b']

while 'b' in l:
    l.remove('b')

print(l)    # Imprime ['a', 'c', 'd', 'e', 'f']
```
