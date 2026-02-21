# Archivos

Los archivos son conjuntos de datos estructurados que se guardan en memoria en la computadora, que pueden trascender la ejecución de un programa. Esto nos permite, por ejemplo, guardar datos que surgen de la ejecución de un programa en un momento determinado, para luego volver a utilizarlos.

Por ejemplo, cuando escribimos un documento de Word para hacer un TP, podemos guardar nuestro progreso hasta el momento para poder retomarlo luego. Word utiliza unos archivos terminados en `.docx` para guardar nuestro trabajo y poder retomarlo luego.

Cada programa define su propia forma de guardar sus datos. En el ejemplo de Word, un archivo `.docx` tiene una estructura particular para guardar los datos, de forma tal que pueda guardar el texto escrito, la fuente utilizada, el tamaño, si hay negritas, colores, imágenes, etc.

La forma en la que un programa guarda sus datos en archivos (i.e. el formato de los mismos) es propia de cada programa, y no se regula como cada programa guarda los datos, ya que es muy propio del programa en cuestión: cada programa crea sus archivos de datos en una forma que está pensada para ser leída con **ese** programa.

La terminación `.docx` (que en este caso corresponde a un archivo de Word) se la denomina **extensión del archivo**, y no es realmente necesaria para que un archivo esté bien definido (incluso, se pueden crear archivos sin extensión). Las extensiones son principalmente una forma de que el Sistema Operativo (Windows, Mac, etc.) sepa qué tiene que hacer con ese archivo.

# Archivos de texto plano

Los archivos `.docx`, al igual que muchos otros tipos de archivos, contienen dentro información contextual para el programa, e información de formato para sus datos. En el caso de Word, los archivos no contienen únicamente el texto que escribimos, sino que también contienen información sobre la fuente, tamaños de letra, etc.

Los archivos de texto plano, cuya extensión es normalmente `.txt`, son archivos en los que solamente aparece texto. 

Estos archivos son muy utilizados para programar: los archivos de los distintos lenguajes de programación suelen ser archivos de texto plano, pero con una extensión propia que indique en qué están programados. Ejemplos:

* `.py` Indica que es código en Python.
* `.c` en C.
* `.cpp` en C++.
* `.rb` en Ruby.
* `.java` en Java.
* Y muchos otros más.

# Archivos CSV

Los archivos de _Comma Separated Values_ (CSV) son archivos de **texto plano** que permiten representar información en un formato similar a una tabla simple. De hecho, Windows intentará abrir un archivo CSV, de forma predeterminada, con Excel.

Por ejemplo, la siguiente tabla:

| Nombre | Apellido | Carrera     | Promedio |
|--------|----------|-------------|----------|
| Juan   | Causse   | Informática | 10       |
| Pedro  | Gonzalez | Industrial  | 10       |

Se representaria de la siguiente forma:

```csv
Nombre,Apellido,Carrera,Promedio
Juan,Causse,Informática,10
Pedro,Gonzalez,Industrial,10
```

* Cada fila de la tabla es una línea.
* Cada valor (las diferentes columnas) en una fila están separados por comas.
* El archivo CSV suele incluir como primera fila (primera línea) el **encabezado** de la tabla, que indica qué contiene cada fila.

# Uso de archivos de texto plano en Python

Python puede leer cualquier archivo, en principio (a menos que indiquemos lo contrario) como texto plano. Nos permite abrir un archivo, leer de el o escribirlo, y cerrarlo.

## Abrir archivos

Para abrir archivos, usamos la función `open()`. Se usa de la siguiente forma:

```python
<variable> = open(<nombre_archivo>, <modo>)
```

Donde: 
* `<variable>` es el nombre de una variable que vamos a usar para acceder al archivo. **Suele llamársela _handle_ del archivo**.
* `<nombre_archivo>` es el nombre del archivo que vamos a abrir.
* `<modo>` indica qué operación vamos a querer realizar con el archivo. Esto es importante porque Python necesita saber para qué va a abrir el archivo de antemano, ya que es información que se la pide el Sistema Operativo. El modo es alguno de los siguientes (hay más, pero no los vemos):
  * `'r'` (read): Abrir el archivo para lectura. Si el archivo no existe, `open()` lanzará un excepción `FileNotFoundError`.
  * `'w'` (write): Abrir el archivo para escritura. Si archivo no exsite, lo crea. Si el archivo existe, lo sobreescribe, es decir, descarta todo el contenido que pudiera tener, y lo abre para escritura como si de un archivo nuevo se tratase.
  * `'a'` (append): Abre el archivo para escritura y coloca el cursor interno al final del mismo. Esto permite agregar información al final del archivo sin perder la ya existente. Si el archivo no existe, lo crea.

### Ejemplo:
```python
file = open('myfile.txt', 'w')
```
Abre el archivo `myfile.txt` en modo de escritura (`'w'`), y crea la variable `file` que nos permite manipular el archivo.

## Cerrar un archivo

Para cerrar un archivo, lo hacemos mediante:
```python
<variable>.close()
```

