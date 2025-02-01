"""
Ejercicio 3:
	
Desarrollar la función primeraMitad que reciba una palabra de longitud par como
parámetro, y que genere y retorne un string que contenga la primera mitad de dicha
palabra. Desde el programa principal ingresar por teclado la palabra, invocar a la función
y mostrar por pantalla el resultado que retorna la función. Para el caso que el texto
ingresado no sea una palabra (o sea contenga otros caracteres que no sean letras) o
que no sea de longitud par, se deberá pedir al usuario que realice el ingreso
nuevamente, dándole al mismo todas las oportunidades que sean necesarias (validación
del ingreso).
"""

def primeraMitad(palabra):
	return palabra[: len(palabra) // 2] 	# Con un slice, me quedo con todos los caracteres desde el principio hasta la mitad de la palabra																															# Se debe usar division entera con //, pues los slices requieren de indices de tipo int
																		
"""
# Version sencilla de validacion, pero ineficiente:																										
def esPalabra(s):
	res = True
		
	for c in s:
		if not(('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z')): # Si NO es letra
			res = False
		
	return res																																																																			
"""

# Version eficiente de validacion:
def esPalabra(s):
	"""
	Recibe una string, y retorna True si todos sus caracteres son letras, o False en caso contrario
	"""
	valida = True
	i= 0
	
	while valida and i < len(s):		# El ciclo termina al encontrar el primer caracter invalido
		c = s[i]
		if not(('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z')): # Si NO es letra
			valida = False
		i += 1
	
	return valida

"""
Estructura basica para hacer validaciones:

done = False
while not done:
	<Pido entrada usando input()>
	if <Condiciones de validacion (puede ser mas de una usando and)>:
		done = True
	else:
		<Mensaje de error con print()>
"""

def main():
	# Ingreso de la palabra
	done = False																					   					# Flag (bandera) que me indica si la palabra fue correctamente ingresada
	while not done:									 										    					# Mientras no se ingrese correctamente la palabra
		palabra = input('Ingrese una palabra: ') 								 				# Pido la palabra
		if len(palabra) % 2 == 0 and esPalabra(palabra) == True:  			# Si es valida
			done = True																				 						# salgo del ciclo
		else:																								  					# Sino, muestro un error
			print('Error. Ingrese una palabra de longitud par:', palabra)
		
	# Cuando salgo del ciclo, la palabra es valida
	print(primeraMitad(palabra))
	
main()
	
