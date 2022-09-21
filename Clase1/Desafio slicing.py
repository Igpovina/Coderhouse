#Clase 1

#Programa que devuleve un string invertido usando slicing

cadena = "acitametaM, 5.8, otipeP ordeP"

cadena_volteada = cadena[::-1] # doy vuelta la cadena y la guardo en una variable nueva

print(cadena_volteada) # verifico

#hago el slicing de la cadena completa y guardo cada valor en una variable nueva
nombre_alumno = cadena_volteada[0:12:]
nota = cadena_volteada[14: 17:]
materia = cadena_volteada[19: 30:]
#verifico
print(nota)
print(materia)
print(nombre_alumno)

#imprimo cadena completa
print("{} ha sacado un {} en {}".format(nombre_alumno, nota, materia))
#(el '.format' lo uso para no tener que concatenar sumando, en los parentesis pongo 
# las varialbes que vana a aparecer en las llaves, en el orden correcto)