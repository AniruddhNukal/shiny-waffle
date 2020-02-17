import grid, player, comp

def setup2p():
    player1 = player.Player('X')
    player2 = player.Player('O')
    matrix = grid.Grid()
    return matrix, player1, player2

def setup1pE():
    player1 = player.Player('X')
    player2 = comp.Comp('O', False)
    matrix = grid.Grid()
    return matrix, player1, player2

def setup1pD():
    player1 = player.Player('X')
    player2 = comp.Comp('O', True)
    matrix = grid.Grid()
    return matrix, player1, player2

def game(matrix, player1, player2):
    main_player = None
    count = 0
    while True:
        main_player = player_switch(main_player, player1, player2)
        print(matrix)
        main_player.make_move(matrix)
        count += 1
        if check_end(matrix):
            game_end(main_player, matrix)
            break
        if count == 9:
            tie(matrix)
            break

def player_switch(player, player1, player2):
    if player:
        if player == player1:
            new_player = player2
        else:
            new_player = player1
    else:
        new_player = player1
    return new_player

def check_end(matrix):
    win = False
    #horizontal check
    for row in matrix.table:
        sym = row[0].symbol
        count = 0
        for box in row:
            if box.symbol == sym and not box.symbol == ' ':
                count += 1
        if count == 3:
            win = True
    #vertical check
    for i in range(3):
        sym = matrix.table[0][i].symbol
        count = 0
        for box in [matrix.table[0][i], matrix.table[1][i], matrix.table[2][i]]:
            if box.symbol == sym and not box.symbol == ' ':
                count += 1
        if count == 3:
            win = True
    #diagonal 1 check
    sym = matrix.table[0][0].symbol
    count = 0
    for i in range(3):
        box = matrix.table[i][i]
        if box.symbol == sym and not box.symbol == ' ':
            count += 1
    if count == 3:
        win = True
    #diagonal 2 check
    sym = matrix.table[0][2].symbol
    count = 0
    for i in range(3):
        box = matrix.table[i][2 - i]
        if box.symbol == sym and not box.symbol == ' ':
            count += 1
    if count == 3:
        win = True
    return win

def game_end(player, matrix):
    print(player.symbol, 'won!')
    print(matrix)

def tie(matrix):
    print('Tie!')
    print(matrix)