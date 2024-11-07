##############
### SLICES ###
##############

### Usos de los slices ###
# Los slices se utilizan para obtener una partición de distintos elementos que puedan iterarse, por ejemplo:
# * Listas
# * Strings
# * Tuplas

### Componentes de un slice ###
# Un slice se compone de: [inicio:fin:paso]
# * inicio: Es el índice de inicio de la partición. Todos los elementos desde este índice en adelante son tomados
#           al momento de generar la partición. El inicio puede omitirse (siempre poniendo los dos puntos, pero
#           ignorando el número que va en ese lugar), en cuyo caso se asume que es 0.
# * fin: Es el índice de fin de la partición. Indica el elemento hasta el cual llegará la partición. Es importante
#        tener en cuenta que el elemento final no es incluído en la partición (llega hasta el elemento anterior).
#        El final también puede omitirse, en cuyo caso se asume que es el último elemento del iterable. Al igual que
#        en el inicio, se agregan los dos puntos, pero no se pone el número que va en el lugar del fin.
# * paso: Es el salto que se da entre los índices de inicio y fin. También puede omitirse. En este caso, no es necesario
#        poner los dos puntos, y se asume que el paso es 1 si el mismo se omite.

###################################################################################################################################
# Los slices no generan excepciones por índices fuera de rango. Simplemente no incluyen a los elementos o generan strings vacíos. #
###################################################################################################################################

### Indices negativos ###
# Para todos estos casos, Python permite utilizar índices negativos, que cuentan desde el final del iterable. Como el índice
# 0 denota el primer elemento, de izquierda a derecha (y como un índice -0 no tendría sentido), los índices negativos
# van desde el -1 (hacia atrás, hacia más negativos). Entonces, por ejemplo, el índice -1 denota el último elemento, el
# índice -2 denota el penúltimo (anteúltimo), el -3 denota el antepenúltimo, y así sucesivamente.
#
# Para convertir un índice negativo a uno positivo, se puede usar la función len(), que devuelve la cantidad de
# elementos del iterable, y sumarle (que termina restando, ya que sumar un número negativo es, matemáticamente, como hacer
# una resta) el índice negativo deseado. Por ejemplo, para convertir el índice -3 a uno positivo, se puede usar len(string) - 3.
#
# Cuando utilizamos un step (paso) negativo, el slice recorre del final al principio (de derecha a izquierda).

### Ejemplos ###

#         0123456789
string = "Hola Mundo"
# len(string) = 10

print("Ejemplos usando todo:")
print(string[0:7])      # "Hola Mu"
print(string[0:8:2])    # "Hl u"
print(string[0:9:2])    # "Hl ud"
print(string[5:5])      # "" (desde 5, hasta 5, sin incluir el 5)
print(string[5:2])      # "" (inicio mayor que fin, no incluye nada)
print("--------------------------------------\n")

print("Ejemplos omitiendo inicio:")
print(string[:7])      # "Hola Mu"
print(string[:8:2])    # "Hl u"
print(string[:9:2])    # "Hl ud"
print("--------------------------------------\n")

print("Ejemplos omitiendo fin:")
print(string[6:])             # "undo"
print(string[6:len(string)])  # "undo" (es equivalente al ejemplo anterior)
print(string[2::3])
print(string[2::2])
print("--------------------------------------\n")

print("Ejemplos usando índices negativos:")
print(string[-1])    # No es un slice, sino que simplemente accede al último elemento
print(string[-7])    # "a"
print(string[-7:])   # Denota (del -7, que es la "a", como vimos), hasta el final. Imprime "a Mundo".
print(string[-2:])   # Denota (del -2, que es la "d", como vimos), hasta el final. Imprime "do".
print(string[-7:-2]) # "a Mun" (recordar que no incluye el último elemento)
print("--------------------------------------\n")

print("Ejemplos usando step negativo:")
print(string[::-1])     # "odnuM aloH" (imprime el string al revés)
print(string[::-2])     # "onMao" (imprime el string al revés, saltando de a 2)
print(string[-2:-8:-1]) # "dnuM a"
print(string[3:-4:-1])  # "" (inicio menor que fin, pero se está recorriendo en sentido inverso, no incluye nada)
print(string[-4:3:-1], ".", sep="")  # "uM ."
print(string[-5:2:-1])  # "M a"
print("--------------------------------------")
