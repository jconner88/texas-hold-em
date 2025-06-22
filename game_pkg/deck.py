import random
values = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7:7, 8:8, 9:9, 10:10,"J": 11, "Q": 12, "K": 13, "A": 14}
suits = {"\u2663":"Clubs" ,  "\u2665" : "Hearts", "\u2666" : "Diamonds" , "\u2660":"Spades"}


class Card:
    def __init__(self, suit, values):
        self.suit = suit
        self.value = values

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for val in values:
                self.cards.append(Card(suit, val))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
            return self.cards.pop()



class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.deal_card())
        return self
    
    def show_hand(self):
        for card in self.hand:
            return card.show()

class Opponent:
    def __init__(self, name):
        self.name = name
        self.hand =[]

    def draw(self, deck):
        self.hand.append(deck.deal_card())
        return self
    
    def show_hand(self):
        hidden = True
        while hidden:
            for card in self.hand:
                print("CARD")
                return

# Driver Code
# deck = Deck()
# deck.shuffle()
# deck.show()


