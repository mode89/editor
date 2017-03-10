from cursor import Cursor
import itertools

class View:

    def __init__(self):
        self.buffer = None
        self.start = 0

    def flush(self, screen):

        start = self.start
        stop = min(start + screen.rows, len(self.buffer.lines))
        lines = itertools.islice(self.buffer.lines, start, stop)

        screen.cursor = Cursor(0, 0)
        for line in lines:
            screen.write(line)
