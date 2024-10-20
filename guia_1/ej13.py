num1 = int(input('Ingrese el multiplicando: '))
num2 = int(input('Ingrese el multiplicador: '))

print()

print('{:10}'.format(num1))
print('x{:9}'.format(num2))
print('-' * 10)

num2_digito0 = (num2 // (10 ** 0)) % 10
num2_digito1 = (num2 // (10 ** 1)) % 10
num2_digito2 = (num2 // (10 ** 2)) % 10

print('{:10}'.format(num2_digito0 * num1))
print('+{:8}-'.format(num2_digito1 * num1))
print('{:8}--'.format(num2_digito2 * num1))


print('-' * 10)
print('{:10}'.format(num1 * num2))

"""
dividendo: 25
divisor:    4
cociente:   6
resto:      1

25  | 4
24    6
--
 1

dividendo = cociente * divisor + resto

EL RESTO SOLAMENTE PUEDE SER UN NUMERO ENTE 0 y (divisor - 1)
EL RESTO DE DIVIDIR CUALQUIER NUMERO POR 6 SOLAMENTE PUEDE
DAR RESULTADOS ENTRE 0 y 5 (incluido)

ENTONCES:
x % y, el resultado es un numero entre 0 e y-1 (incluido)

OBTENER DIGITOS DE UN NUMERO:
numero % 10 SIEMPRE obtiene el ultimo digito
numero // 10 SIEMPRE obtiene el numero SIN EL ULTIMO DIGITO
"""