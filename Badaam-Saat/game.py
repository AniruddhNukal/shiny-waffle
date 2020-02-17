class Game:
    def __init__(self, deal_deck, suit_decks, players):
        self.deal_deck = deal_deck
        self.heart_deck = suit_decks[0]
        self.spade_deck = suit_decks[1]
        self.diamond_deck = suit_decks[2]
        self.club_deck = suit_decks[3]
        self.players = players
