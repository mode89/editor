from input_buffer import *
from screen import *

class Editor:

    class Mode:

        def handle(self, editor, key):
            raise NotImplemented

    class NormalMode(Mode):

        def handle(self, editor, key):
            if key == ord(':'):
                return Editor.CommandMode(editor.screen)
            return self

    class CommandMode(Mode):

        def __init__(self, screen):
            self.buffer = str()
            last_row = screen.rows - 1
            screen.write(":", (last_row, 0))

        def handle(self, editor, key):

            # update command line buffer
            self.buffer += chr(key)

            # display buffer on the screen
            screen = editor.screen
            last_row = screen.rows - 1
            screen.write(self.buffer, (last_row, 1))

            return self

    def __init__(self):
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
            self.screen.write(content)
