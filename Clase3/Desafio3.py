#conditionals

from typing_extensions import Self


nombre = input("Escriba un nombre: ")
validate_name1 = nombre != "****"
validate_name2 = len(nombre)>=4 and len(nombre)<8
validate_name = validate_name1 and validate_name2
# while(validate_name == False):
#     nombre = input("Ingrese un nombre correcto: ")
#     validate_name1 = nombre != "****"
#     validate_name2 = len(nombre)>=4 and len(nombre)<8
#     validate_name = validate_name1 and validate_name2

edad = int(input("Ingrese edad: "))
validate_age1 = edad > 5 and edad < 20
validate_age2 = (edad*3)>35
validate_age = validate_age1 and validate_age2
# while(validate_age == False):
#     edad = int(input("Ingrese una edad valida: "))
#     validate_age1 = edad > 5 and edad < 20
#     validate_age2 = (edad*3)>35
#     validate_age = validate_age1 and validate_age2

print(validate_name1 and validate_name2)
print(validate_age1 and validate_age2)



#lista = [not False,
#         not 3==5,
#         33/3 == 11 and 5>2,
#         True or False,
#         True*5 == 2.5*2 or 123>=23,
#         12>7 and True<False]
#print(lista)
