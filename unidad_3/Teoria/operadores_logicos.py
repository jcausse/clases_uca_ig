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
