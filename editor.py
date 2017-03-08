from input_buffer import *

class Editor:

    class Mode: pass

    class NormalMode(Mode): pass

    def __init__(self):
        self.mode = Editor.NormalMode()
        self.input_buffer = InputBuffer()
        self.exiting = False

    def refresh(self):
        key = self.input_buffer.get()
        if key == 3:
            self.exiting = True

    def open(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            print(content)
