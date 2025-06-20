def Define_family():
   
    dict={}
    while  True:
        name =input("Enter name's member or \'s\' to stop :")
        if name == "s" or name == "S":
            break
        age =input("Enter age's member :")
        dict[name] = int(age)   
    return dict


def Calculate(dict):
    cost=0
    for key,value in dict.items():
        if value < 3:
            cost_ticket=0
            cost+=cost_ticket
        elif  3<= value <12:
            cost_ticket=10
            cost+=cost_ticket
        else:
            cost_ticket=15
            cost+=cost_ticket
        print(f"the ticket price for \'{key}\' is {cost_ticket}")
        
    return f"the total cost is  {cost}"

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
print(Calculate(family))


family = Define_family()
print(Calculate(family))