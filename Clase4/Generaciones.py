anio = int(input("Ingrese su año de nacimiento: "))

if(anio >= 1920 and anio <= 1940):
    print("Pertenece a la generacion silenciosa")
elif(anio >= 1946 and anio <=1964):
    print("Pertenece a la Generacion Baby Boome")
elif(anio >= 1965 and anio <= 1979):
    print("Pertenece a la Generacion X")
elif(anio >= 1980 and anio <= 2000):
    print("Pertenece a la Generacion Y tambien conocido como milennials")
elif(anio >= 2001 and anio <= 2010):
    print("Pertenece a la Generacion Z tambien conocido como Centennials")
else:
    print("No pertenece a ninguna Generacion")