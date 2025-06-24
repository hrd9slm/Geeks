class Person :
    def __init__(self,first_name,age,last_name=""):
        self.first_name=first_name
        self.age=age
        self.last_name=last_name
    
    def is_18(self):
        if self.age >=18:
            return True
        else:
            return False
        
class Family :
    def __init__(self,last_name,members=[]):
        self.last_name=last_name
        self.members=members
    
   
    def  born(self,first_name, age):
        person=Person(first_name,age,self.last_name)
        self.members.append(person)

    def check_majority(self,first_name):
        for person in self.members:
            if person.first_name==first_name:
                if person.is_18():
                    print(f"{person.first_name} You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print(f"Sorry {person.first_name}, you are not allowed to go out with your friends.")


    def family_presentation(self):
        print(f"family_presentation: {self.last_name}")
        for person in self.members:
            print(f"-{person.first_name} ---------> {person.age}")



my_family = Family("El Amrani")

my_family.born("Aya", 14)
my_family.born("Youssef", 20)
my_family.born("Salma", 17)

my_family.family_presentation()


my_family.check_majority("Aya")
my_family.check_majority("Youssef")
my_family.check_majority("Salma")



