# Estructuras de decisión

## Concepto

Las estructuras de decisión o sentencias de control son "bloques constructivos" de un programa que permiten tomar decisiones en base a una o varias condiciones, y ramificar el flujo de ejecución ("por qué líneas de código pasa el programa") de forma que se puedan tomar determinadas acciones para cada rama de dicho flujo de ejecución.

## Ejemplo

Este concepto de tomar decisiones y ramificar nuestras acciones aplica tanto en programación como en la vida cotidiana.

Por ejemplo, todas las mañanas tengo que decidir qué tomar con el desayuno. Supongamos que tengo 3 opciones:
- Té
- Café
- Mate

Para eliminar ambigüedad, vamos a suponer que tengo un orden de preferencias definido:
1. Té
2. Café
3. Mate

Ahora bien, cada infusión requiere de un insumo para prepararse, que puedo o puedo no tener en la alacena un día determinado. Entonces, el hecho de que pueda preparar o no una infusión depende de si tengo el insumo que necesito o no. Entonces:
- Para preparar el té necesito un saquito de té y agua caliente.
- Para preparar café necesito café molido, un filtro y agua caliente.
- Para preparar el mate necesito yerba y agua caliente.

Esto naturalmente induce ciertas precondiciones que deben darse para poder preparar cada bebida. Uno naturalmente puede tomar la decisión de qué bebida preparar en base a la siguiente descripción:

- `?` Si tengo agua caliente:
    - `?` Si tengo saquitos de té:
        - `>` Preparo té.
    - `?` En caso contrario, y si tengo café molido y filtros:
        - `>` Preparo café.
    - `?` En caso contrario, y si tengo yerba:
        - `>` Preparo mate.
    - `?` En caso contrario (si no tengo nada de todo eso):
        - `>` No preparo nada.

- `?` En caso contrario (no tengo agua caliente):
    - `>` No preparo nada.

Notar que en toda esta descipción existen dos tipos de expresiones:
- **Condiciones** (marcadas con `?`).
- **Acciones** (marcadas con `>`).

## Condiciones

