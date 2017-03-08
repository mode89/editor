import curses
import curses.ascii

class Editor:

    def run(self):
        try:
            self.screen = curses.initscr()
            curses.raw()
            curses.noecho()
            self.screen.keypad(True)
            curses.curs_set(1)

            while True:
                key = self.screen.getch()
                if key == curses.ascii.ETX: break
        finally:
            curses.noraw()
            self.screen.keypad(False)
            curses.echo()
            curses.endwin()

    def open(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            print(content)
