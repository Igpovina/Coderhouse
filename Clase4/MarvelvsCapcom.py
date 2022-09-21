nombre = input("Ingrese su nombre: ")
fan = input("Marvel o Capcom: ")

if(fan == 'Marvel' and nombre[0] < 'M' or fan == 'Capcom' and nombre[0] > 'n'):
    print("Pertence al grupo A")
else:
    print("Pertenece al grupo B")