brand = {
"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color":{"France": "blue",  "Spain": "red", "US": ["pink", "green"]}}

brand["number_stores"]=2


print("Zara's client: ")
for type in brand["type_of_clothes"]:
    print(f"- {type}")
brand["country_creation"]="Spain"


for x in brand["international_competitors"]:
    if "Desigual" not in brand["international_competitors"]:
        brand["international_competitors"].append("Desigual")
    print(f"- {x}")


del brand["creation_date"]
print("brand",brand)


print( brand["international_competitors"][-1])
print( brand["major_color"]["US"])

keys=brand.keys()
print(" the number of keys :" ,len(keys))

print(keys)

new={
    "creation_date": 1975,
    "number_stores": 64395
}
print(brand.update(new))
print(brand)