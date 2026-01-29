# Diccionarios

## Indice

- [Concepto](#concepto)
- [Sintaxis](#sintaxis)
- [Acceso a Elementos](#acceso-a-elementos)
- [Inserción de Elementos](#inserción-de-elementos)
- [Iteración](#iteración)
  - [Por Claves](#por-claves)
  - [Por Valores](#por-valores)
  - [Por Ítems](#por-ítems)
- [Operador de Membresía](#operador-de-membresía)
  - [Caso de Uso](#caso-de-uso)
- [Casos de Uso de Diccionarios](#casos-de-uso-de-diccionarios)
  - [Diccionarios de Variables Contadoras](#diccionarios-de-variables-contadoras)
  - [Diccionarios de Variables Acumuladoras](#diccionarios-de-variables-acumuladoras)

---

## Concepto

Un diccionario es una estructura de datos en principio, **sin orden** (pero, a partir de Python 3.7 los elementos mantienen el orden de inserción) formada por **pares clave-valor**.

Un par **clave-valor** es un par (en el sentido matemático) de dos elementos, llamados:

- **Clave (Key)**: Es un elemento **único** que **identifica de forma unívoca al par**, no puede repetirse, es decir, **no puede haber dos pares en un mismo diccionario que tengan la misma clave**. Los diccionarios de Python puede tener claves heterogéneas, es decir, Python soporta que haya claves con distintos tipos de dato dentro de un mismo diccionario.
- **Valor (Value)**: Es un elemento que puede ser de cualquier tipo de dato, que "acompaña" a la clave. Se dice que dicho **valor está asociado a la clave**.

**Nota importante**: las claves deben ser de tipos inmutables (o más técnicamente, _hashables_).

---

## Sintaxis

La sintaxis de un diccionario es:

```python
<variable> = {
    <clave 1> : <valor 1> ,
    <clave 2> : <valor 2> ,
    <clave 3> : <valor 3>
}
```

Notar que:

- Los pares clave-valor se encierran entre llaves `{}`. El diccionario se define de esta forma.
- Se utiliza un `:` para separar una clave de su valor asociado (`<clave> : <valor>`).
- Los pares clave-valor se separan por comas `,` unos de otros.

### Ejemplo 1

El siguiente diccionario almacena información sobre los resultados de un examen.

- Las claves son las posibles notas del examen (`int` de 1 a 10).
- Los valores indican la cantidad de alumnos que se sacaron esa nota.

```python
notas = {
    1: 2,
    2: 5,
    3: 2,
    4: 8,
    5: 10,
    6: 9,
    7: 15,
    8: 10,
    9: 8,
    10: 4
}
```

Notar que: 

- Tanto claves como valores están formadas por un único elemento.
- Las claves (números a la izquierda del `:`) no se repiten.
- Los valores (números a la derecha del `:`) pueden repetirse (por ejemplo, la cantidad de personas que sacó 5 es igual que la cantidad de personas que sacó 8).

### Ejemplo 2

El siguiente diccionario almacena información sobre distintos vehículos, donde la clave es la patente del vehículo (de tipo `str`), y los valores asociados a las claves son tuplas donde:

- El primer elemento es la marca (`str`).
- El segundo elemento es el modelo (`str`).
- El tercer elemento es el año (`int`).
- El cuarto elemento indica el valor anual de la patente de ese auto (`float`).

```python
autos = {
    'AA123BB': ('Audi', 'R8', 2021, 5732425.59),
    'ABC123': ('Toyota', 'Corolla', 1997, 59342.50)
}
```

Es importante notar que los valores asociados a las claves no son varios elementos. Al igual que en el ejemplo anterior, cada par tiene una clave que consta de un único elemento, y un valor que también consta de un único elemento, que en este caso es una tupla. Lo que hay de distinto en este ejemplo es que el valor "empaqueta" varios subelementos dentro.

---

## Acceso a elementos

El acceso a los elementos de un diccionario difiere del de las listas o tuplas. Recordar que el acceso a las listas y a las tuplas se hace a través de sus índices.

Por ejemplo:

```python
# Es una lista
l = ['hola', 'buen', 'dia']

# Imprime el elemento 0 (el primero), que es 'hola'
print(l[0])

# Es una tupla
t = (5, 7, 9)

# Imprime el elemento 2 (el tercero), que es 9
print(t[2])
```

Recordemos que el acceso a un índice inválido en una lista o tupla genera un `IndexError`, como se puede ver acá:

```python
l = ['hola', 'buen', 'dia']
print(l[3])     # Indice invalido

# Da error:
# IndexError: list index out of range
```

El acceso a los diccionarios se realiza a partir de sus claves, colocando la clave a la que queremos acceder entre corchetes `[]`, como se ve acá:

```python
<variable> = {...}      # Define un diccionario
<variable>[<clave>]     # Accede a la clave <clave> y devuelve su valor asociado
```

Acceder a una clave que no existe usando los corchetes `[]` genera un error `KeyError`.

Otra forma de acceder a los elementos de un diccionario es mediante el método `get`. `<diccionario>.get(<clave>)` devuelve el valor asociado a esa clave. A diferencia del acceso a través de corchetes `[]`, el acceso usando `get` devuelve `None` si la clave no existe, en lugar de producir un `KeyError`.

### Ejemplo 1

Usando el ejemplo 1 anterior:

```python
print(notas[7])             # Imprime 15
print(notas.get(11))        # Imprime None
print(notas[11])            # Genera KeyError
```

### Ejemplo 2

Usando el ejemplo 2 anterior:

```python
print(autos['AA123BB']) # Imprime ('Audi', 'R8', 2021, 5732425.59)
print(autos['XYZ999'])  # Genera KeyError
print(autos[0])         # Genera KeyError
```

Recordar que no se puede acceder utiizando índices, ya que son estructuras (en principio) sin orden.

---

## Inserción de elementos

Para insertar un elemento en un diccionario, se usa una sintaxis similar a aquella para acceder por corchetes `[]`, pero se le suma una asignación. La sintaxis es:

```python
<variable> = {...}
<variable>[<clave>] = <valor>
```

Se agrega el par `<clave> : <valor>` al diccionario `<variable>`.

**MUY IMPORTANTE**:

- Si la clave no existe en el diccionario (i.e., no existe ningun par clave-valor con esa clave), se inserta un nuevo par clave-valor.
- Si la clave ya existe en el diccionario (i.e., ya existe un par clave valor que tiene esa misma clave), el valor anterior será reemplazado por el nuevo valor.

### Ejemplo

```python
d = {'a': 1, 'b': 2}
print(d)                # Imprime {'a': 1, 'b': 2}

d['c'] = 3
print(d)                # Imprime {'a': 1, 'b': 2, 'c': 3}

d['b'] = 4
print(d)                # Imprime {'a': 1, 'b': 4, 'c': 3}
```

---

## Iteración

Para iterar un diccionario, podemos recorrerlo mediante sus claves, sus valores, o sus ítems.

Supongamos que tenemos el siguiente diccionario:

```python
d = {'a': 1, 'b': 2, 'c': 3}
```

### Por Claves

Se toman las claves una por una.
Esta es la forma por defecto de recorrido. Se puede reaizar mediante un ciclo `for`, de las siguientes dos formas:

Forma 1:

```python
for k in d:             # Toma cada clave y la guarda en la variable k
    print(k)            # Imprime la clave
```

Forma 2:

```python
for k in d.keys():      # Toma cada clave y la guarda en la variable k
    print(k)            # Imprime la clave
```

No es necesario especificar que se desea iterar por claves, pero puede hacerse usando `.keys()`.

En ambos casos, la salida es:

```
a
b
c
```

### Por Valores

Se toman los valores uno por uno.

```python
for v in d.values():    # Toma cada valor y la guarda en la variable v
    print(v)            # Imprime el valor
```

Es necesario especificar que se desea iterar por valores usando `.values()`.

La salida es:

```
1
2
3
```

### Por Ítems

> **IMPORTANTE**: No está permitido usr la función `.items()` en Informática General UCA. Esta sección es solo informativa.

Se toman los pares clave-valor uno por uno. Un ítem es una tupla de dos elementos donde:

- El primer elemento es la clave.
- El segundo elemento es su valor asociado.

```python
for i in d.items():     # Toma cada item y la guarda en la variable i
    print(i)            # Imprime el item
```

Es necesario especificar que se desea iterar por valores usando `.items()`.

La salida es:

```
('a', 1)
('b', 2)
('c', 3)
```

---

## Operador de membresía

El operador de membresía `in` nos permite conocer si una clave ya pertenece a un diccionario (de la misma forma que nos permite conocer si un elemento pertenece o no a una lista o tupla). Este operador retorna un valor de tipo `bool` (`True` o `False`) indicando si un elemento es o no clave del diccionario.

También podemos combinar el operador `not` con el de membresía `in` para obtener la negación del resultado.

### Ejemplo

```python
d = {'a': 1, 'b': 2}
print('a' in d)         # Imprime True porque 'a' es clave en d
print('c' in d)         # Imprime False porque 'b' no es clave en d
print(1 in d)           # Imprime False porque 1 es un valor, no una clave

print('a' not in d)     # False (es falso que 'a' no es clave de d)
print('c' not in d)     # True (es cierto que 'c' no es clave de d)
```

### Caso de uso

Estos operadores se usan mucho para verificar si un elemento está o no dentro del diccionario, y poder tomar acciones en consecuencia.

En este ejemplo se tiene una fiesta, y se registra qué trajo cada invitado:

```python
def registrar_invitado(invitados, nombre, item):
    """
    Invitados: diccionario de invitados
    Nombre: nombre del invitado
    Item: que trajo a la fiesta
    """
    if nombre not in invitados:
        invitados[nombre] = item
        print(f'Hola {nombre}! Gracias por traer {item}.')
    else:
        print(f'{nombre} ya estaba en la fiesta.')

invitados = {}

# Hola Juan! Gracias por traer Fernet.
registrar_invitado(invitados, 'Juan', 'Fernet')

# Hola Maria! Gracias por traer Coca.
registrar_invitado(invitados, 'Maria', 'Coca')

print(invitados) # {'Juan': 'Fernet', 'Maria': 'Coca'}

# Juan ya estaba en la fiesta
registrar_invitado(invitados, 'Juan', 'Hielo')

print(invitados) # {'Juan': 'Fernet', 'Maria': 'Coca'}
```

---

## Casos de uso de diccionarios

### Diccionarios de variables contadoras

En la fiesta de uno de los ejemplos anteriores se organizan juegos, y se compite entre 3 equipos: Rojo, Verde, y Azul.

Se cuenta con la siguiente lista que muestra el equipo que resultó ganador en cada juego:

```python
# El equipo Verde gano 4 juegos
# El equipo Rojo gano 3 juegos
# El equipo Azul gano 2 juegos

ganadores = ['Rojo', 'Azul', 'Rojo', 'Verde', 'Verde', 'Verde', 'Azul', 'Verde', 'Rojo']
```

El siguiente código cuenta la cantidad de victorias por cada equipo, usando un dicionario. Las claves del diccionario son los nombre de los equipos (y cada uno aparece una única vez). El valor asociado a cada clave es una variable de tipo `int` que conforma un contador. Los contadores inician en cero y se van incrementando a medida que se van encontrando victorias para ese equipo en la lista.

```python
contadores = {}

for equipo in ganadores:            # Para cada equipo en la lista
    if equipo not in contadores:    # Si el equipo no esta agregado al diccionario
        contadores[equipo] = 1      # Agrego el par clave-valor con valor 1
    else:                           # Si el equipo ya estaba en el diccionario
        contadores[equipo] += 1     # Le sumo 1 a la variable contadora correspondiente
```

- Cuando tomo el primer elemento de la lista `'Rojo'`, dado que el mismo no está en el diccionario, se agrega con valor `1`.
  - `contadores = {'Rojo': 1}`
- Cuando tomo el segundo elemento de la lista `'Azul'`, dado que el mismo no está en el diccionario, se agrega con valor `1`.
  - `contadores = {'Rojo': 1, 'Azul': 1}`
- Cuando tomo el tercer elemento de la lista `'Rojo'`, dado que el mismo ya está en el diccionario, se incrementa su valor.
  - `contadores = {'Rojo': 2, 'Azul': 1}`
- y así sucesivamente.

El proceso de adición completo puede visualizarse con este código:

```python
ganadores = ['Rojo', 'Azul', 'Rojo', 'Verde', 'Verde', 'Verde', 'Azul', 'Verde', 'Rojo']
contadores = {}

for equipo in ganadores:
    print(f'Equipo:{equipo}')
    print(f'\tAntes de agregar: {contadores}')
    if equipo not in contadores:
        print("\tNo estaba, se agrega.    \t")
        contadores[equipo] = 1
    else:
        print("\tYa estaba, se incrementa.\t")
        contadores[equipo] += 1
    print(f'\tDespues de agregar: {contadores}')
```

Que genera la siguiente salida:

```
Equipo:Rojo
        Antes de agregar: {}
        No estaba, se agrega.    
        Despues de agregar: {'Rojo': 1}
Equipo:Azul
        Antes de agregar: {'Rojo': 1}
        No estaba, se agrega.    
        Despues de agregar: {'Rojo': 1, 'Azul': 1}
Equipo:Rojo
        Antes de agregar: {'Rojo': 1, 'Azul': 1}
        Ya estaba, se incrementa.
        Despues de agregar: {'Rojo': 2, 'Azul': 1}
Equipo:Verde
        Antes de agregar: {'Rojo': 2, 'Azul': 1}
        No estaba, se agrega.    
        Despues de agregar: {'Rojo': 2, 'Azul': 1, 'Verde': 1}
Equipo:Verde
        Antes de agregar: {'Rojo': 2, 'Azul': 1, 'Verde': 1}
        Ya estaba, se incrementa.
        Despues de agregar: {'Rojo': 2, 'Azul': 1, 'Verde': 2}
Equipo:Verde
        Antes de agregar: {'Rojo': 2, 'Azul': 1, 'Verde': 2}
        Ya estaba, se incrementa.
        Despues de agregar: {'Rojo': 2, 'Azul': 1, 'Verde': 3}
Equipo:Azul
        Antes de agregar: {'Rojo': 2, 'Azul': 1, 'Verde': 3}
        Ya estaba, se incrementa.
        Despues de agregar: {'Rojo': 2, 'Azul': 2, 'Verde': 3}
Equipo:Verde
        Antes de agregar: {'Rojo': 2, 'Azul': 2, 'Verde': 3}
        Ya estaba, se incrementa.
        Despues de agregar: {'Rojo': 2, 'Azul': 2, 'Verde': 4}
Equipo:Rojo
        Antes de agregar: {'Rojo': 2, 'Azul': 2, 'Verde': 4}
        Ya estaba, se incrementa.
        Despues de agregar: {'Rojo': 3, 'Azul': 2, 'Verde': 4}
```

### Diccionarios de variables acumuladoras

Supongamos muchos amigos se reúnen y tienen el siguiente archivo `CSV` con un pedido de empanadas (cada amigo agregó varias entradas con los gustos que quería pedir y la cantidad):

`empanadas.csv`:

```csv
GUSTO,CANTIDAD
carne,2
jamon y queso,3
carne,4
humita,1
jamon y queso,5
cebolla y queso,4
carne picante,2
capresse,4
jamon y queso,6
```

Para hacer el pedido de forma más eficiente, se arma un programa que lee el archivo, cuenta cuántas empanadas se quieren pedir de cada gusto, e imprime los gustos y la cantidad total por gusto. Además imprime el total de empanadas a pedir.

```python
pedido = {}
total = 0

# Abrimos el archivo para lectura
with open('empanadas.csv', 'r') as file:

    # Quitamos el encabezado
    file.readline()

    # Para cada linea en el archivo
    for line in file:

        # Proceso la linea, y la separo en gusto y cantidad
        # Devuelve lista de str
        gusto, cant = line.strip().split(',')
        # Convierto a int la cantidad
        cant = int(cant)

        # Si ese gusto no esta aun en el pedido
        if gusto not in pedido:
            # Agrego el gusto al pedido, con la cantidad pedida
            pedido[gusto] = cant

        # Si ese gusto ya esta en el pedido
        else:
            # No agrego nuevamente el gusto, solo le sumo al
            # valor del diccionario la cantidad nueva a la cantidad
            # acumulada anteriormente
            pedido[gusto] += cant

        # Independientemente de si estaba o no en el diccionario, sumo
        # todas las cantidades (esta es una variable acumuladora comun
        # y corriente)
        total += cant

print(f'Empanadas totales: {total}')
print(pedido)
```

Produce la siguiente salida:

```
Empanadas totales: 31
{'carne': 6, 'jamon y queso': 14, 'humita': 1, 'cebolla y queso': 4, 'carne picante': 2, 'capresse': 4}
```
