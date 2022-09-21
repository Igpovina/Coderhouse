"""
Escribir un algoritmo que pida al usuario que ingrese nombres (uno a la vez) hasta que el usuario ingrese la palabra 'fin'
Agregar todos los nombres dentro de una lista ordenados alfabeticamente
Imprimir la lista
NO SE PERMITE usar el metodo sort
"""
def name_organizer():
    nombres = []
    nombre = ""
    while(True):
        nombre = input("Ingrese un nombre o fin para salir: ")
        if(nombre == "fin"):
            break
        elif len(nombres)==0:
            nombres.append(nombre.capitalize())
        else:
            for i,j in enumerate(nombres):
                if ((nombre.capitalize()) < j):
                    nombres.insert(i,nombre.capitalize())
                    break
            else:
                nombres.append(nombre.capitalize())
    print(nombres)

