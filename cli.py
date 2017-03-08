import curses
from editor import *

def wrappred_main(screen):
    curses.use_default_colors()
    curses.noecho()
    curses.cbreak()
    curses.raw()
    screen.keypad(True)

    editor = Editor()
    while not editor.exiting:
        screen.clear()
        screen.addstr(editor.screen.content())
        editor.input_buffer.put(screen.getch())
        editor.refresh()

def main():
    curses.wrapper(wrappred_main)

if __name__ == "__main__":
    main()
