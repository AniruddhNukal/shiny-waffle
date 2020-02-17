import deck, model

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = deck.Deck()
        self.points = 0
        
    def make_move(self, game):
        decks = [game.heart_deck, game.spade_deck, game.diamond_deck, game.club_deck]
        start = self.check_start(decks)
        playable = self.find_playable_cards(decks, start)
        self.show_cards(playable)
        card = self.choose_move(playable)
        if card:
            self.transfer_card(decks, card)
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

    def show_cards(self, playable):
        print('Playable cards:')
        for card in self.deck.cards:
            if card not in playable:
                print(card)
        for i in range(len(playable)):
            print('[' + str(i + 1) + '] ' + str(playable[i]))

    def choose_move(self, playable):
        index = self.get_index(playable)
        print('--------------------------------------------------')
        if index:
            return playable[index - 1]
        else:
            return None

    def get_index(self, playable):
        if len(playable) == 0:
            input('No playable options, press enter to pass')
            return None
        index = input('Number: >')
        if not index.isdigit():
            index = self.get_index(playable)
        if isinstance(index, str):
            index = int(index)
        if index > len(playable) or index <= 0:
            index = self.get_index(playable)
        return index

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
