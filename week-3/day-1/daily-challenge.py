class Farm:
    animals = {}
    def __init__(self, name):
        self.name = f"{name}'s Farm"
    
    def add_animal(self, name, quantity = 1):
        if name in list(self.animals.keys()):
            self.animals[name] += quantity
        else: 
            self.animals[name] = quantity

    def get_info(self):
        print(self.name)
        for key in list(self.animals.keys()):
            print(key,":", self.animals[key])
        
        print("E-I-E-I-O!")

    def get_animal_types(self) -> [str]:
        animals_list = sorted(list(self.animals.keys()))
        print(animals_list)
        return animals_list

    def get_short_info(self):
        animals = []
        for animal in self.get_animal_types():
            if self.animals[animal] > 1:
                animals.append(animal + "s")
            else:
                animals.append("a " + animal)
        print(f"{self.name} has {", ".join(animals[:-1]) + " and " + animals[-1]}")

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_short_info()
    