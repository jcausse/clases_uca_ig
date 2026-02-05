"""
Ejercicio 3:

El concepto de paridad es de fundamental importancia para la detección y corrección de                           
errores en el almacenamiento y transmisión de datos en los sistemas informáticos. Para                         
cada dato en binario se genera un bit adicional (bit de paridad) de manera tal que este                                 
será 1 (​uno​) si la suma de la cantidad de 1 (​unos​) presentes en el dato es impar y 0                                       
(​cero​) si esta suma es par.  
 
Programar la función booleana ​paridad ​que recibe como parámetro un número binario                       
de hasta 8 bits y genera y retorna el bit de paridad correspondiente. Utilizarla en un                               
programa que solicite al usuario el ingreso del número binario, invoque a la función e                             
informe la paridad generada.
"""

"""
Un byte, que puede ser por ejemplo 1101 1001 va a tener un:
* Most Significative Bit (MSb) => el de mas a la izquierda
* Less Significative Bit (LSb) => el de mas a la derecha

En un byte (8 bits), podemos numerar los bits del 0 al 7, donde el bit 0 es el LSb, y el
bit 7 es el MSb

1       1       0       1       1       0       0       1
bit 7   bit 6   bit 5   bit 4   bit 3   bit 2   bit 1   bit 0
"""

# Hacemos una funcion que nos permita extraer un bit cualquiera, dado su numero de bit
# Ejemplo:
"""
byte = 11011001
print(get_bit(byte, 4)) # Imprime 1
print(get_bit(byte, 1)) # Imprime 0
"""

def get_bit(byte, bit_num):
    return (byte // (10 ** bit_num)) % 10

def parity(byte):
    ones_count  = get_bit(byte, 0)
    ones_count += get_bit(byte, 1)
    ones_count += get_bit(byte, 2)
    ones_count += get_bit(byte, 3)
    ones_count += get_bit(byte, 4)
    ones_count += get_bit(byte, 5)
    ones_count += get_bit(byte, 6)
    ones_count += get_bit(byte, 7)
    return ones_count % 2

def main():
    byte = int(input('Ingrese un numero binario de hasta 8 bits: '))
    print('Bit de paridad:', parity(byte))

main()
