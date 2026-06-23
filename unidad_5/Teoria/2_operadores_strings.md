# Operadores de strings

Es importante recordar que el efecto que tiene cada operador depende del tipo de dato de sus operandos (de las variables y/o datos inmediatos a los que se aplique). Por ejemplo, el operador `+` aplica la suma usual cuando está aplicado a operandos de tipos numéricos (como `int` o `float`).

Al igual que cualquier otro objeto en Python, los distintos operadores tienen diferentes efectos al aplicarse a los strings (tipo `str`).

A continuación se enumeran los operadores que se utilizan en Informática General UCA.

## Longitud de un string (`len`)

Como toda secuencia, los strings tienen una longitud dada por la cantidad de caracteres (ya sean letras, digitos u otros simbolos) que tienen dentro. La función `len()` de Python, aplicada a un string, devuelve dicha longitud. Se define que la longitud del string vacío es cero.

### Ejemplos

```python
print(len(""))          # Imprime 0
print(len(" "))         # Imprime 1 (el espacio es un caracter mas)
print(len("Hola"))      # Imprime 4
print(len("Python"))    # Imprime 6
print(len("\n"))        # Imprime 1 (no 2, porque la \ funciona como
                        # caracter de escapado, \n es un enter)
```

## Operador de concatenación (`+`)

* El operador de concatenación es el símbolo `+`. 
* Se utiliza para unir (concatenar) dos strings. 
* Ambos operandos deben ser de tipo `str`. 
* Los strings son concatenados en orden (primero el de la izquierda, luego el de la derecha).

**El resultado es un nuevo string, y los strings originales no se modifican**. Esto se debe a que los objetos de tipo `str` de Python son **inmutables**, es decir, **no pueden ser modificados una vez creados**.

### Ejemplos

```python
x = "Hola"
print(x + "Mundo")  # Imprime "HolaMundo"

# El string vacio "" es el elemento neutro de la operacion de
# concatenacion. Concatenar con un string vacio resulta en el
# mismo string
print("" + "Hola")  # Imprime "Hola"
print("Hola" + "")  # Idem anterior
print("" + x + "")  # Idem anterior (x = "Hola")

# TypeError: solo se puede concatenar string con string, no otro tipo de dato
# TypeError: can only concatenate str (not "int") to str
print("Mi numero de la suerte es: " + 9)

# Para concatenar un objeto que no sea de tipo str con un
# string, hay que convertir a string dicho objeto
# Imprime "Mi numero de la suerte es: 9"
# (str convierte el número a string para ser concatenado)                   
print("Mi numero de la suerte es: " + str(9))
```

## Operador de repetición (`*`)

* El operador de repetición es el símbolo `*`.
* Se utiliza para repetir un string un número determinado de veces. 
* Los operandos deben ser uno de tipo `str` y otro de tipo `int`.
* El orden de los operandos es indistinto y no altera el resultado (da igual si el número está a la izquierda y el string a la derecha o viceversa).

**El resultado es un nuevo string, y los strings originales no se modifican**. Esto se debe a que los objetos de tipo `str` de Python son **inmutables**, es decir, **no pueden ser modificados una vez creados**.

### Ejemplos

```python
print("Hola" * 3)   # Imprime "HolaHolaHola"
print(3 * "Hola")   # Imprime "HolaHolaHola"

y = "Buen Dia"
print(y * 2)        # "Buen DiaBuen Dia"

z = "Adios"
print(5 * z)        # "AdiosAdiosAdiosAdiosAdios"

# Multiplicar por cero o por un negativo da como resultado un string vacio
print(z * 0)
print(z * -4)

# No se puede multiplicar un string (ni cualquier secuencia) por un numero
# fraccionario
# TypeError: can't multiply sequence by non-int of type 'float'
print('Hola' * 3.14)
```
## Ejemplo de uso en un ejercicio

Como buen ejemplo de uso de estos operadores, se recomienda repasar el [ejercicio 6 de la guía 2](https://github.com/jcausse/clases_uca_ig/blob/main/unidad_2/ej06.py), que hace uso de estos dos últimos operadores para suplir la imposibilidad de usar condicionales (que son tema de la guía 3).

## Operadores con asignación (`+=` y `*=`)

Vale recordar la gran utilidad de los operadores "concatenación y asignación" y "repetición y asignación", que son muy usados en los ejercicios.

* El operador `+=` recibe una variable que contenga un `str` del lado izquierdo y otro `str` del lado derecho. Se concatenará el string derecho al final del izquierdo, y se asignará el resultado en la misma variable que está del lado izquierdo, **reemplazando su valor actual** (el mismo no podrá ser recuperado).

* El operador `*=` recibe una variable que contenga un `str` del lado izquierdo y un `int` del lado derecho. Se repetirpa el string izquierdo la cantidad de veces que indique el número del lado derecho, y se asignará el resultado en la misma variable que está del lado izquierdo, **reemplazando su valor actual** (el mismo no podrá ser recuperado). Es importante notar que **en este caso, si el número es una constante y no está dentro de una variable, el orden de los operandos sí importa** (no se puede realizar una asignación a una constante).

### Ejemplos

```python
x = "hola"
x += "chau" # Equivale a x = x + 'chau'
print(x)    # Imprime "holachau"

y = "python"
y *= 2      # Equivale a y = y * 2
print(y)    # Imprime "pythonpython"
```

## Igualdad y desigualdad de strings

Los operadores de comparación `==` y `!=` nos pueden informar si dos strings son iguales o distintos, respectivamente. Estos operadores, al igual que en cualquier otro de sus usos, devuelven un resultado de tipo `bool` (`True` o `False`).

> **Importante** : Dos strings son iguales si ambos tienen la misma longitud (la misma `len`), y son iguales caracter a caracter (**distinguiendo entre mayúsculas y minúsculas**).

### Ejemplos

```python
print('hola' == 'chau')             # False
print('' != ' ')                    # True (vacio y espacio)
print('python' == 'python')         # True
print('python' == 'Python')         # False
print('python' != 'Python')         # True
print(not('python' == 'Python'))    # False
```

## Comparación de orden de strings

Los operadores `<`, `<=`, `>` y `>=` comparan los strings de manera que un string es menor que otro cuando:

* Ambos coinciden, pero uno es más corto, y entonces el más corto es menor. 

  Por ejemplo: `'mate' < 'mates'`

* Ambos difieren en algún caracter, y entonces será menor aquel que tenga el caracter con el menor código ASCII (dado por la [tabla ASCII](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/800px-ASCII-Table-wide.svg.png?20221024154539)) en la primera vez que difieran. 

  Por ejemplo:
    * `'buenos+dias' < 'buenos,dias'` pues el símbolo `+ está antes que la `,`.
    * `'Saludos' < 'saludos'` pues la `S` mayúscula está antes que la `s` minúscula.
    * `'arte' < 'veloz'` pues la `a` minúscula está antes que la `v` minúscula.


> **Muy importante**: Recordar que las mayúsculas siempre vienen antes que las minúsculas en la tabla ASCII. Por esto, si en algún ejercicio se pide ordenar de forma alfabética dos strings es necesario que los mismos estén o ambos en mayúsculas, o ambos en minúsculas para poder compararlos sin que haya errores debido a la diferencia en la codificación. Se dice en este caso que la comparación es _case insensitive_.

### Utilidad
Cuando los strings están únicamente formados por letras, y son siempre todas mayúsculas o todas minúsculas, estos operadores comparan strings de forma alfabética **ascendente**. De esta forma, y usando ciclos, se resuelve el problema de ordenar palabras en orden alfabético (muy común en segundos parciales y exámenes finales).
