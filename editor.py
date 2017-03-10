from buffer import *
from input_buffer import *
from screen import *

class Editor:

    class NormalMode:

        def handle(self, editor, key):
            if key == ord('j'):
                editor.screen.cursor.row += 1
            if key == ord('k'):
                editor.screen.cursor.row -= 1
            if key == ord('l'):
                editor.screen.cursor.col += 1
            if key == ord('h'):
                editor.screen.cursor.col -= 1
            if key == ord(':'):
                return Editor.CommandMode(editor.screen)
            return self

    class CommandMode:

        def __init__(self, screen):
            self.buffer = str()
            self.cursor = 0
            last_row = screen.rows - 1
            screen.write(":", (last_row, 0))

        def handle(self, editor, key):

            screen = editor.screen
            last_row = screen.rows - 1
            begin = (last_row, 1)

            # update command line buffer
            if key >= 32 and key <= 126:
                self.buffer += chr(key)
                self.cursor += 1
            elif key == KEY_BACKSPACE:
                first = self.buffer[0:self.cursor-1]
                second = self.buffer[self.cursor:-1]
                self.buffer = first + second
                if self.cursor > 0: self.cursor -= 1
            elif key == KEY_ENTER:
                exec(self.buffer)
                return Editor.NormalMode()

            # clear command line and write command buffer
            clear = " " * (screen.cols - 1)
            screen.write(clear, begin)
            screen.write(self.buffer, begin)

            return self

    def __init__(self):
        self.buffers = dict()
        self.mode = Editor.NormalMode()
        self.input_buffer = InputBuffer()
        self.exiting = False

    def refresh(self):
        while not self.input_buffer.empty():
            key = self.input_buffer.get()
            if key == 3:
                self.exiting = True
            self.mode = self.mode.handle(self, key)

    def open(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            self.buffers[file_name] = Buffer(file_name)
            self.screen.write(content, (0, 0))
            self.screen.cursor.row = 0
            self.screen.cursor.col = 0
