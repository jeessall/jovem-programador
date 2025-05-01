class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"
    
class Gato (Animal):
    def emitir_som(self):
        return "Miau"

cachorro = Cachorro("Bobby")

gato = Gato("Mimi")

print(cachorro.nome,"-->",cachorro.emitir_som())
print(gato.nome,"-->",gato.emitir_som())


