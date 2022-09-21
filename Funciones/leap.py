#devuelve si el anio es biciesto
def is_leap(year):
    leap = False
    if(not year%4):
        leap = True
        if(not year%100):
            if(not year%400):
                leap = True
                return leap
            leap = False
            return leap
    return leap


#Permutaciones
def permutaciones(x,y,z,n):
    intersection = list(([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)))
    new_list = []
    for i in intersection:
        if sum(list(i))!=n:
            new_list.append(i)
    print(new_list)
    
def ano_bisiesto(year):
  if(type(year)==int):
    leap = False
    if(not year%4):
        leap = True
        if(not year%100):
            if(not year%400):
                leap = True
                pass
            leap = False
            pass
    pass
    if(leap):
      print("{} es anio biciesto".format(year))
    else:
      print("{} no es anio biciesto".format(year))
  else:
    print("Por favor ingrese un numero")