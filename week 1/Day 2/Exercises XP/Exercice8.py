topic=""
topic_list=[]
base_price=10

while topic !="stop":
    topic=input("entrer le topic : ")
    if topic == 'quit':
        break
    else:
        topic_list.append(topic)
        base_price+=2.5
        print(f"Adding {topic} to your pizza the price :{base_price}")

    

