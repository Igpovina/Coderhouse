divisas = {'Dolar':'$','Euro':'€', 'Libra':'£'}

busqueda = input("Ingrese la divisa que desea visualizar: ")
print(divisas.get(busqueda,"Esa divisa no esta disponible"))

# for i in divisas.keys():
#     if busqueda == i:
#         print(divisas.get(i))
#     else:
#         print("divisa no disponible")