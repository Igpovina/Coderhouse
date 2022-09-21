from sqlite3 import ProgrammingError


# ej 1
# Crear una funcion que reiba dos string y devuelva la posicion donde se encuentra el segundo string dentro del primero 
# en caso de que no se encuentre devolver -1
# NO ESTA PERMITIDO usar funciones de busqueda como find y rfind 
# ej "hello, welcome to my world", "welcome" --> 7

def string_match(main_string, sub_string):
    for i, j in enumerate(main_string):
        for poss, charsub in enumerate(sub_string):
            if main_string[i + poss] != charsub:
                break
            
            if poss == len(sub_string)-1:
                return i
            
    return -1

print(string_match("hello, welcome to my world", "welcome"))

def match_suma(arr, target):
    for i, num_i in enumerate(arr):
        for j, num_j in enumerate(arr[i+1:]):
            if num_i + num_j == target:
                return True
    return False

print(match_suma([1,5,9,11,19],11))