### Ejemplo:

Usando el archivo del ejemplo anterior:
```python
file.close()
```

## Uso de archivos con with

> **IMPORTANTE**: En Informática General UCA, el uso de `with` no se dicta en clase, y por tanto no está permitido. Esta sección es solo informativa.

El `with` es una estructura de Python que nos permite liberar recursos pedidos de forma automática cuando el bloque de código que contiene termina.

Esto se suele utilizar mucho con archivos ya que permite que el archivo se cierre de forma automática sin nosotros tener que hacer `<variable>.close()` de manera manual.

La sintaxis para utilizar archivos con `with` es la siguiente:

```python
with open(<nombre_archivo>, <modo>) as <variable>:
    <CODIGO DEL WITH>
    <CODIGO DEL WITH>
    <CODIGO DEL WITH>

<OTRO CODIGO, FUERA DEL WITH>
```

Python:
* Abre el archivo cuando encuentra el `with`.
* Ejecuta todo el código de dentro del con el archivo abierto. En este punto podemos manipular el archivo, leyendo o escribiendo el mismo.
* Cuando termina `<CODIGO DEL WITH>` cierra el archivo de forma automática, sin que lo tengamos que especificar.
* Sigue ejecutando el código que viene debajo, `<OTRO CODIGO, FUERA DEL WITH>`.

**IMPORTANTE:** Todo intento de utilizar el archivo desde fuera del `with` dará un error, pues el archivo ya se cerró. En caso de que necesitemos hacer otra operación con el mismo archivo, debemos abrirlo nuevamente (ya sea usando `with`, que es lo que se recomienda, o de la forma tradicional con `open()` y `close()`).

## Escribir archivos

Para escribir un archivo, ya abierto y con su _handle_ (variable con la cual usamos el archivo) guardado en `<variable>`, usamos el método `write`, de la siguiente forma:

```python
<variable>.write(<contenido>)
```

Donde `<contenido>` **debe ser un string**, que se va a escribir **tal cual** en el archivo. "Tal cual" indica que, a diferencia de `print()`, `write()` **NO introduce saltos de línea al terminar de escribir el contenido**.

Se recomienda el uso de _f-strings_ para insertar valores contenidos en variables (que pueden ser strings o de tipo numérico, como `int` o `float`) en el texto.

### Ejemplo de uso

```python
# Escribir mi nombre, mi apellido, y mi facultad en 3 lineas
# distinas en un archivo.

with open('mi_archivo.txt', 'w') as file:
    file.write('Juan Ignacio\n')
    file.write('Causse\n')
    file.write('ITBA\n')

# NOTA: \n es un salto de linea. Esto permite que el 
# siguiente texto que se escribe quede abajo.
```

### Importante

Tener en cuenta también que `write()` permite un solo parámetro, que debe ser de tipo string. Por lo tanto, los siguientes dos bloques de código muestran usos correctos de `print()` que no funcionan con `write()`.

```python
x = 2
print('El valor de x es: ', x)          # OK
file.write('El valor de x es: ', x)     # No funciona
```

Ocurre este error: `TypeError: TextIOWrapper.write() takes exactly one argument (2 given)`.

```python
x = 2
print(x)            # OK
file.write(x)       # No funciona
```

Ocurre este error: `TypeError: write() argument must be str, not int`.

## Leer archivos

Para leer un archivo, ya abierto y con su _handle_ (variable con la cual usamos el archivo) guardado en `<variable>`, usamos los siguientes métodos:

* `read()`: Lee el contenido de un archivo por completo, y lo guarda en una variable de tipo string.
* `readline()`: Lee la siguiente línea de un archivo hasta que la misma termina (se considera que la línea termina al encontrar un `\n`), y la devuelve en un string.
* `readlines()`: Lee todas las líneas de un archivo (es decir, lee el archivo completo), y devuelve una lista de strings, donde cada string es una linea por separado.

**IMPORTANTE:** Los strings que devuelven estas funciones tienen como caracter final el salto de línea (`\n`), si lo hubiera (la última línea, donde termina el archivo, podría no tenerlo).

**IMPORTANTE:** Si el archivo contiene valores numéricos, es responsabilidad de quien programa realizar las conversiones de tipo de dato y las validaciones que sean pertinentes. Incluso si Python lee un número dentro del archivo, el contenido lo devuelve como string.

### Ejemplo

Supongamos que tenemos el siguiente archivo, llamado `mi_archivo.txt`:

```
hola
esta es una prueba
buenos dias
123
25.75
```

Notar que todas las líneas incluyen un salto de línea, excepto la última (pues no hay línea vacía al final).

Abriendo el archivo con `with open('mi_archivo.txt', 'r') as file:`, se muestra el resultado de las siguientes operaciones:

`read()`:

```python
>>> with open('mi_archivo.txt', 'r') as file:
...     cont = file.read()
...
>>> cont
'hola\nesta es una prueba\nbuenos dias\n123\n25.75'
```

`readline()`:

