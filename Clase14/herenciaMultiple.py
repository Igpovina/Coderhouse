class Mamifero():
    def __init__(self, cant_mamas, esperanza_de_vida):
        self.cant_mamas = cant_mamas
        self.esperanza_de_vida = esperanza_de_vida
        self.peso = 0.5
        self.__vivo = False
        
    def mamar(self, tiempo):
        self.peso += (tiempo * 0.2)
    
    def nacer(self):
        self.__vivo = True
        
    def get_vivo(self):
        if self.__vivo:
            return "esta vivo"
        else:
            return "no esta vivo"
    
class Animal_marino():
    
    def __init__(self, tiene_branqueas, especie):
        self.branqueas = tiene_branqueas
        self.especie = especie
        
    def nadar(self):
        return f'Nadaremos, nadaremos, en el mar'
    
    
class Cetaceo(Mamifero, Animal_marino):
    
    def __init__(self, cant_mamas, esperanza_de_vida, tiene_branqueas, especie, vive_en, notas = None,):
        Mamifero.__init__(self, cant_mamas, esperanza_de_vida)
        Animal_marino.__init__(self, tiene_branqueas, especie)
        self.notas = notas
        self.vive_en = vive_en
        
    def nadar(self):
        return f'Estooooyyy nadaaaandoooo'
    
mamifero1 = Mamifero(4, 10)
mamifero1.nacer()
print(mamifero1.get_vivo())

cetaceo1 = Cetaceo(6, 15, "No", "Ballena Azul", "Atlantico", "mas pequenos")

print(cetaceo1.nadar())