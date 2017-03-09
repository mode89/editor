class Screen:

    class Cursor:

        def __init__(self):
            self.row = 0
            self.col = 0

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.buffer = [[ord(' ') for x in range(cols)] for y in range(rows)]
        self.cursor = Screen.Cursor()

    def write(self, text, coord=None):

        if coord is not None:
            self.cursor.row = coord[0]
            self.cursor.col = coord[1]

        for char in text:

            if char == '\n' or self.cursor.col == self.cols:
                self.cursor.row += 1
                self.cursor.col = 0
            else:
                self.buffer[self.cursor.row][self.cursor.col] = ord(char)
                self.cursor.col += 1

    def __getitem__(self, coord):
        return self.buffer[coord[0]][coord[1]]
