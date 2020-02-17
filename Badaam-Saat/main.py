import model

print('Welcome to Badaam Saat')
print('How many computer-controlled players?')
comp_count = model.count_check()

print('A single game or a set of games (7 games)?')
mode = model.mode_check()

if mode == 'single':
    model.game_loop(comp_count)
else:
    #future addition
    pass