option = int(input("Cuantos numeros quiere ingresar:" ))
suma = []
for i in range(option):
    suma.append(int(input("Ingrese un numero: ")))
print(suma)
print(sum(suma)/option)