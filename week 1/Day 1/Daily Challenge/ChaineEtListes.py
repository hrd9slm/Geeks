# Defi 1
print("Defi 1\n--------")
number=int(input("Etrer un nombre : "))
longueur=int(input("Etrer une longueur : "))
liste=[number]
new_number=number
for i in range(longueur-1):
   new_number +=number
   liste.append(new_number)
print(liste)
# Defi 2
print("Defi 2\n--------")
mot=input("Etrer un mot : ")
mot2=""
for i in mot:
    if len(mot2)==0:
        mot2+=i 
    elif i  not in mot2:
        mot2+=i 
    else:
        continue   
print(mot2)
