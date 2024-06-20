import random
class Game:
    def get_user_choice(self):
        user_choice = input("Enter 'r' for Rock, 'p' for Paper or 's' for Scissors: ")
        if user_choice not in ['r', 'p', 's']:
            print("INVALID CHOICE")
            self.get_user_choice()
        else:
            match user_choice:
                case 'r':
                    return 'rock'
                case 'p':
                    return 'paper'
                case 's':
                    return 'scissors'

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def get_game_result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'drew'
        else:
            match user_choice:
                case 'rock':
                    match computer_choice:
                        case 'paper':
                            return 'lost'
                        case 'scissors':
                            return 'won'
                case 'paper':
                    match computer_choice:
                        case 'scissors':
                            return 'lost'
                        case 'rock':
                            return 'won'
                case 'scissors':
                    match computer_choice:
                        case 'rock':
                            return 'lost'
                        case 'paper':
                            return 'won'
    def play(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        result = self.get_game_result(user_choice, computer_choice)
        print(f"You chose {user_choice}, the computer chose {computer_choice}, you {result}!")
        return result