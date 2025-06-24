class Dog:
    def __init__(self, name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight
       

    def bark(self):
       return f"{self.name} is barking"

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):
        if self.run_speed()* self.weight> other_dog.run_speed()* other_dog.weight:
            return f"{self.name} is winning"
        elif self.run_speed()* self.weight < other_dog.run_speed()* other_dog.weight:
            return f"{other_dog.name} is winning"
        else:
            return "no one is winnig"


if __name__=="__main__":        
    # Step 2: Create dog instances
    dog1=Dog("alex",3,55)
    dog2=Dog("boby",5,23)
    dog3=Dog("ren",4,46)

    # Step 3: Test dog methods
    print(dog1.bark())
    print(dog2.run_speed())
    print(dog1.fight(dog2))