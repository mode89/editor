from cursor import Cursor

class Screen:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.buffer = [[ord(' ') for x in range(cols)] for y in range(rows)]
        self.cursor = Cursor(0, 0)

    def write(self, text, coord=None):

        if coord is not None:
            self.cursor.row = coord[0]
            self.cursor.col = coord[1]

        for char in text:
            self.buffer[self.cursor.row][self.cursor.col] = ord(char)
            self.cursor.col += 1

    def __getitem__(self, coord):
        return self.buffer[coord[0]][coord[1]]
