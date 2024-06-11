#challenge 1

word = input("Enter a word: ")

letters = list(set(word))

dictionary = {}

for i in letters:
    dictionary[i] = []
    for j in range(len(word)): 
        if word[j] == i:
            dictionary[i].append(j)

print(dictionary)



#challenge 2

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

for key in list(items_purchase.keys()):
    items_purchase[key] = int(items_purchase[key].replace("$", "").replace(",", ""))

wallet = int(input("How much can you spend: "))

canAfford = []
for key in list(items_purchase.keys()):
    if items_purchase[key] <= wallet:
        canAfford.append(key)

if len(canAfford):
    print("The following items are within your budget: ", canAfford)

else: 
    print("You cannot afford any of the items :(")





