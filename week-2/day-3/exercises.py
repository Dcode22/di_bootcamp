#exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))

print(dictionary)


#exercise 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
totalCost = 0
for key in list(family.keys()):
    if family[key] < 3:
        pass  
    elif family[key] < 12:
        totalCost += 10
    else:
        totalCost += 15
print('total: ', totalCost)

#exercise 3 

brand = {
    "name": "Zara", 
    "creation_date": 1975, 
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    'number_stores': 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

print(f"Zara's clients are people in {list(brand["major_color"].keys())[0]}, {list(brand["major_color"].keys())[1]} and {list(brand["major_color"].keys())[2]}.")
brand["country_created_in"] = "Spain"
if list(brand.keys()).count("international_competitors"):
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand.keys()))

print(list(brand.keys()))

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print(brand["number_stores"]) #updated value


# exercise 4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {}
disney_users_B = {}
disney_users_C = {}

for i in users:
    disney_users_A[i] = users.index(i)
    disney_users_B[users.index(i)] = i
users.sort()
for i in users:
    disney_users_C[i] = users.index(i)
print('A', disney_users_A)
print('B', disney_users_B)
print('C', disney_users_C)

disney_users_A2 = {}
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
for i in filter(lambda a: a.count('i') or a[0] =='M' or a[0] == 'P', users):
    disney_users_A2[i] = users.index(i)

print('A2', disney_users_A2)


