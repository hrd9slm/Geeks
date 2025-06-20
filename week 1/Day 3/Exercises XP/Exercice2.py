class Dog():
    def __init__(self,name,height):
        self.name =name
        self.height=height
        print(f"the dog s name {self.name} and height:{self.height}")

    def bark(self):
         print(f"goes woof! ------> {self.name}")

         
    def jump(self):
        print(f" jumps {self.height*2} cm high!")


    def Compare_dog(self, dog):
        if self.height > dog.height:
            print(f"{self.name} is bigger than {dog.name}")
        elif self.height < dog.height:
            print(f"{dog.name} is bigger than {self.name}")
        else:
            print(f"{self.name} and {dog.name} are the same height")

            
if __name__ == "__main__":   
    dog_1=Dog("davids",21)
    dog_2=Dog("sarah",33)
    dog_1.bark()
    dog_1.jump()
    dog_2.bark()
    dog_2.jump()
    dog_1.Compare_dog(dog_2)