```python
>>> with open('mi_archivo.txt', 'r') as file:
...     cont = file.readline()
...
>>> cont
'hola\n'
```

**IMPORTANTE:** Notar que cada invocación a `readline()` devuelve la siguiente línea a leer del archivo. Esto se manejar de forma automática, usando el cursor interno que tiene el mismo.

```python
>>> with open('mi_archivo.txt', 'r') as file:
...     cont1 = file.readline()
...     cont2 = file.readline()
...
>>> cont1
'hola\n'
>>> cont2
'esta es una prueba\n'
```

`readlines()`:

```python
>>> with open('mi_archivo.txt', 'r') as file:
...     cont = file.readlines()
...
>>> cont
['hola\n', 'esta es una prueba\n', 'buenos dias\n', '123\n', '25.75']
```

# Uso de archivos CSV plano en Python

**IMPORTANTE:** Leer primero la sección anterior y tenerla clara. Esta sección es simplemente una aplicación.

## Lectura de un CSV

Para leer un archivo CSV, conviene abrirlo de la misma forma que se mostró antes (se recomienda usar `with`), y luego de abierto el archivo se puede iterar el mismo por sus líneas de la siguiente forma:

```python
for line in file:
    <CODIGO>
```

Donde `line` es una variable donde Python guardará la línea leída (no necesita llamarse así, puede tener cualquier otro nombre), y `file` es el _handle_ del archivo.

El objetivo de esto es que, por cada iteración, `line` contenga la siguiente línea del archivo, y podamos operar con la misma.

### Ejemplo

Para el siguiente archivo, `empanadas.csv`, que contiene un pedido de empanadas de un grupo de amigos.

```csv
Juan,Carne Picante,2
Juan,Capresse,1
Pedro,Verdura,1
Pedro,Carne Suave,1
Maria,Roquefort,2
Camila,Pollo,1
```

El siguiente código:
```python
with open('empanadas.csv', 'r') as file:
    for line in file:
        print(line)
```

Imrpime:
```
Juan,Carne Picante,2

Juan,Capresse,1

Pedro,Verdura,1

Pedro,Carne Suave,1

Maria,Roquefort,2

Camila,Pollo,1

```

**IMPORTANTE**: Las líneas de separación vacías se deben a que cada línea del archivo termina en un `\n`. Este salto de línea lo podemos eliminar utilizando el método `strip()` de strings, que quita todo caracter en blanco que esté al principio o al final de un string.

## Obtención de datos de un CSV

Al leer e iterar un CSV, para procesarlo, necesitamos separar los campos de cada línea.

Partiendo de un código similar al del ejemplo anterior, nos quedará en `line` la próxima línea a leer cada vez. Siguiendo la recomendación anterior, conviene eliminar los saltos de línea y espacios vacíos usando `strip()`, y luego podremos separar las líneas según las comas (que son los separadores de un CSV) usando la función `split()`.

La función `split()` recibe como parámetro el caracter de separación a utilizar, y devuelve una lista de strings donde cada elemento de la lista es cada campo de la línea del CSV.

### Ejemplo

Para el archivo del ejemplo anterior, el siguiente código:

```python
with open('empanadas.csv', 'r') as file:
    for line in file:
        line_sep = line.strip().split(',')
        print(line_sep)
```

Imprime:

```
['Juan', 'Carne Picante', '2']
['Juan', 'Capresse', '1']
['Pedro', 'Verdura', '1']
['Pedro', 'Carne Suave', '1']
['Maria', 'Roquefort', '2']
['Camila', 'Pollo', '1']
```

## Procesamiento de un CSV

A la hora de ir leyendo un CSV, conviene procesarlo a medida que se leen las líneas, de forma que el contenido del archivo sea iterado una única vez. El procesamiento normalmente lo hacemos dentro del ciclo `for` descrito antes, o en funciones aparte que serán llamadas desde ese ciclo.

### Ejemplo

**IMPORTANTE:** Este ejemplo asume conocimientos sobre el uso de diccionarios.

Para el archivo del ejemplo anterior, si queremos determinar cuántas empanadas pidió cada uno, el código sería el siguiente:

```python
pedidos = {}    # Diccionario vacio para almacenar los pedidos

# Abro el archivo CSV
with open('empanadas.csv', 'r') as file:

    # Lo itero por lineas
    for line in file:

        # Elimino el \n final y separo la linea segun las comas
        line_sep = line.strip().split(',')

        # Obtengo los datos de interes
        nombre = line_sep[0]
        cant = int(line_sep[2])

        # Si anteriormente ya me encontre con un pedido de esta persona, ya va
        # a estar en el diccionario
        if nombre in pedidos:
            pedidos[nombre] += cant     # En este caso, sumo a la cantidad total

        # Si me encuentro por primera vez con esta persona, no va a estar en el
        # diccionario
        else:
            pedidos[nombre] = cant      # En este caso, agrego su primer pedido

print(pedidos)
```

Imprime:

```python
{'Juan': 3, 'Pedro': 2, 'Maria': 2, 'Camila': 1}
```
