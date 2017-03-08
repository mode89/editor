class Editor:

    class Mode: pass

    class NormalMode(Mode): pass

    def __init__(self):
        self.mode = Editor.NormalMode()

    def open(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            print(content)
