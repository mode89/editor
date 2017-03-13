import buffer
from copy import deepcopy
from cursor import Cursor
import itertools

class View:

    def __init__(self):
        self.buffer = buffer.Buffer()
        self.start = 0
        self.cursor = Cursor(0, 0)

    def flush(self, screen):

        lines = itertools.islice(
            self.buffer.lines,
            self.start,
            len(self.buffer.lines))

        # write lines starting from the begining of the screen
        row = 0
        for line in lines:

            line_len = len(line) - 1 # don't count line break
            line_rows = int(line_len / screen.cols) + 1

            for i in range(line_rows):
                start = i * screen.cols
                stop = min(start + screen.cols, line_len)
                screen.write(line[start:stop], (row, 0))
                row += 1
                if row >= screen.rows: break # reach bottom of screen

            if row >= screen.rows: break # reach bottom of screen

        screen.cursor = deepcopy(self.cursor)
