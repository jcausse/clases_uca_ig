"""
Ejercicio 8:

Desarrollar un programa en el que se ingrese un valor numérico entero, el cual                           
representa una cantidad expresada en segundos, y luego lo exprese en días, horas,                         
minutos y segundos.

60 segundos             = 1 minuto
60 * 60 segundos        = 60 minutos    = 1 hora
60 * 60 * 24 segundos   = 1440 minutos  = 24 horas  =   1 dia

Ejemplo:
--------

36344573845 segundo    36344573845 dia * segundo
------------------- =  ----------- ------------- = 420654 dia
            segundo    86400       segundo
86400       -------
            dia

=> El resto de dividir 36344573845 // 86400 es 68245
=> 36344573845 segundos equivale a 420654 dias y 68245 segundos
            
68245 segundo   68245 hora * segundo
------------- = ----- -------------- = 18 hora
      segundo   3600  segundo
3600  -------
      hora

=> El resto de dividir 68245 // 3600 es 3445
=> 68245 segundos equivale a 18 horas y 3445 segundos

3445 segundo   3445 minuto * segundo
------------ = ---- ---------------- = 57 minuto
     segundo    60  segundo
60   -------
     minuto

=> El resto de dividir 3445 // 60 es 25
=> 3445 segundos equivale a 57 minutos y 25 segundos

=> Finalmente:
DIVIDENDO       DIVISOR     COCIENTE    RESTO   INTERPRETACION
36344573845     86400       420654      68245   => 420654 dias     
68245           3600        18          3445    => 18 horas
3445            60          57          25      => 57 minutos, 25 segundos

=> 36344573845 segundos equivale a 420654 dias, 18 horas, 57 minutos y 25 segundos
"""

# Conversions:
SECS_PER_DAY  = 60 * 60 * 24 # 86400
SECS_PER_HOUR = 60 * 60      # 3600
SECS_PER_MIN  = 60           # 60

total_seconds = int(input('Ingrese una cantidad total de segundos: '))

# Calculate whole days and remainding seconds
days        = total_seconds // SECS_PER_DAY
remainder   = total_seconds %  SECS_PER_DAY

# Calculate whole hours and remainding seconds
hours       = remainder     // SECS_PER_HOUR
remainder   = remainder     %  SECS_PER_HOUR

# Calculate whole minutes and remainding seconds
minutes     = remainder     // SECS_PER_MIN
remainder   = remainder     %  SECS_PER_MIN

# The remainder equals the amount of seconds 0 - 59
seconds = remainder

print('{} segundos equivale a {} dias, {} horas, {} minutos y {} segundos'.format(
    total_seconds,
    days,
    hours,
    minutes,
    seconds
))
