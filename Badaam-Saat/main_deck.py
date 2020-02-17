import deck, card, random

class Main_Deck(deck.Deck):
    def generate_cards(self):
        for val in [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']:
            for suit in ['spades', 'diamonds', 'clubs', 'hearts']:
                new_card = card.Card(suit, val)
                self.cards.append(new_card)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def deal_cards(self, players):
        while len(self.cards) != 0:
            for player in players:
                if len(self.cards) != 0:
                    player.deck.cards.append(self.cards[0])
                    self.cards.remove(self.cards[0])
