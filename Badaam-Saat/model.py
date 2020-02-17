import deck, player, main_deck, suit_deck, comp, game
import os

def setup(comp_count):
    deal_deck = main_deck.Main_Deck()
    heart_deck = suit_deck.Suit_Deck('hearts')
    spade_deck = suit_deck.Suit_Deck('spades')
    diamond_deck = suit_deck.Suit_Deck('diamonds')
    club_deck = suit_deck.Suit_Deck('clubs')
    players = []
    players.append(player.Player(input('Name: > ')))
    for i in range(comp_count):
        players.append(comp.Comp('Comp' + str(i + 1)))
    stage = game.Game(deal_deck, [heart_deck, spade_deck, diamond_deck, club_deck], players)
    stage.deal_deck.generate_cards()
    stage.deal_deck.shuffle_cards()
    stage.deal_deck.deal_cards(stage.players)
    return stage

def turn(stage):
    show_game(stage)
    code = True
    for player in stage.players:
        if code:
            code = player.make_move(stage)
    if not code:
        stage = game_over(stage)
    os.system('clear')
    return stage, code

def game_over(stage):
    for player in stage.players:
        points = 0
        for card in player.deck.cards:
            points += card.numval
        player.points += points
    return stage

def count_check():
    count = input('> ')
    if not count.isdigit():
        print('Please enter a number')
        count = count_check()
    return int(count)

def mode_check():
    mode = input('(single/set)> ').lower()
    if mode not in ['single', 'set']:
        print('Please enter "single" or "set"')
        mode = mode_check()
    return mode

def game_loop(player_count):
    stage = setup(player_count)
    code = True
    while code:
        stage, code = turn(stage)
    lowest = None
    for player in stage.players:
        if not lowest:
            lowest = player
        else:
            if player.points < lowest.points:
                lowest = player
    print(lowest.name, 'is the winner')
    for i in range(4):
        print(' ')

def show_game(stage):
    lines = arrange_game(stage)
    print('Played cards', '    Hearts        Spades       Diamonds       Clubs    ')
    for line in lines:
        print(line)

def arrange_game(stage):
    decks = [stage.heart_deck, stage.spade_deck, stage.diamond_deck, stage.club_deck]
    lines = []
    end = find_longest(stage)
    for i in range(end):
        line = ''
        if i < len(decks[0].cards):
            cardstr = str(decks[0].cards[i])
            if decks[0].cards[i].numval != 10:
                cardstr += ' '
        else:
            cardstr = '              '
        line += cardstr
        if i < len(decks[1].cards):
            cardstr = str(decks[1].cards[i])
            if decks[1].cards[i].numval != 10:
                cardstr += ' '
        else:
            cardstr = '              '
        line += cardstr
        if i < len(decks[2].cards):
            cardstr = str(decks[2].cards[i])
            if decks[2].cards[i].numval != 10:
                cardstr += ' '
        else:
            cardstr = '                '
        line += cardstr
        if i < len(decks[3].cards):
            cardstr = str(decks[3].cards[i])
            if decks[3].cards[i].numval != 10:
                cardstr += ' '
        else:
            cardstr = '             '
        line += cardstr
        lines.append(line)
    return lines

def find_longest(stage):
    decks = [stage.heart_deck, stage.spade_deck, stage.diamond_deck, stage.club_deck]
    longest = None
    for deck in decks:
        if not longest:
            longest = deck
        else:
            if len(deck.cards) > len(longest.cards):
                longest = deck
    return len(longest.cards)