#################################################
### Algoritmos útiles para / con diccionarios ###
#################################################

################################################
### 1. Encontrar la clave con el mayor valor ###
################################################

# Este algoritmo encuentra la clave que tiene asociado el mayor valor. Las claves pueden ser de cualquier tipo (recordar que las mismas
# deben ser únicas), y los valores pueden ser:
# * int o float (se aplicará la comparación numérica habitual).
# * strings (conviene que los mismos estén formados solo por letras mayúsculas o minúsculas -no ambas-, y se aplicará la comparación por tabla ASCII).

def max_dict(di):
    """
    Recibe un diccionario y devuelve una tupla con:
    [0] la clave para la cual se asocia el mayor valor.
    [1] dicho valor maximo.
    Si el diccionario esta vacio, retorna (None, None).
    """
    claves = list(di.keys())        # Obtengo todas las claves.
    ret = (None, None)              # Inicializo el valor de retorno en None. Si el diccionario esta vacio, retorna (None, None).
    
    if len(claves) > 0:             # Si el diccionario NO esta vacio, aplico el caso general del algoritmo. En caso contrario, se saltea el if.
        # Inicializacion:
        clave_max = claves[0]       # Asumo que la primera clave tiene el maximo valor
        valor_max = di[clave_max]   # Y me guardo el maximo valor
        
        # Obtengo el valor maximo:
        for i in range(1, len(claves)):         # Para cada clave restante
            clave_actual = claves[i]            # Obtengo la clave actual
            valor_actual = di[clave_actual]     # Y el valor actual
            if valor_actual > valor_max:        # Si el valor actual supera al maximo
                clave_max = clave_actual        # Guardo como clave del maximo valor a la actual
                valor_max = valor_actual        # Guardo como valor maximo el valor actual
        
        # Armo la tupla a retornar:
        ret = (clave_max, valor_max)
    
    return ret

#################################################
### 2. Encontrar la clave con el menor valor ####
#################################################

# Este algoritmo encuentra la clave que tiene asociado el menor valor. Las claves pueden ser de cualquier tipo (recordar que las mismas
# deben ser únicas), y los valores pueden ser:
# * int o float (se aplicará la comparación numérica habitual).
# * strings (conviene que los mismos estén formados solo por letras mayúsculas o minúsculas -no ambas-, y se aplicará la comparación por tabla ASCII).

def min_dict(di):
    """
    Recibe un diccionario y devuelve una tupla con:
    [0] la clave para la cual se asocia el menor valor.
    [1] dicho valor minimo.
    Si el diccionario esta vacio, retorna (None, None).
    """
    claves = list(di.keys())        # Obtengo todas las claves.
    ret = (None, None)              # Inicializo el valor de retorno en None. Si el diccionario esta vacio, retorna (None, None).
    
    if len(claves) > 0:             # Si el diccionario NO esta vacio, aplico el caso general del algoritmo. En caso contrario, se saltea el if.
        # Inicializacion:
        clave_min = claves[0]       # Asumo que la primera clave tiene el menor valor
        valor_min = di[clave_min]   # Y me guardo el menor valor
        
        # Obtengo el valor minimo:
        for i in range(1, len(claves)):         # Para cada clave restante
            clave_actual = claves[i]            # Obtengo la clave actual
            valor_actual = di[clave_actual]     # Y el valor actual
            if valor_actual < valor_min:        # Si el valor actual es menor que el minimo
                clave_min = clave_actual        # Guardo como clave del minimo valor a la actual
                valor_min = valor_actual        # Guardo como valor minimo el valor actual
        
        # Armo la tupla a retornar:
        ret = (clave_min, valor_min)
    
    return ret

##### Pruebas
"""
di = {
    'a': 1,
    'b': 5,
    'c': 2,
    'd': 4,
    'e': 0
}

print(max_dict(di))     # ('b', 5)
print(min_dict(di))     # ('e', 0)
"""

##########################################################################################################

#############################################################################################
### 3. Contar la cantidad de repeticiones de elementos en una lista, según algún criterio ###
#############################################################################################

