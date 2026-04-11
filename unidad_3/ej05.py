def is_leap_year(year): 
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def is_valid_date(day, month, year):
    if day <= 0 or month <= 0 or month > 12 or year < 0:
        ret = False
    else:
        if month == 4 or month == 6 or month == 9 or month == 11:
            ret = day <= 30
        elif month == 2:
            if is_leap_year(year):
                max_day = 29
            else:
                max_day = 28
            ret = day <= max_day
        else:
            ret = day <= 31
    return ret

def main():
    day = int(input('Ingrese dia: '))
    month = int(input('Ingrese mes: '))
    year = int(input('Ingrese año: '))

    if is_valid_date(day, month, year):
        print('{:02d}/{:02d}/{} es una fecha valida'.format(day, month, year))
    else:
        print('Fecha invalida')

main()
