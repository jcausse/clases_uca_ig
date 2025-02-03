##########################
### Operadores logicos ###
##########################

# Los operadores logicos nos permiten realizar operaciones entre valores de verdad (booleanos), que
# en Python toman los valores True y False.
# Todos los operadores logicos operan con valores booleanos y devuelven valores booleanos.

# Podemos clasificarlos segun la cantidad de operandos que necesitan:
# * operadores unarios (un solo operando)
# * operadores binarios (dos operandos)

##################
### Operadores ###
##################

# Los operadores que Python trae por defecto son:

# OPERADOR      ARIDAD          SIGNIFICADO                         DESCRIPCION                                                 #
#-------------------------------------------------------------------------------------------------------------------------------#
# not           unario          Negacion de un valor de verdad      Invierte un valor de verdad (True -> False, False -> True)  #
# and           binario         Conjuncion logica                   El resultado es verdadero si ambos son verdaderos           #
# or            binario         Disyuncion logica                   El resultado es verdadero si al menos uno es verdadero      #

########################
### Tablas de verdad ###
########################

# A         not A    #
#--------------------#
# True      False    #
# False     True     #

# A         B           A and B     #
#-----------------------------------#
# False     False       False       #       <=== (1)
# False     True        False       #       <=== (2)
# True      False       False       #
# True      True        True        #

# A         B           A or B      #
#-----------------------------------#
# False     False       False       #
# False     True        True        #
# True      False       True        #       <=== (3)
# True      True        True        #       <=== (4)

#########################
### Operadores "Lazy" ###
#########################

# Los operadores "and" y "or" en Python, al igual que en otros lenguajes como C, por ejemplo, tienen un comportamiento que se suele
# notar como "Lazy" ("perezosos").
# Al usar estos operadores, los operandos se evaluan en orden (e.g. al hacer una operacion como A and B, A se evalua primero, y
# B despues). Si al evaluar el primer operando ya puede conocerse el resultado de la operacion logica, NO se evalua el segundo
# operando, y el resultado final queda determinado.

### AND Lazy ###

# Ver que en (1) A = False y B = False, en (2), A = False y B = True; y en ambos el resultado es siempre False.
# Si en una operacion AND el primer operando se evalua como False, el segundo NO SERA EVALUADO, pues, independientemente de su
# valor de verdad, el resultado sera, en ambos casos, False.

# Si en un AND el primer operando es False, el resultado no depende del segundo operando (por lo que no se evalua) y da False.
# Ahora bien, si el primer operando es True, el resultado dependera del segundo operando, por lo que debe evaluarse.

### OR Lazy ###

# Ver que en (3) A = True y B = False, en (4), A = True y B = True; y en ambos el resultado es siempre True.
# Si en una operacion OR el primer operando se evalua como True, el segundo NO SERA EVALUADO, pues, independientemente de su
# valor de verdad, el resultado sera, en ambos casos, True.

# Si en un OR el primer operando es True, el resultado no depende del segundo operando (por lo que no se evalua) y da True.
# Ahora bien, si el primer operando es False, el resultado dependera del segundo operando, por lo que debe evaluarse.

### Ejemplo ###

def falso():
    print('Funcion falso()')
    return False

def verdadero():
    print('Funcion verdadero()')
    return True

print('verdadero() and verdadero()')
resultado = verdadero() and verdadero()
### Imprime:
# Funcion verdadero()
# Funcion verdadero()
print(resultado)
### Imprime:
# True
print('--------------------')

print('verdadero() and falso()')
resultado = verdadero() and falso()
### Imprime:
# Funcion verdadero()
# Funcion falso()
print(resultado)
### Imprime:
# False
print('--------------------')

print('falso() and verdadero()')
resultado = falso() and verdadero()
### Imprime:
# Funcion falso()
print(resultado)
### Imprime:
# False
print('--------------------')

print('falso() or verdadero()')
resultado = falso() or verdadero()
### Imprime:
# Funcion falso()
# Funcion verdadero()
print(resultado)
### Imprime:
# True
print('--------------------')