# Supongamos que tenemos la siguiente lista, que contiene strings con marcas y
# modelos de autos (no me molestaría tener alguno de ellos):

autos = [
    'Toyota GR 86',                         # Toyota
    'Porsche 918 Spyder',                   # Porsche
    'Chevrolet Corvette Z06',               # Chevrolet
    'Honda NSX',                            # Honda
    'Nissan Skyline',                       # Nissan
    'Honda Civic Type R',                   # Honda
    'Lamborghini Aventador SVJ',            # Lamborghini
    'Porsche Panamera',                     # Porsche
    'Ferrari 458 Italia',                   # Ferrari
    'Ferrari F8 Tributo',                   # Ferrari
    'Mazda RX7',                            # Mazda
    'Subaru Impreza WRX',                   # Subaru
    'BMW M4 Competition',                   # BMW
    'Porsche 718 Cayman',                   # Porsche
    'Mercedes-Benz C63 AMG',                # Mercedes-Benz
    'Audi TT RS',                           # Audi
    'Porsche 911 GT3 RS',                   # Porsche
    'Toyota Supra',                         # Toyota
    'Ford GT40'                             # Ford
]

# Supongamos ahora que queremos contar cuántos autos hay de cada marca (la marca siempre
# es la primera palabra del string, es decir, siempre está entre el principio del mismo
# y el primer espacio que aparece).

# Para obtener el criterio según el cual contar los elementos (que, en este caso, es la marca,
# podemos - y es bastante recomendable - hacer una función que extraiga la información necesaria
# del string).

def obtener_marca(s):       # Esta función separa el string por sus espacios, y devuelve la primera
    return s.split()[0]     # palabra que contiene el mismo.

# Ahora, el siguiente algoritmo permite contar cuántos autos hay de cada marca. Esta idea puede ser
# reutilizada en MUCHOS ejercicios (de segundo parcial y de finales) donde se tenga que resolver un
# problema similar (por ejemplo, en el final de febrero 2025, donde había que contar la cantidad de
# apariciones de distintas aerolíneas).

def contar_marcas(lst):
    """
    Recibe una lista de strings, los agrupa según el criterio indicado, y devuelve un diccionario donde las claves son
    las marcas (el criterio), y los valores son la cantidad de apariciones de cada marca.
    """
    di = {}                 # Lo primero que hacemos es inicializar un diccionario vacío para poder contar las ocurrencias.
                            # Las keys serán las marcas, y los values, la cantidad de apariciones.
    for s in lst:                       # Para cada string en la lista
        marca = obtener_marca(s)        # Extraemos la marca (que es el criterio por el cual se agrupan los elementos).
        
        # Y AHORA VIENE LA PARTE CLAVE: Como las keys en un diccionario son únicas, si encontramos una marca que NO esté
        # actualmente en el diccionario, la agregamos al mismo con un valor de 1 (porque encontramos en la lista 1 auto de
        # esa marca hasta el momento). 
        # Ahora bien, si la marca ya se encuentra en el diccionario, es porque anteriormente ya encontramos autos de dicha marca.
        # En ese caso, simplemente incrementamos en 1 el valor para esa key (indicando que encontramos 1 auto más de esa marca).

        if marca not in di:             # Si la marca NO está en el diccionario
            di[marca] = 1               # Agregamos la marca
        else:                           # Si la marca ya estaba en el diccionario
            di[marca] += 1              # Le sumamos una aparición
    
    return di                           # Retornamos el diccionario

##### Prueba:
"""
marcas_y_apariciones = contar_marcas(autos)
print(marcas_y_apariciones)

# Ahora, podemos también aplicar los algoritmos anteriores. Por ejemplo, podríamos
# mostrar cuál es la marca con más apariciones.

marca, apariciones = max_dict(marcas_y_apariciones)
print('La marca con más apariciones es {}, que aparece {} veces.'.format(marca, apariciones)) # Porsche, 4 apariciones.
"""
