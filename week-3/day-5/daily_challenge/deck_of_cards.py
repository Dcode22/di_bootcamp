import random
class Card:
    suit = ''
    value = ''
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value}{self.suit}"
    def __repr__(self):
        return self.__str__()

class Deck:
    cards = []
    def __init__(self):
        for value in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            for suit in ['spades', 'clubs', 'diamonds', 'hearts']:
                self.cards.append(Card(suit, value))
        print(self.cards)

    def shuffle(self):
        if len(self.cards):
            random.shuffle(self.cards)
            print(self.cards)
        else:
            raise Exception('Card missing')
        
    def deal(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        print(card)
        print(self.cards)
        return card


new_deck = Deck()

new_deck.shuffle()

new_deck.deal()