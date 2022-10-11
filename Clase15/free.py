"""
escribir una funcion que pida al usuario su fecha de nacimiento (agno mes dia hora minuto)
y calcule cuantos anos tiene
cuantos dias faltan para su cumpleanois
"""
from datetime import datetime, timedelta


fecha_de_nacimiento = input("ingrese su fecha de nacimiento ej: dd/mm/aaaa ")

dt = datetime.now().date()
# print(dt)

fecha = datetime.strptime(fecha_de_nacimiento, "%d/%m/%Y").date()
print(type(fecha))


print(365-int(fecha.day))