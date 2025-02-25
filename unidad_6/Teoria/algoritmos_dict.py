###########################################
### Algoritmos útiles para diccionarios ###
###########################################

### 1. Encontrar la clave con el mayor valor
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

### 2. Encontrar la clave con el menor valor
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

### Pruebas
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
