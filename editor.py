from input_buffer import *
from screen import *

class Editor:

    class Mode:

        def handle(self, key):
            raise NotImplemented

    class NormalMode(Mode):

        def handle(self, key):
            if key == ord(':'):
                return Editor.CommandMode()
            return self

    class CommandMode(Mode): pass

    def __init__(self):
        self.mode = Editor.NormalMode()
        self.input_buffer = InputBuffer()
        self.exiting = False

    def refresh(self):
        key = self.input_buffer.get()
        if key == 3:
            self.exiting = True
        self.mode = self.mode.handle(key)

    def open(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            self.screen.write(content)
