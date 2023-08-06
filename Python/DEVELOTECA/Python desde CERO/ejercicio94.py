# Modulo de tiempo (usar modulos ya existentes dentro de Python)

import datetime # control del tiempo

tiempo = datetime.datetime.now() # la hora actual

# Formato de fecha M, Y, d
print(tiempo.strftime("%Y %m %d"))

