class cat():
    def __init__(self,name,age):
        self.name =name
        self.age=age


    def compare(self,cat1,cat2):
        if self.age >= cat1.age and self.age >= cat2.age:
           print(f"The oldest cat is {self.name}, and is {self.age} years old.”")
        elif cat1.age >= self.age and cat1.age >= cat2.age:
            print(f"The oldest cat is {cat1.name}, and is {cat1.age} years old.”")
        else:
             print(f"The oldest cat is {cat2.name}, and is {cat2.age} years old.”")
    
    @staticmethod
    def compare_old(cat1, cat2, cat3):
        if cat3.age >= cat1.age and cat3.age >= cat2.age:
           print(f"The oldest cat is {cat3.name}, and is {cat3.age} years old.”")
        elif cat1.age >= cat3.age and cat1.age >= cat2.age:
            print(f"The oldest cat is {cat1.name}, and is {cat1.age} years old.”")
        else:
             print(f"The oldest cat is {cat2.name}, and is {cat2.age} years old.")

if __name__ == "__main__":
    cat_1=cat("murphy",3)
    cat_2=cat("marry",4)
    cat_3=cat("sun",5)
    cat.compare_old(cat_1,cat_2,cat_3)
    print("-------------------------")
    cat_1.compare(cat_2,cat_3)
    cat_2.compare(cat_3,cat_1)
    cat_3.compare(cat_1,cat_2)
