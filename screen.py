import curses

class Screen:

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.raw()
        curses.noecho()
        self.stdscr.keypad(True)
        curses.curs_set(1)

    def __del__(self):
        self.release()

    def release(self):
        curses.noraw()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
