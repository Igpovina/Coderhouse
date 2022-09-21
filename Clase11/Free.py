def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No puede dividir por 0")

try:
    nombre = input("ingrese su nombre: ")
    edad = int(input("ingrese su edad: "))
    print("El año que viene {} va a tener {} años".format(nombre, edad+1))
except:
    print("Ingrese datos validos")
    
while(True):
    try:
        peso = float(input("Ingrese su peso: "))
        altura = float(input("Ingrese su altura: "))
        imc = peso / (altura**2)
        print(imc)
    except ZeroDivisionError as e:
        print("La altura no puede ser 0")
    except ValueError as e:
        print("Ingreso datos no numericos")
    except Exception as e:
        print(type(e).__name__)
        print("ingreso datos no validos")
    else:
        print("Todo se calculo correctamente")
        break
    finally:
        print("Finaliza el bloque try")