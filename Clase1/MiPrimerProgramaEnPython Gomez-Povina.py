#Primer programa en Python

'''
    Este programa calcula la nota final de los estudiantes.
    La nota final se calcula basandose en 3 notas previas a las cuales
    cada una le corresponde un porcentaje distinto de la nota final
        nota 1: 20%
        nota 2: 30%
        nota 3: 50%
'''
nota_1 = float(input('Ingrese la Primera nota: ')) * 0.2
nota_2 = float(input('Ingrese la Segunda nota: ')) * 0.3
nota_3 = float(input('Ingrese la Tercera nota: ')) * 0.5

nota_final = (nota_1 + nota_2 + nota_3)

print(nota_final)