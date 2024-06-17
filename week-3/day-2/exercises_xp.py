# exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
all_cats = [Bengal("Bobby", 12), Chartreux("Chatty", 15), Siamese("SooSoo", 8)]
sara_pets = Pets(all_cats)
sara_pets.walk()

# exercise 2

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        return self.weight/self.age*10
    
    def fight(self, other_dog: "Dog"):
        if self.run_speed()*self.weight < other_dog.run_speed()*other_dog.weight:
            print(f"{other_dog.name} wins the fight")
        else:
            print(f"{self.name} wins the fight")


layla = Dog("Layla", 5, 60)
blue = Dog("Blue", 4, 75)
rees = Dog("Rees", 3, 60)
layla.bark()
blue.run_speed()
rees.fight(blue)


# exercise 3: see ./exercise-3.py


# exercise 4
class Family:
    members = []
    def __init__(self, last_name: str):
        self.last_name = last_name

    def born(self, **child):
        self.members.append({"name": child["name"], "age": child["age"], "gender": child["gender"], "is_child": child["is_child"]})
     
    def is_18(self, name: str):
        person = next((member for member in self.members if member["name"] == name), None)
        return person["age"] >= 18

    def family_presentation(self):
        print(f"{self.last_name} Family:")
        for member in self.members:
            print(f"{member["name"]} is a {member["age"]} year old {member["gender"]} and is {"an adult" if self.is_18(member["name"]) else "a child"}")

wales_family = Family("Wales")
wales_family.born(name = "Michael", age = 35, gender = "Male", is_child = False)
wales_family.born(name = "Sarah", age = 32, gender = "Female", is_child = False)
wales_family.is_18("Michael")
wales_family.family_presentation()


# exercise 5

class TheIncredibles(Family):
    def use_power(self, name: str):
        person =  next((member for member in self.members if member["name"] == name), None)
        if self.is_18(name):
            print(person["power"])
        else: 
            raise Exception("must be over 18 to use power")
    
    def born(self, **child):
        super().born(**child)
        member = next((member for member in self.members if member["name"] == child["name"]), None)
        print('new member: ', member)
        member["power"] = child["power"]
        member["incredible_name"] = child["incredible_name"]

    def incredible_presentation(self):
        print("BEHOLD OUR INCREDIBLE CLAN:")
        super().family_presentation()
        for member in self.members:
            print('member: ', member)
            print(f"{member['name']}, AKA {member['incredible_name']}'s power is {member['power']}")

incredibles = TheIncredibles("Incredibles")
incredibles.born(name = 'Michael', age = 35, gender = 'Male', is_child = False, power ='fly', incredible_name = 'MikeFly')
incredibles.born(name = 'Sarah', age = 32, gender = 'Female', is_child = False, power = 'read minds', incredible_name = 'SuperWoman')

incredibles.incredible_presentation()
incredibles.born(name = 'Baby Jack', age = 1, gender = 'Male', is_child = True, power='Unknown Power', incredible_name = 'BabyJ')
incredibles.incredible_presentation()