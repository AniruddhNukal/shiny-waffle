class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, grid):
        coords = self.check_values(grid)
        grid.table[coords[0]][coords[1]].change_symbol(self.symbol)

    def re_input(self):
        coord = input('> ').strip()
        if len(coord) != 3:
            coord = self.re_input()
        if coord[1] != ' ':
            coord = self.re_input()
        if isinstance(coord, str):
            coord = coord.split()
        if coord[0] not in ['1', '2', '3'] or coord[1] not in ['1', '2', '3']:
            coord = self.re_input()
        return coord
    
    def check_values(self, grid):
        coords = self.re_input()
        for i in range(2):
            coords[i] = int(coords[i]) - 1
        if grid.table[coords[0]][coords[1]].symbol == ' ':
            empty_coord = coords
        else:
            empty_coord = self.check_values(grid)
        return empty_coord