class Farm:
    def __init__(self,farm_name):
        self.name=farm_name
        self.animal={}
    
    def add_animal(self,animal_type,count=1):
        if animal_type in self.animal:
            count=self.animal[animal_type]+count
            self.animal[animal_type]=count
        else :
             self.animal[animal_type]=count

        return f"{animal_type}-----> {count}"

    def get_info(self):
        print(f"the farm name : {self.name}")
        for animal,count in self.animal.items():
            print(f"- {animal} : {count}\n") 
        return "E-I-E-I-O!"





if __name__ == "__main__":
    farm1=Farm("hadika")
    farm1.add_animal("sba3",3)
    farm1.add_animal("jmal",2)
    farm1.add_animal("timssah",9)
    farm1.add_animal("bagra")
    print(farm1.get_info())
  