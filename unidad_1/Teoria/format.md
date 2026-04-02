# Formato de Strings

## Motivación

La función `print` permite recibir múltiples parámetros. Cada parámetro, como en cualquier función se separa mediante comas `,` de los demás. Estos parámetros pueden ser tanto cadenas de texto (`str`) dadas de manera inmediata (literales), como también variables, de las cuales se consulta e imprime su valor.

```python
x = 3
verdad = False
y = 3.14
texto = 'Buen dia'

print('Hola', texto, 'x =', x, 'y =', y, verdad)
```

Este código imprime `Hola Buen dia x = 3 y = 3.14 False`.

Además, la función `print`:
- Deja un espacio entre parámetro y parámetro (se puede sobreescribir el valor usando `sep=`).
- Inserta un salto de línea automático al final (se puede sobreescribir el valor usando `end=`).

Por ejemplo:

```python
x = 3
texto = 'Python'

print('Hola', texto, '=', x, sep='%', end='***')
```

Este código imprime `Hola%Python%=%3***` sin un salto de línea al final.

Ahora bien, si se considera el siguiente ejemplo:

```python
x = 10/3        # 3.333333...
y = 4
z = 935

print('y =', y)
print('z =', z)
```

- ¿Cómo puedo hacer para que se imprima una cantidad determiada de decimales al imprimir `x`?
- Dado que `y` y `z` tienen una cantidad distinta de dígitos, ¿cómo puedo hacer para que al imprimirse por pantalla ocupen una cantidad definida de lugares para que en lugar de la salida verse así:
    ```
    y = 4
    z = 935
    ```
    se vea así:
    ```
    y =   4
    z = 935
    ```
    ?
- Al pasarle a `print` varios parámetros, a veces necesitamos que el separador de parámetros (predeterminadamente, un espacio) se imprima, y a veces no. ¿Cómo puedo indicarle cuándo imprimirlo y cuándo no?

**La motivación del formateo surge de que, de forma predeterminada, `print` no es lo suficientemente "potente" como para cumplir con todos estos casos de uso.**

## Método `.format()`

`format()` es un método de la clase `str` que permite generar una cadena de texto específica a partir de texto literal, y de la interpolación de valores de variables (poner los valores de las variables dentro del texto).

Todo el texto escrito en el `str` original que da el formato aparece de manera literal.

Los caracteres que permiten la interpolación de valores son las llaves `{}`. Por cada par de llaves presente en la cadena original, se debe pasar a `format` un parámetro. `format` se encargará de reemplazar cada par de llaves por el valor del parámetro recibido, **en orden**.

### Ejemplo

```python
nombre = 'Pepe'
numero = 9

mi_str = 'Soy {} y mi numero es {}'.format(nombre, numero)
```

La cadena de texto construida en este caso es `Soy Pepe y mi numero es 9`.

Notar que:
- `format()` es propio de la clase `str` y no tiene absolutamente nada que ver con `print()`. Se puede construir una cadena de la forma en que lo hicimos en el ejemplo sin la necesidad que dicha cadena esté dentro de un `print()`.
- Al no estar dentro de un `print()`, no tienen efecto `sep=` y `end=`, ya que no los hay (pues son parte de `print()` y no de los `str`). 
- **Las cadenas de texto (`str`) son INMUTABLES** (una vez creadas, no pueden cambiar). Como consecuencia, una vez armada la cadena, la misma **no cambia en caso de que cambien los valores de las variables utilizadas en el `format()`**.

### Ejemplo

Si a continuación del ejemplo anterior se agrega:

```python
numero = 11     # Cambio posterior a la construccion del str

print(mi_str)   # print() sobre un str construido antes
                # Imprime el str construido
                # No imprime separadores (hay 1 solo parametro)
                # Imprime salto de linea al final 
                # (es el end= predeterminado).
```

Imprime `Soy Pepe y mi numero es 9`, que es la cadena inicialmente generada.

## Especificadores de formato

Al interpolar variables, se pueden utilizar ciertos _format specifiers_ para indicar a Python cómo tiene que imprimir los valores de esas variables.

Ejmplos comunes:
- Imprimir una cadena de texto utilizando una cantidad fija de espacios (llenando con espacios en blanco).
- Justificar un texto a la izquierda.
- Centrar un texto.
- Imprimir un número entero utilizando una cantidad fija de dígitos, y colocando ceros a la izquierda para llenar dicha cantidad (ejemplo: imprimir `23` con cinco dígitos y llenando con ceros resulta en `00023`).
- Imprimir un número fraccionario (un `float`) con una cantidad determinada de decimales.

Los especificadores de formato se indican dentro de las llaves `{}` en la cadena de formato y comienzan con `:`. La sintaxis es:

```
{:ESPECIFICADOR}
```

Estos especificadores no se imprimen de manera literal (porque están dentro de las llaves), sino que son interpretados por `format()` a la hora de generar la cadena final.

Los especificadores suelen ser combinables.

## Ejemplos prácticos

Ver el archivo [format.py](https://github.com/jcausse/clases_uca_ig/tree/main/unidad_1/Teoria/format.py).

## Links útiles

https://pyformat.info/ (usar siempre la notación `new`)
https://www.w3schools.com/python/ref_string_format.asp
