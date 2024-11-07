"""
Ejercicio 2:

Dado un string de dos caracteres denominado “extremos” (por ejemplo ​“<>” o ​“$$”) y                           
otro string que contiene una palabra, desarrollar una función que reciba ambos strings                         
como parámetros y que retorne un nuevo string donde la palabra se encuentre en el                             
medio de los caracteres “extremos”. En caso de qué “extremos” no contenga dos                         
elementos o en caso de qué “palabra” sea vacío, la función deberá retornar un string                             
vacío. Desde el programa principal ingresar por teclado los extremos y la palabra,                         
invocar a la función y mostrar por pantalla el resultado que retorna la función tal como se                                 
ilustra en los siguientes ejemplos: 
 
Ingrese los extremos: {}  
Ingrese palabra: hola  
 
La función retornó: {hola} 
 
Ingrese los extremos: #  
Ingrese palabra:  cristal 
 
La función ha retornado una palabra vacía
"""

def ejercicio2(extremos, palabra):
    if len(extremos) != 2 or palabra == '':     # Aca verifique que el string de extremos tenga 2 caracteres  
        return ''
    return extremos[0] + palabra + extremos[1]  # Aca, hacer extremos[0] y extremos[1] es seguro, pues si el string no tuviera
                                                # 2 caracteres habría retornado '' en la línea anterior. Esta verificación siempre
                                                # es buena, porque sino, acceder a un elemento fuera de rango causaría un error.
                                                # Notar que extremos[0] NO ES UN SLICE, sino que accede al primer caracter del string.
                                                # El acceso a índices inválidos SI genera errores (IndexError), no así los slices.
    
def main():
    extremos = input('Ingrese los extremos: ')
    palabra = input('Ingrese palabra: ')
    resultado = ejercicio2(extremos, palabra)
    if resultado == '':
        print('La función ha retornado una palabra vacía')
    else:
        print(resultado)
    
main()
