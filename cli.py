import curses
from editor import *
from screen import *

def wrappred_main(stdscr):
    curses.use_default_colors()
    curses.noecho()
    curses.cbreak()
    curses.raw()
    stdscr.keypad(True)
    stdscr.clearok(False)
    stdscr.immedok(False)

    editor = Editor()
    rows, cols = stdscr.getmaxyx()
    screen = Screen(rows, cols)
    editor.screen = screen

    while not editor.exiting:

        for row in range(screen.rows):
            # curses throws error when addch() writes to the last column
            lastcol = screen.cols - 1
            for col in range(lastcol):
                stdscr.addch(row, col, screen[row,col])
            stdscr.insch(row, lastcol, screen[row,lastcol])
        stdscr.move(screen.cursor.row, screen.cursor.col)

        editor.input_buffer.put(stdscr.getch())
        editor.refresh()

def main():
    curses.wrapper(wrappred_main)

if __name__ == "__main__":
    main()
