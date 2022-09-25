class Persona():
    def __init__(self, nom, ape, ed):
        self.nombre = nom 
        self.apellido = ape
        self.edad = ed
        
    def saluda(self):
        return f'Hola, mi nombre es {self.nombre} {self.apellido}'
    
    
messi = Persona("Lionel", "Messi", 35)
print(messi.saluda())