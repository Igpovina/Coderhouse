"""
    Clase 1
"""
#Programa para devolver promedio

partidos_ganados = int(input("Ingrese la cantidad de Partidos Ganados: ")) * 2
partidos_perdidos = int(input("Ingrese la cantidad de Partidos Perdidos: ")) * 0
partidos_empatados = int(input("Ingrese la cantidad de Partidos EMpatados: ")) * 1

cantidad_de_partidos = int(input("Ingrese la cantidad total de Partidos: "))

promedio = (partidos_empatados + partidos_ganados + partidos_perdidos)/cantidad_de_partidos
print(promedio)