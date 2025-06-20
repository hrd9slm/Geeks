
import random 
def check(number):
    random_number=random.randint(1, 100)
    if number < 1 or number > 100:
            return "number invalid --->[1,100]"
    else:
            if random_number==number:
                return f"Success!"
            else: 
                return f"Fail! Your number: {number}, Random number: {random_number}"
    

print(check(0))