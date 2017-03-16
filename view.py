import buffer
import itertools

def get_line_length(line):
    return len(line) - 1 # don't count line break

def get_line_height(line, screen):
    length = get_line_length(line)
    if length == 0:
        rows = 1
    else:
        rows = int((length + screen.cols - 1) / screen.cols)
    return rows

class View:

    class Cursor:

        def __init__(self):
            self.line = 0
            self.col = 0

    def __init__(self):
        self.buffer = buffer.Buffer()
        self.top_line = 0
        self.cursor = View.Cursor()

    def move_down(self):
        self.cursor.line = \
            min(self.cursor.line + 1, len(self.buffer.lines) - 1)

    def move_up(self):
        self.cursor.line = max(self.cursor.line - 1, 0)

    def move_right(self):
        line = self.buffer.lines[self.cursor.line]
        self.cursor.col = \
            max(min(self.cursor.col + 1, get_line_length(line) - 1), 0)

    def move_left(self):
        # constrain by line ending
        line = self.buffer.lines[self.cursor.line]
        length = get_line_length(line)
        if self.cursor.col >= length:
            self.cursor.col = length - 1

        self.cursor.col -= 1

        # constrain by line beginning
        if self.cursor.col < 0: self.cursor.col = 0

    def flush(self, screen):

        lines = itertools.islice(
            self.buffer.lines,
            self.top_line,
            len(self.buffer.lines))

        # write lines starting from the begining of the screen
        row = 0
        for line in lines:

            line_len = get_line_length(line)
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
            self.top_line,
            self.cursor.line)

        screen_row = 0
        for line in lines:
            screen_row += get_line_height(line, screen)

        cur_line = self.buffer.lines[self.cursor.line]
        cur_length = get_line_length(cur_line)

        clamped_col = min(cur_length - 1, self.cursor.col) # clamp from right
        clamped_col = max(0, clamped_col) # clamp from left

        screen_col = clamped_col % screen.cols
        screen_row += int(clamped_col / screen.cols)

        screen.cursor.row = screen_row
        screen.cursor.col = screen_col
