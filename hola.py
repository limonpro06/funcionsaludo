import datetime

# Obtener la hora actual
hora_actual = datetime.datetime.now().hour

# Determinar el saludo segun la hora
if 5 <= hora_actual < 12:
    saludo = "Buenos dias"
elif 12 <= hora_actual < 18:
    saludo = "Buenas tardes"
else:
    saludo = "Buenas noches"

# Imprimir el saludo
print(saludo)
