numeros = [1, 3, 6, 9]
numero = int(input("Ingrese un numero del 0 al 9: "))
while(numero < 0 or numero > 9):
    numero = int(input("Ingrese un numero entre 0 y 9: "))
if(numeros.count(numero)):
    print("El numero {} se encuentra en la lista".format(numero))
else:
    print("El numero {} no se encuentra en la lista".format(numero))