edad = int(input("Ingrese su edad: "))
antiguedad = int(input("Hace cuantos anios usa este banco: "))
ingreso = int(input("Ingrese salario mensual en dolares: "))

if (edad >= 18):
    if(antiguedad >= 3 and ingreso >= 2500):
        print("Credito Bancario aprobado")
    elif(ingreso >= 4000):
        print("Credito Bancario aprobado")
    else:
        print("Su credito Bancario no ha sido aprobado")
else:
    print("Su credito Bancario no ha sido aprobado")
