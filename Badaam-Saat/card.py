class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if self.value == 'A':
            self.numval = 1
        elif self.value == 'K':
            self.numval = 13
        elif self.value == 'Q':
            self.numval = 12
        elif self.value == 'J':
            self.numval = 11
        else:
            self.numval = int(self.value)

    def __repr__(self):
        return '(' + self.value + ' of ' + self.suit + ')'
