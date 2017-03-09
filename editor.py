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
            last_row = screen.rows - 1
            screen.write(":", (last_row, 0))

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
