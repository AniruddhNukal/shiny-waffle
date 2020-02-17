import deck, random

class Comp:
    def __init__(self, name):
        self.name = name
        self.deck = deck.Deck()
        self.points = 0

    def make_move(self, game):
        decks = [game.heart_deck, game.spade_deck, game.diamond_deck, game.club_deck]
        start = self.check_start(decks)
        playable = self.find_playable_cards(decks, start)
        if len(playable) > 0:
            choice = random.choice(playable)
            self.transfer_card(decks, choice)
            print(self.name, 'played', str(choice), '(' + str(len(self.deck.cards)) + ' cards)')
        else:
            print(self.name, 'couldn\'t play anything and passed', '(' + str(len(self.deck.cards)) + ' cards)')
        return len(self.deck.cards) > 0

    def find_playable_cards(self, decks, start):
        playable = []
        if start:
            for card in self.deck.cards:
                if card.suit == 'hearts' and card.value == '7':
                    playable.append(card)
        else:
            for deck in decks:
                suit = deck.name
                for card in self.deck.cards:
                    if card.suit == suit:
                        if len(deck.cards) == 0:
                            if card.value == '7':
                                playable.append(card)
                        else:
                            if card.numval == deck.cards[0].numval - 1 or card.numval == deck.cards[-1].numval + 1:
                                playable.append(card)
        return playable

    def check_start(self, decks):
        start = True
        for deck in decks:
            if len(deck.cards) > 0:
                start = False
        return start

    def transfer_card(self, decks, card):
        self.deck.cards.remove(card)
        for deck in decks:
            if card.suit == deck.name:
                if card.value == '7':
                    deck.cards.append(card)
                elif card.numval > 7:
                    deck.cards.append(card)
                else:
                    deck.cards.insert(0, card)
