import box

class Grid:
    def __init__(self):
        self.table = []
        for x in range(3):
            row = []
            for y in range(3):
                square = box.Box(x, y)
                row.append(square)
            self.table.append(row)
    
    def __repr__(self):
        s = ''
        for i in range(3):
            for j in range(3):
                s += str(self.table[i][j])
            if i != 2:
                s += '\n'
        return s