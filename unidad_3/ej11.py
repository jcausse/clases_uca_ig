def minimo(a, b):
    if a <= b:
        ret = a
    else:
        ret = b
    return ret

def mensaje(cant_1, cant_5, total):
    cant_ideal_5 = total // 5   # Cantidad ideales: Cuantos usaria de cada longitud si tuviera infinitos de cada una
    
    # La cantidad de caños de 5 que voy a usar es el minimo entre los que necesitaria de manera ideal (suponiendo que tengo
    # infinitos) y los que verdaderamente tengo. Nunca voy a usar mas de los que idealmente necesitaria ni mas de los que
    # realmente tengo.
    usados_5 = minimo(cant_ideal_5, cant_5)
    
    # Lo que me sobra a cubrir con caños de 1 es el total menos lo que ya cubri con la cantidad de caños de 5 que use
    # Si cant_ideal_5 <= cant_5 (necesitaria menos o las misma cantidad que tengo), entonces el restante va a ser de 0 a 4 metros
    # En cambio, si cant_ideal_5 > cant_5 (necesitaria idealmente mas de los que tengo), entonces uso todos los que tengo pero me
    # va a faltar cubrir un tendido mayor o igual a 5 metros, que lo debo cubrir enteramente con caños de 1 metro. Ejemplos:
    # - cant_5 = 3, total = 21, uso los 3 que tengo, y necesito cubrir 6 metros mas solo con caños de 1 (los de 5 se acabaron)
    # - cant_5 = 3, total = 20, uso los 3 que tengo, y necesito cubrir 5 metros mas solo con caños de 1 (los de 5 se acabaron)
    restante = total - 5 * usados_5
    
    # Anteriormente quedo determinado un restante a cubrir con caños de 1. La cantidad de caños de 1 que necesito para cubrir ese
    # tramo que falta es (restante // 1) (que es igual a restante). Debo tener esa cantidad de caños de 1.
    # Ahora bien, puedo tener los suficientes caños de 1 como para cubrir el restante o no. Si los tengo, se puede cubrir. Si no
    # los tengo no puedo cubrir el total solicitado.
    if restante > cant_1:       # Si necesito mas caños de 1 que los que tengo para cubrir lo que falta
        ret = 'No es posible cubrir el tendido.'
    else:                       # Si me alcanzan
        ret =   'Es posible cubrir el tendido.\n' + \
                'Sugerencia:\n' + \
                '  {} unidades de caño de 5 metros\n' + \
                '  {} unidades de caño de 1 metro'

        # Recordar que los str son inmutables! Para formatear y "cambiar" el str hay que asignar de nuevo
        ret = ret.format(usados_5, restante) 
    
    return ret

def main():
    cant_1 = int(input('Cantidad de caños de 1 metros: '))
    cant_5 = int(input('Cantidad de caños de 5 metros: '))
    total  = int(input('Metros totales a cubrir: '))
    msg = mensaje(cant_1, cant_5, total)
    print(msg)
    
main()
