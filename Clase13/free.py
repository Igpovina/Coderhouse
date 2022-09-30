class Alumno():
    
    def __init__(self, nombre, nota):
        self.f_name = nombre
        self._grade = nota

    def get_nombre(self):
        print("El nombre del alumno es {} su nota es {}".format(self.f_name, self._grade))

    def resultado(self):
        if self._grade > 5:
            print("{} esta aprobado".format(self.f_name))
        else:
            print("{} esta reprobado".format(self.f_name))
            
    def __str__(self):
        return f'soy un alumno llamado {self.f_name}'

ignacio = Alumno("Ignacio", 8)
print(ignacio)
# ignacio.get_nombre()
# ignacio.resultado()

"""
Crear una clase Atleta, que tenga su nombre, apellido, altura, peso, teléfono e índice de masa corporal (descripción) .
Decidir que atributos deben ser públicos y cuales privados. Crear los métodos get y set que crea necesarios.
Donde el imc es es peso dividido, la altura al cuadrado. con la altura en metros.
"""
class Atleta():
    
    def __init__(self, nombre, apellido, altura, peso, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.__altura = altura
        self.__peso = peso
        self.telefono = telefono
        self.__icm = peso/altura**2
    
    def get_nombre(self):
        return f'{self.nombre} {self.apellido}'
    
    def get_peso(self):
        return self.__peso
    def get_altura(self):
        return self.__altura
    def get_telefono(self):
        return self.telefono
    def get_icm(self):
        return self.__icm
    
    def set_peso(self, peso):
        self.__peso = peso
        self.__icm = self.__peso/self.__altura**2
    def set_altura(self, altura):
        self.__altura = altura
        self.__icm = self.__peso/self.__altura**2
    def set_telefono(self, telefono):
        self.telefono = telefono
        
atleta1 = Atleta("ignacio", "gomez", 1.63, 60, "+1 347-833-1229")
print(atleta1.get_nombre())
print(atleta1.get_icm())
atleta1.set_peso(50)
print(atleta1.get_icm())