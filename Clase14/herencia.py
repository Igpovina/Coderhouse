# class Animal():
#     def __init__(self, especie, edad):
#         self.especie = especie
#         self.edad = edad
    
#     def hablar(self):
#         pass
    
#     def moverse(self):
#         pass
    
#     def describirme(self):
#         print("Soy un animal del tipo", type(self).__name__)
        
# class Perro(Animal):
#     def __init__(self, especie, edad, dueno):
#         super().__init__(especie, edad)
#         self.dueno = dueno
        
# perro1 = Perro("mamifero", 4, "Ignacio")

# perro1.describirme()



class Persona():
    
    def __init__(self, nombre, apellido, edad, sexo, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.dni = dni
        
    def saludar(self):
        print("Hola mi nombre es {} {} y soy un/a {}".format(self.nombre, self.apellido,type(self).__name__))
        


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, sexo, dni, sueldo, horario):
        super().__init__(nombre, apellido, edad, sexo, dni)
        self.sueldo = sueldo
        self.horario = horario
               
    def fichar(self, ingreso):
        if(ingreso <= self.horario):
            return f'Llegue {self.horario - ingreso} minutos temprano'
        else:
            return f'Llegue {ingreso - self.horario} minutos tarde'
    
        
class Seguridad(Empleado):
    def __init__(self, nombre, apellido, edad, sexo, dni, sueldo, horario, vehiculo, arma):
        super().__init__(nombre, apellido, edad, sexo, dni, sueldo, horario)
        self.vehiculo = vehiculo
        self.arma = arma
    
    def llamar_policia(self, mensaje):
        return f'Hola policia {mensaje}'
        
        
        
        
persona1 = Persona("Ignacio", "Gomez", 34, "Masculino", 36896810)
empleado1 = Empleado("Pepe", "argento", 55, "Masculino", 34856987, 1500, 360)
seguridad1 = Seguridad("Paul", "Blart", 40, "Masculino", 12345678, 2500, 360, "Fiat Uno", "Glock18")
persona1.saludar()
empleado1.saludar()
seguridad1.saludar()