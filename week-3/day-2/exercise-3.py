from exercises_xp import Dog, blue, rees
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained:bool):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
        print(args)
        print(f"{self.name} plays with {args[0].name if len(args) < 2 else (", ".join([arg.name for arg in args][:-1]) + " and " + args[-1].name)}.")

    def do_trick(self):
        trick_playbook = [f"{self.name} does a barrel roll.", f"{self.name} stands on his back legs.", f"{self.name} shakes your hand.", f"{self.name} plays dead."]
        print(trick_playbook[random.randint(0, len(trick_playbook) - 1)])

layla = PetDog("Layla", 3, 60, True)

layla.play(blue, rees)
layla.do_trick()
