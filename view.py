import buffer
import itertools

def get_line_rows(line, screen):
    length = len(line) - 1 # don't count line break
    rows = int((length + screen.cols - 1) / screen.cols)
    return rows

class View:

    class Cursor:

        def __init__(self):
            self.line = 0
            self.col = 0

    def __init__(self):
        self.buffer = buffer.Buffer()
        self.start = 0
        self.cursor = View.Cursor()

    def move_down(self):
        self.cursor.line = \
            min(self.cursor.line + 1, len(self.buffer.lines) - 1)

    def move_up(self):
        self.cursor.line = max(self.cursor.line - 1, 0)

    def move_right(self):
        line = self.buffer.lines[self.cursor.line]
        self.cursor.col = \
            max(min(self.cursor.col + 1, len(line) - 2), 0)

    def move_left(self):
        line = self.buffer.lines[self.cursor.line]
        self.cursor.col = min(max(self.cursor.col - 1, 0), len(line) - 1)

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

        self.update_cursor(screen)

    def update_cursor(self, screen):

        lines = itertools.islice(
            self.buffer.lines,
            self.start,
            self.cursor.line)

        screen_row = 0
        for line in lines:
            screen_row += get_line_rows(line, screen)

        cur_line = self.buffer.lines[self.cursor.line]
        cur_length = len(cur_line) - 1 # don't count line break

        clamped_col = min(cur_length - 1, self.cursor.col) # clamp from right
        clamped_col = max(0, clamped_col) # clamp from left

        screen_col = clamped_col % screen.cols
        screen_row += int(clamped_col / screen.cols)

        screen.cursor.row = screen_row
        screen.cursor.col = screen_col
