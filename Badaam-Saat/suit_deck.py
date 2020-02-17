import deck

class Suit_Deck(deck.Deck):
    def __init__(self, name):
        super().__init__()
        self.name = name
