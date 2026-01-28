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

| Operador | Nombre                 | Tipo                       |
| -------- | ---------------------  | -------------------------- |
| +        | Suma o concatenación   | Aritmético                 |
| -        | Resta                  | Aritmético                 |
| *        | Multiplicación         | Aritmético                 |
| **       | Potenciación           | Aritmético                 |
| /        | División exacta        | Aritmético                 |
| //       | División entera        | Aritmético                 |
| <<       | Shift izquierdo        | Bitwise (operador de bits) |
| >>       | Shift derecho          | Bitwise (operador de bits) |
| &        | AND bit a bit          | Bitwise (operador de bits) |
| \|       | OR bit a bit           | Bitwise (operador de bits) |
| ^        | XOR bit a bit          | Bitwise (operador de bits) |
| ~        | NOT bit a bit          | Bitwise (operador de bits) |
| <        | Menor                  | Comparación                |
| >        | Mayor                  | Comparación                |
| <=       | Menor o igual          | Comparación                |
| >=       | Mayor o igual          | Comparación                |
| ==       | Igual                  | Comparación                |
| !=       | Distinto               | Comparación                |
| and      | Conjunción             | Lógico                     |
| or       | Disyunción (inclusiva) | Lógico                     |
| not      | Negación               | Lógico                     |