print('falso() or falso()')
resultado = falso() or falso()
### Imprime:
# Funcion falso()
# Funcion falso()
print(resultado)
### Imprime:
# False
print('--------------------')

print('verdadero() or falso()')
resultado = verdadero() or falso()
### Imprime:
# Funcion verdadero()
print(resultado)
### Imprime:
# True
print('--------------------')

print('verdadero() or verdadero()')
resultado = verdadero() or verdadero()
### Imprime:
# Funcion verdadero()
print(resultado)
### Imprime:
# True
print('--------------------')

### Utilidad ###

# Supongamos que queremos determinar si un número a es divisible por otro número b.
# Si resultado de la operación a % b es cero, entonces a es divisible por b.
# Esto tiene un problema: si b es cero, a % b será a % 0, lo cual provocará un error.
"""
a = 9
print(a % 3)        # Imprime 0 (9 es divisible por 3)
print(a % 4)        # Imprime 1 (9 no es divisible por 4)
print(a % 0)        # No imprime nada, y da error: ZeroDivisionError: integer modulo by zero
"""

# Esto lo puedo solucionar de la siguiente manera:
# b != 0 and a % b == 0

# La primera condición (b != 0) sólo sera verdadera si b no es cero. En ese caso, como la primera condición es verdadera, esto no alcanza
# para determinar el resultado final de la and, por lo que la segunda condición (a % b == 0) debe evaluarse:
# * Supongamos que a es 9 y b es 3. En este caso, el resultado de a % b será cero. Luego, la comparación por igualdad (a % b == 0) equivale
#   a comparar (0 == 0) (pues el primer cero es el resultado de a % b). Esta comparación dará True, que es el resultado de la segunda condición
#   Finalmente:
#   * b != 0 es True
#   * a % b == 0 es True
#   * True and True es True, indicando que 9 es divisible por 3
# * Supongamos que a es 10 y b es 3. En este caso, el resultado de a % b será 1. Luego, la comparación por igualdad (a % b == 1) equivale
#   a comparar (1 == 0). Esta comparación dará False, que es el resultado de la segunda condición
#   Finalmente:
#   * b != 0 es True
#   * a % b == 0 es False
#   * True and False es False, indicando que 10 NO es divisible por 3

# En caso de que b fuera cero, la primera condición (b != 0) dará False (porque b es efectivamente 0). Debido a que el operador and es lazy,
# y a que la primera condición es falsa, el resultado de la and es falso, independientemente del resultado de la segunda condición (a % b == 0).
# Por esto, dicha segunda condición nunca se evalúa, evitando hacer la división por cero.

# Ver que es esencial que b != 0 sea la primera de las condiciones. Esto es porque necesitamos que se verifique primero que b no es cero para 
# solo hacer el módulo en ese caso. Si invertimos las condiciones, la expresión deja de funcionar correctamente.

a = 9
b = 3
print(b != 0 and a % b == 0) # True

a = 10
b = 3
print(b != 0 and a % b == 0) # False

a = 9
b = 0
print(b != 0 and a % b == 0) # False (sin dar ningún error)
"""
# NOTA: Las condiciones NO son intercambiables
print(a % b == 0 and b != 0) # Error: ZeroDivisionError: integer modulo by zero
"""

print('--------------------')

# Hecho función, podemos implementar esta condición en el siguiente programa:

def es_divisible(a, b):
    return b != 0 and a % b == 0    # Devolverá True o False, según se evalúe la condición como vimos antes

def main():
    a = int(input('Ingrese un número:   '))
    b = int(input('Ingrese otro número: '))
    if es_divisible(a, b):          # Si la función devuelve True, a es divisible por b
        print('{} es divisible por {}'.format(a, b))
    else:                           # En caso contrario, no lo es
        print('{} NO es divisible por {}'.format(a, b))

main()

# Notar que este programa soporta que b sea cero, sin dar errores:
"""
Ingrese un número:   5
Ingrese otro número: 0
5 NO es divisible por 0
"""

