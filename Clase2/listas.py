print("\nLIST")
lista_vieja = [1, 2, 3, 4]
print(lista_vieja)

print("\nAPPEND")
lista_vieja.append(5)
print(lista_vieja)

print("\nCOPY & CLEAR")
lista_nueva = lista_vieja.copy()
lista_vieja.clear()
print(lista_vieja)
print(lista_nueva)

print("\nEXTEND")
mas_numeros = [4, 4, "HOLA", 6, 7]
# lista_nueva.append(mas_numeros)
lista_nueva.extend(mas_numeros)
print(lista_nueva)

print("\nCOUNT")
print(lista_nueva.count(4))

print("\nINDEX")
print(lista_nueva.index("HOLA"))

print("\nINSERT")
lista_nueva.insert(8, "ADIOS")
print(lista_nueva)

print("\nPOP")
lista_nueva.pop()
lista_nueva.pop(0)
# lista_nueva.pop("ADIOS")
print(lista_nueva)

# print("\nREMOVE")
# lista_nueva.remove("ADIOS")
# print(lista_nueva)

# print("\nREVERSE")
# lista_nueva.reverse()
# print(lista_nueva)

# print("\nSORT")
# # lista_nueva.sort()
# lista_nueva.remove("HOLA")
# print(lista_nueva)
# vocales = ["u", "e", "i", "a"]
# vocales.sort()
# print(vocales)
