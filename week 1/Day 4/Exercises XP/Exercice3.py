from Exercice2 import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight,trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        return self.bark()


    def play(self, *args):
        names=self.name+","
        for dog in args:
            names+=dog.name+","
        return f"{names} all play together"
    
    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        index = random.randint(1, 3)
        if self.trained==True:
            return f"{tricks[index]}"
        else:
            return "walo"

        


# Test PetDog methods
my_dog1 = PetDog("Fido", 2, 11)
my_dog2 = PetDog("yteu", 5, 10)
my_dog3 = PetDog("qsf", 3, 17)
my_dog4 = PetDog("dodt", 6, 13)
# my_dog.train()
# my_dog.play("Buddy", "Max")
# my_dog.do_a_trick()£
print(my_dog1.play(my_dog2,my_dog3,my_dog4))
my_dog1.play(my_dog2,my_dog3,my_dog4)
print(my_dog1.do_a_trick())
my_dog1.train()
print(my_dog1.do_a_trick())

