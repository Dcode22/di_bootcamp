# exercise 1
my_fav_numbers = {22, 84, 97}
my_fav_numbers.add(64)
my_fav_numbers.add(33)
my_fav_numbers.remove(33)
friend_fav_numbers = {81, 49, 24}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# exercise 2
### no

# exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")
basket.clear()
print(basket)

# exercise 4
#1 floats are numbers with decimals
#2 
float_list = [number/2 for number in range(3, 11)]
print('float_list: ', float_list)
#3 
float_list2 = []
for i in range(1, 5):
    float_list2.extend([i + 0.5, i + 1])
print('float_list2: ', float_list2)

# exercise 5
for i in range(1, 21):
    print(i)
for i in range(1,21):
    if i % 2 == 0:
        print(i)

# exercise 6
my_name = "dave"
user_name = ""
while user_name != my_name:
    user_name = input("enter your name: ")

#  exercise 7
favorite_fruits = input('Enter your favorite fruits separated by a space: ').split()
guess = input("type the name of any fruit: ")
if favorite_fruits.count(guess):
    print("You chose one of your favorite fruits! Enjoy!")
else: 
    print("You chose a new fruit. I hope you enjoy")


# exercise 8
topping_entered = ""
all_toppings = []
while topping_entered != 'quit':
    topping_entered = input("enter a pizza topping, type 'quit' to quit: ")
    if topping_entered != 'quit':
        all_toppings.append(topping_entered)
        print(f"We'll add {topping_entered} to your pizza")
print(f"Order Summary:\n Toppings: {all_toppings}\n Total Price: {len(all_toppings)*2.5 + 10}")

# exercise 9
family_ages = input("Enter the ages of all family members getting tickets: ")
total_cost = 0
for age in map(lambda n: int(n), family_ages.split()): 
    if age < 3:
        pass
    elif age < 12:
        total_cost += 10
    else: 
        total_cost += 15
print('Total Cost: ', f"${total_cost}")


teenagers = ["Daryl", "Samantha", "Tom", "Justin", "Phoebe"]
for teen in teenagers.copy(): 
    age = int(input(f"Hey {teen} how old are you? "))
    if age < 16 or age > 21:
        teenagers.remove(teen)
    else:
        pass

print("Only the following people are allowed to enter: ", teenagers)


# exercise 10

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while sandwich_orders.count("Pastrami sandwich"):
    sandwich_orders.remove("Pastrami sandwich")
print('sandwich_orders: ', sandwich_orders)
finished_sandwiches = []
for sandwich in sandwich_orders.copy():
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)
print('finished_sandwiches: ', finished_sandwiches)
print('sandwich_orders: ', sandwich_orders)
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")

