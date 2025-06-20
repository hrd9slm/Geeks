word = input("Enter a word: ")
dicti = {}
for i, y in enumerate(word):
    if y in dicti:
        dicti[y].append(i)
    else:
        dicti[y] = [i]

print(dicti)