Una **condición** es una expresión a la cual se asocia un valor de verdad, que resulta de evaluar la expresión. Los valores de verdad son valores que se denominan _booleanos_ porque se asocian al [Álgebra de Boole](https://en.wikipedia.org/wiki/Boolean_algebra), y son bi-valuados, pueden valer:
- Verdadero (en Python, `True`).
- Falso (en Python, `False`).

Los operadores condicionales de Python (como pueden ser `==`, `!=`, `>`, `>=`, etc.) generan valores _booleanos_

```python
>>> x = 3
>>> y = 4
>>> x == 2
False
>>> x <= y
True
>>> y != 5
True
```

## Acción

Las acciones son grupos de instrucciones que uno realiza en base a si sucedió o no determinada condición.

---

# Estructuras de control en Python

Python define un grupo de palabras reservadas en su sintaxis para poder implementar esta idea de toma de decisiones y ramificación del flujo de ejecución:

- `if`
- `elif`
- `else`
- `match` y `case` (no se ven en Informática General UCA).

## `if`

El condicional `if` es el más básico, y permite ejecutar un determinado código en el caso de que una condición resulte evaluada como verdadera (`True`).

Python requiere de una condición que debe ir al lado del `if`, y un grupo **no vacío** de líneas de código como cuerpo, que son aquellas que se ejecutarán cuando la condición sea verdadera.

En el caso en el que la condición resulte falsa, el cuerpo del `if` no es ejecutado, y el flujo del programa continúa por la próxima instrucción que esté fuera del `if`.

```python
if <CONDICION>:
    <CUERPO (grupo de acciones)>
    <CUERPO (grupo de acciones)>
    <CUERPO (grupo de acciones)>
```

## `else`

`else` es opcional, y me permite indicar qué hacer "en caso contrario" de un `if`, es decir, qué acción tomar cuando la condición de un `if` resulte `False`.

De aquí se deducen tres cosas muy importantes:
- **Solo puede haber a lo sumo un `else` por cada `if`**.
- **No puede haber un `else` sin un previo `if`**.
- **Los `else` no requieren (y no admiten) condiciones, ya que trabajan con la condición del `if` previo**.

```python
if <CONDICION>:
    <CUERPO DEL IF>
    <CUERPO DEL IF>
    <CUERPO DEL IF>
else:
    <CUERPO DEL ELSE>
    <CUERPO DEL ELSE>
    <CUERPO DEL ELSE>
```

> **Nota**: Cuando se tiene una estructura `if` / `else`, siempre se ejecuta alguno de los dos cuerpos, nunca ninguno ni nunca ambos (son disjuntos).

## `elif`

### Motivación

Es muy común que cuando una determinada condición no se cumple para un `if` determinado, queramos evaluar otra condición, pero solo en el caso en el que la primera no se haya cumplido. Un ejemplo de esto puede ser el anterior sobre infusiones:
- Necesito evaluar si tengo todos los insumos para preparar el té antes de prepararlo.
- En el caso en el que no tenga insumos para preparar el té, evaluaré si cuento con los insumos para prearar el café, pero solamente si no contaba con los insumos para preparar té, ya que en ese caso hubiera directamente preparado el té y listo.

De alguna manera, esto se representa mediante la siguiente estructura:

```python
if <TENGO INSUMOS PARA TE>:
    <PREPARO TE>
else:
    if <TENGO INSUMOS PARA CAFE>:
        <PREPARO CAFE>
```

Cuando tengo muchos de estos grupos de decisiones donde voy a evaluar una condición solamente si las anteriores no se cumplen, rápidamente termino con una estructura como la siguiente:

```python
if <CONDICION 1>:
    <CUERPO 1>
else:
    if <CONDICION 2>:
        <CUERPO 2>
    else:
        if <CONDICION 3>:
            <CUERPO 3>
        else:
            ...
            ...
            ...
                if <CONDICION N>:
                    <CUERPO N>
                else:   # Si las condiciones 1 a N fallaron
                    <CUERPO ELSE>
```

Este código es muy difícil de leer y de mantener cuando se agregan muchos condicionales ([_Spaghetti Code_](https://en.wikipedia.org/wiki/Spaghetti_code)).

### Sintaxis

`elif` es una combinación entre `else` y un posterior `if` dentro del cuerpo de ese `else`, **sin que haya ninguna línea de código extra entre el `else` y el `if` anidado que está adentro**. De esta forma, en la mayoría de los casos, las estructuras con la siguiente forma:

```python
if <CONDICION 1>:
    <CUERPO 1>
else:
    if <CONDICION 2>:
        <CUERPO 2>
```

pueden transformarse a:

```python
if <CONDICION 1>:
    <CUERPO 1>
elif <CONDICION 2>:
    <CUERPO 2>
```

### Funcionamiento

En las cadenas como la primera, se tienen distintos "juegos" de condicionales: cada `if` se asocia con su `else` de abajo y nada más.

En las cadenas como la segunda, tanto el `if` del principio, como todos los `elif` que pueda haber en el medio, como el `else` final funcionan todos como una sola cadena de condicionales (sus condiciones quedan ligadas entre ellas), de la siguiente forma:

Imaginemos la siguiente estructura:

```python
if <CONDICION IF>:
    <CUERPO IF>
elif <CONDICION ELIF 1>:
    <CUERPO ELIF 1>
elif <CONDICION ELIF 2>:
    <CUERPO ELIF 2>
elif <CONDICION ELIF 3>:
    <CUERPO ELIF 3>
...
elif <CONDICION ELIF N>:
    <CUERPO ELIF N>
else:
    <CUERPO ELSE>
```

- Si la condición del `if` es verdadera:
    - Se ejecuta el `<CUERPO IF>`.
    - Se ignoran todas las condiciones posteriores (las de los `elif`).
    - Se ignoran los `<CUERPOS ELIF *>` (todos los cuerpos de los `elif`).
    - Se ignora el `<CUERPO ELSE>`.

- Si la condición del `if` es falsa:
    - Se evalúan **en orden** las condiciones de los `elif`.
    - Cuando la condición de un `elif` es falsa, su cuerpo se ignora, y se procede a evaluar la condición del siguiente `elif`.
    - Cuando la condición de un `elif` es verdadera, su cuerpo se ejecuta, y se ignoran la condiciones y cuerpos de todos los siguientes `elif` y del `else`.

- Si la condición del `if` y de todos los `elif` son falsas, recién entonces se ejecuta el `<CUERPO ELSE>`.

### Ejemplo

De esta forma, el planteo original para las infusiones:

- `?` Si tengo agua caliente:
    - `?` Si tengo saquitos de té:
        - `>` Preparo té.
    - `?` En caso contrario, y si tengo café molido y filtros:
        - `>` Preparo café.
    - `?` En caso contrario, y si tengo yerba:
        - `>` Preparo mate.
    - `?` En caso contrario (si no tengo nada de todo eso):
        - `>` No preparo nada.

- `?` En caso contrario (no tengo agua caliente):
    - `>` No preparo nada.

se traduce a código como:

```python
if <tengo agua caliente>:
    if <Si tengo saquitos de té>:
        <Preparo té>
    elif <Si tengo café molido y filtros>:
        <Preparo café>
    elif <Si tengo yerba>:
        <Preparo mate>
    else:
        <No preparo nada>
else:           # else del if del principio
    <No preparo nada>
```
