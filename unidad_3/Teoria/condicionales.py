### Condicionales ###

# Los condicionales son estructuras que nos permiten tomar decisiones, ejecutando (o no) codigo ante el resultado de:
# * Una comparacion
# * Una operacion matematica
# * Una llamada a funcion
# * etc.
# Incluso, nos permiten ejecutar distintas porciones de codigo dependiendo de un valor, encadenando condiciones.

### if ###
"""
if <CONDICION>:
    <CUERPO>
"""

# La base de los condicionales es el if, que es una estructura que tiene una <CONDICION> y un <CUERPO>, y ejecuta
# el codigo contenido en su <CUERPO> en caso de que la <CONDICION> se evalue como Verdadera (True)

#############################################################################
# Ejemplo:
"""
x = 16
if x % 2 == 0:
    print(x, 'es par')
"""

# En este ejemplo, la condicion x % 2 == 0 puede devolver dos valores posibles:
# * True, si el resultado de la operacion x % 2 es cero.
# * False, si el resultado de x % 2 es algun valor que NO sea cero.

# Como x es 16, que es divisible por 2, el resto de dividir 16 / 2 sera 0, por lo que
# x % 2 es cero, y la condicion se evalua como True. Si x fuese 17, por ejemplo,
# 17 % 2 es uno (distinto de cero), por lo que la condicion evalua como False.
#############################################################################

### else ###
"""
if <CONDICION>:
    <CUERPO_IF>
else:
    <CUERPO_ELSE>
"""

# El else no tiene ninguna condicion asociada. Ejecuta el codigo que contiene en su cuerpo (CUERPO_ELSE) si la
# CONDICION del if previo fue evaluada como False (y, por lo tanto, CUERPO_IF no se ejecuto).
# Si la CONDICION del if previo es evaluada como True, se ejecuta CUERPO_IF (por lo que vimos antes), y NO se
# ejecuta CUERPO_ELSE.

# * El else siempre es OPCIONAL, no asi su if previo (no puede haber un else sin un if previo)

#############################################################################
# Ejemplo: "Anda al kiosco. Si hay Coca-Cola, compra una. Sino, compra una Pepsi".
"""
if hay_coca_cola():
    comprar_coca_cola()
else:
    comprar_pepsi()
"""
#############################################################################
# Ejemplo: Siguiendo el ejemplo de los numeros pares, antes se imprimia 'x es par' si el numero era par, pero nada
# si era impar
"""
x = 21

if x % 2 == 0:
    print(x, 'es par')
else:
    print(x, 'es impar')
"""
#############################################################################

### elif ###
"""
if <CONDICION_IF>:
    <CUERPO_IF>
elif <CONDICION_ELIF_1>:
    <CUERPO_ELIF_1>
elif <CONDICION_ELIF_2>:
    <CUERPO_ELIF_2>
elif <CONDICION_ELIF_3>:
    <CUERPO_ELIF_3>
elif <CONDICION_ELIF_4>:
    <CUERPO_ELIF_4>
.
.
.
else:
    <CUERPO_ELSE>
"""

# El elif es un intermedio entre un if y un else. Son opcionales, pero dependen de:
# * el if previo (obligatorio)
# * los elif que vengan antes que uno determinado en la cadena (si se tiene, por ejemplo, un if, 3 elif, y un else,
#   el primer elif depende solo del if; el segundo elif depende del if y del primer elif, y el tercer elif depende
#   de el if y de los dos elifs anteriores. El esle depende de el if y de todos los elif)

# Los elif se recorren en el orden en que aparecen. Si la condicion del if o de alguno de sus elifs da verdadera,
# se ejecuta el cuerpo de la estructura cuya condicion haya dado verdadera, y las condiciones de las estructuras que
# siguen no son evaluadas, ni sus cuerpos ejecutados (incluido el else, cuyo cuerpo tampoco se ejecuta).

#############################################################################
# Ejemplo: "Anda al kiosco. Si hay Coca-Cola, compra una. Sino, compra una Pepsi. Si tampoco
# hay pepsi, compra una Levite. Si no hay Levite, compra una soda. Si no hay, no compres nada.".
"""
if hay_coca_cola():
    comprar_coca_cola()
elif hay_pepsi():
    comprar_pepsi()
elif hay_levite():
    comprar_levite()
elif hay_soda():
    comprar_soda()
else:
    irse_sin_comprar()
"""
#############################################################################
# Ejemplo: clasificar un numero
"""
x = 35

if x < 10:                                  # False
    print(x, 'es menor que 10')             # No se ejecuta
elif x < 20:                                # False
    print(x, 'esta entre 10 y 19')          # No se ejecuta
elif x < 30:                                # False
    print(x, 'esta entre 20 y 29')          # No se ejecuta
elif x < 40:                                # True
    print(x, 'esta entre 30 y 39')          # Se ejecuta        ------------
elif x < 50:                                # No se evalua
    print(x, 'esta entre 40 y 49')          # No se ejecuta
else:
    print(x, 'es mayor que 50')             # No se ejecuta
"""
#############################################################################
