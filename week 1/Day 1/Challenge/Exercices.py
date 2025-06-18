
# Exercice 1
print("Exercice 1\n------------")
print("Hello world\n" * 4)
# Exercice 2
print("Exercice 2\n------------")
print((99**3)*8)
# Exercice 3
print("Exercice 3\n------------")
nom = input("Entrer votre nom : ")
if nom == "salma":
    print("Hé ! On a le même prénom ? Salma power ✨😎 !")
else :
    print("Tu n'es pas Salma ? Dommage, mais tu es quand même le/la bienvenu(e) 😄 ! ")
# Exercice 4
print("Exercice 4\n------------")
taille=input("Tapez votre taille : ")
if int(taille)>= 145 :
     print("Vous etes assez grands pour rouler")
else :
     print("Vous avez besoin de grandir un peu plus pour rouler.")

# Exercice 5
print("Exercice 5\n------------")
my_fav_numbers=set([333,99,77])
print("my_fav_numbers :",my_fav_numbers)
my_fav_numbers.add(36)
my_fav_numbers.add(3665)
print("my_fav_numbers :",my_fav_numbers)
my_fav_numbers.remove(3665)
print("my_fav_numbers :",my_fav_numbers)
friend_fav_numbers=set([1,74,56,32,19])
print("friend_fav_numbers ;",friend_fav_numbers)
my_fav_numbersfriend_fav_numbersour_fav_numbers=my_fav_numbers | friend_fav_numbers
print("my_fav_numbersfriend_fav_numbersour_fav_numbers :",my_fav_numbersfriend_fav_numbersour_fav_numbers)

# Exercice 6
print("Exercice 6\n------------")
tuple = (3,6,21,435)
secon_tuple=(7,3)
print(tuple+secon_tuple)
# Exercice 7
print("Exercice 7\n------------")
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
print(basket.count("Apples"))
print(basket.clear())

# Exercice 8

print("Exercice 8\n------------")
# 1/
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
i = 0
new_sandwich_orders=[]
while i< len(sandwich_orders):
    item = sandwich_orders[i]
    i+=1
    if item != "Pastrami sandwich":
        new_sandwich_orders.append(item)
    else:
        continue
print(new_sandwich_orders)
sandwich_orders=new_sandwich_orders
# 2/
finished_sandwiches=[]
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print("\nSandwichs prepares :")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")


    





