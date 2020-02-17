class Box:
    def __init__(self, x, y):
        self.symbol = ' '
        self.x = x
        self.y = y

    def __repr__(self):
        return '[' + self.symbol + ']'
    
    def change_symbol(self, symbol):
        self.symbol = symbol