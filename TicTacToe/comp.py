import player, random

class Comp(player.Player):
    def __init__(self, symbol, diff):
        super().__init__(symbol)
        self.diff = diff
    
    def make_move(self, grid):
        if not self.diff:
            arr = self.random_check(grid)
        else:
            arr = self.intel(grid)
        grid.table[arr[0]][arr[1]].change_symbol(self.symbol)
        print('>', str(arr[0] + 1), str(arr[1] + 1))

    def random_check(self, grid):
        list = [random.randint(0, 2), random.randint(0, 2)]
        if grid.table[list[0]][list[1]].symbol != ' ':
            list = self.random_check(grid)
        return list
    
    def intel(self, grid):
        #horizontal
        for row in grid.table:
            sym_list = []
            for box in row:
                sym_list.append(box.symbol)
            sym_count = self.composition_check(sym_list)
            if sym_count[0] == 2 and sym_count[2] == 1:
                for box in row:
                    if box.symbol == ' ':
                        return [box.x, box.y]
            elif sym_count[1] == 2 and sym_count[2] == 1:
                for box in row:
                    if box.symbol == ' ':
                        return [box.x, box.y]
        #vertical
        for i in range(3):
            sym_list = []
            for j in range(3):
                sym_list.append(grid.table[i][j].symbol)
            sym_count = self.composition_check(sym_list)
            if sym_count[0] == 2 and sym_count[2] == 1:
                for j in range(3):
                    if grid.table[i][j].symbol == ' ':
                        return [j, i]
            elif sym_count[1] == 2 and sym_count[2] == 1:
                for j in range(3):
                    if grid.table[i][j].symbol == ' ':
                        return [j, i]
        #diagonal 1
        sym_list = []
        for i in range(3):
            sym_list.append(grid.table[i][i].symbol)
        sym_count = self.composition_check(sym_list)
        if sym_count[0] == 2 and sym_count[2] == 1:
            for i in range(3):
                if grid.table[i][i].symbol == ' ':
                    return [i, i]
        elif sym_count[1] == 2 and sym_count[2] == 1:
            for i in range(3):
                if grid.table[i][i].symbol == ' ':
                    return [i, i]
        #diagonal 2
        sym_list = []
        for i in range(3):
            sym_list.append(grid.table[i][2 - i].symbol)
        sym_count = self.composition_check(sym_list)
        if sym_count[0] == 2 and sym_count[2] == 1:
            for i in range(3):
                if grid.table[i][2 - i].symbol == ' ':
                    return [i, 2 - i]
        elif sym_count[1] == 2 and sym_count[2] == 1:
            for i in range(3):
                if grid.table[i][2 - i].symbol == ' ':
                    return [i, 2 - i]
        return self.random_check(grid)
    
    def composition_check(self, list):
        x_count = 0
        o_count = 0
        blank_count = 0
        for i in list:
            if i == 'X':
                x_count += 1
            elif i == 'O':
                o_count += 1
            else:
                blank_count += 1
        return (x_count, o_count, blank_count)