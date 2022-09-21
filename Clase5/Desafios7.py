# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
for i in lista_1:
    if(lista_1.count(i) and lista_2.count(i) and lista_3.count(i) == 0):
        lista_3.append(i)
print(lista_3)
    