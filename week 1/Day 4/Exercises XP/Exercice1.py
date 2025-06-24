class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

        
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese (Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
if __name__=="__main__":
    Siamese1=Siamese("max", 2)
    Siamese2=Siamese("sem",3)
    Chartreux1=Chartreux("morphy",1)
    Bengal1=Bengal("moon",1)

    animals=[Siamese1,Siamese2,Chartreux1,Bengal1]

    sara_pets=Pets(animals)

    sara_pets.walk()

