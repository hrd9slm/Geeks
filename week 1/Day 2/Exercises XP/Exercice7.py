import random
# srep 1
def get_random_temp() :
    random_number= random.randint(-10, 40)
    return random_number
#step 2
"""
def main():
    random_temp=get_random_temp()
    return f"“The temperature right now is {random_temp} degrees Celsius.”"
    """
# step 3
def main():
    random_temp=get_random_temp()
    if random_temp < 0:
        return f"The temperature right now is {random_temp}\nBrrr, that s freezing! Wear some extra layers today."
    elif 0 <= random_temp < 16:
        "The temperature right now is {random_temp}\nQuite chilly! Don t forget your coat."
    elif 16 <= random_temp < 24:
        return f"The temperature right now is {random_temp}\nNice weather."
    elif 24 <= random_temp < 33:
        return f"The temperature right now is {random_temp}\nA bit warm, stay hydrated."
    elif 33 <= random_temp <= 40:
        return f"The temperature right now is {random_temp}\nIt s really hot! Stay cool."
   
    
 # Bonus a faire ???????

print(main())

    
