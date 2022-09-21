# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

lista = list(range(11))
lista2 = list(range(-10,1))
lista3 = list(range(0,21,2))
lista4 = list(range(-19,0,2))
lista5 = list(range(0,51,5))
# for i in range(11):
#     lista.append(i)
#     lista2.append(i-10)
#     lista3.append(2*i)
#     lista4.append((i*2)-21)
#     lista5.append(5*i)
print(lista)
print(lista2)
print(lista3)
print(lista4)
print(lista5)