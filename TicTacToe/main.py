import model

def runtime():
    print('How many players? (1 or 2)')
    players = player_check()
    if players == 1:
        print('What difficulty? (Easy or Hard)')
        difficulty = diff_check()
        if difficulty == 'easy':
            matrix, p1, p2 = model.setup1pE()
        else:
            matrix, p1, p2 = model.setup1pD()
    else:
        matrix, p1, p2 = model.setup2p()
    model.game(matrix, p1, p2)

def player_check():
    num = input()
    if num not in ['1', '2']:
        num = player_check()
    if isinstance(num, str):
        num = int(num)
    return num

def diff_check():
    diff = input()
    if diff.lower() not in ['easy', 'hard']:
        diff = diff_check()
    return diff

if __name__ == '__main__':
    runtime()