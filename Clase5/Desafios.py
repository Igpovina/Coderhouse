number_a = int(input("Ingrese un numero: "))
number_b = int(input("Ingrese otr numero: "))
option = 1

while(option):
    option = int(input("Ingrese una opcion entre 1 - 4: "))
    if(option == 1):
        print(number_a + number_b)
    elif(option == 2):
        print(number_a - number_b)
    elif(option == 3):
        print(number_a * number_b)
    elif(option == 4):
        print("fin de programa")
        break
    else:
        print("Opcion invalida")