# exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

tommy = Cat("Tommy", 3)
grey = Cat("Grey", 2)
gingy = Cat("Gingy", 12)

def findOldestCat(cats: [Cat]) -> Cat:
    oldest_cat = None
    for cat in cats:
        if not oldest_cat or cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat
print(f"The oldest cat is {findOldestCat([tommy, grey, gingy]).name}, and is {findOldestCat([tommy, grey, gingy]).age} years old")

# exercise 2

class Dog:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height * 2 }cm high")
    

davids_dog = Dog("Rex", 50)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print(f"Sarah's dog {sarahs_dog.name} is taller")
else: 
    print(f"David's dog {davids_dog.name} is taller")

# exercise 3
class Song:
    def __init__(self, lyrics: [str]):
        self.lyrics = lyrics

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

for lyric in stairway.lyrics:
    print(lyric)

# exercise 4

class Zoo:
    def __init__(self, zoo_name: str):
        self.animals = []
        self.name = zoo_name
        self.sorted_animals = {}
    def add_animal(self, new_animal: str):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        
    def get_animals(self):
        for animal in self.animals:
            print(animal) 
        
    def sell_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
    
    def sort_animals(self):
        sorted_animals = {
            1: sorted(self.animals)[0]
        }
        for animal in sorted(self.animals)[1:]:
            animalKeys = list(sorted_animals.keys())
            if isinstance(sorted_animals[animalKeys[-1]], list):
                if sorted_animals[animalKeys[-1]][0][0] == animal[0]:
                    sorted_animals[animalKeys[-1]] = sorted_animals[animalKeys[-1]].append(animal)
                else:
                    sorted_animals[animalKeys[-1] + 1] = animal
            else:
                if sorted_animals[animalKeys[-1]][0] == animal[0]:
                    sorted_animals[animalKeys[-1]] = [sorted_animals[animalKeys[-1]], animal]
                else:
                    sorted_animals[animalKeys[-1] + 1] = animal
        self.sorted_animals = sorted_animals

    def get_groups(self):
        for value in list(self.sorted_animals.values()):
            print(value)


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Goblin")
ramat_gan_safari.add_animal("Badger")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Chimp")
ramat_gan_safari.add_animal("Eagle")

ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Goblin")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()