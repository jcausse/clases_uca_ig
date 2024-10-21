def minimo(a, b):
    if a < b:
        ret = a
    else:
        ret = b
    return ret

def mensaje(cant_1m, cant_5m, tendido):
    # Caños 5m
    necesarios_5m = tendido // 5                # Veo cuantos caños de 5 necesito
    usados_5m = minimo(cant_5m, necesarios_5m)  # Y uso el minimo entre los que necesito y los que tengo
    cubierto = 5 * usados_5m                    # Tendido cubierto hasta ahora (con caños de 5m)

    # Caños 1m
    necesarios_1m = tendido - cubierto          # Necesito tantos caños de 1m como metros me falten cubrir
    if necesarios_1m > cant_1m:                 # En este caso, si necesitara mas de los que tengo, no se puede cubrir el tendido
        ret = "No es posible cubrir el tendido."
    else:                                       # Si tengo justo los que necesito o mas, si se puede
        ret = "Es posible cubrir el tendido.\nSugerencia:\n{} unidades de caño de 5 metros.\n{} unidades de caño de 1 metro.".format(usados_5m, necesarios_1m)
    return ret

def main():
    cant_1m = int(input('Cantidad de caños de 1 metro:  '))
    cant_5m = int(input('Cantidad de caños de 5 metros: '))
    tendido = int(input('Metros totales a cubrir:       '))
    print(mensaje(cant_1m, cant_5m, tendido))

main()
