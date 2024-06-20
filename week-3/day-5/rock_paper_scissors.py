from game import Game
def get_user_menu_choice():
    menu_choice = input("MENU:\n(g) To start a new game enter 'g'\n(s) To show the score enter 's'\n(q) To quit enter 'q'\n:")
    return menu_choice
            

def print_results(results):
    print(f"SCORE:\nWins: {results['wins']}\nLosses: {results['losses']}\nDraws: {results['draws']}")


def main():
    menu_choice = None
    wins = 0
    draws = 0
    losses = 0
    while menu_choice != 'q':
        if menu_choice == 'g':
            game = Game()    
            result = game.play()
            match result:
                case 'drew':
                    draws = draws + 1
                case 'won':
                    wins = wins + 1
                case 'lost':
                    losses = losses + 1
        elif menu_choice == 's':
            print_results({"wins": wins, "losses": losses, "draws": draws})
        
        menu_choice = get_user_menu_choice()
        if menu_choice == 'q':
            print_results({"wins": wins, "losses": losses, "draws": draws})

main()