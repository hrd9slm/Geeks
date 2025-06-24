class Zoo():
    def __init__(self,zoo_name,animals):
        self.zoo_name=zoo_name
        self.animals=animals
        print(f"name: {self.zoo_name} , animals : {self.animals}")
    
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        
    
    def get_animals(self):
        print(f"Zoo : {self.zoo_name} :")
        for animal in self.animals :
            print(f"- {animal}")

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        dicti={}
        for animal in self.animals:
            first_letter = animal[0].lower()
            if first_letter not in dicti:
                dicti[first_letter] = [animal]
            else:
                dicti[first_letter].append(animal)

        return dict(sorted(dicti.items()))
    def get_groups(self):
        sorted_animals=self.sort_animals()
        for key,value in sorted_animals.items()  :
            print(f"{key.upper()}: {value}")

if __name__ == "__main__": 
    zoo_name="avantrix"  
    animals=['Baboon', 'Bear','Giraffe','Zebra','Lion','Cat', 'Cougar']
    zoo1=Zoo(zoo_name,animals)
    zoo1.add_animal("qqqqqqqq")
    zoo1.get_animals()
    print("--removing---")
    zoo1.sell_animal("qqqqqqqq")
    zoo1.get_animals()
    print("---sorting---")
    zoo1.sort_animals()
    print("---get_group---")
    zoo1.get_groups()
    







        

