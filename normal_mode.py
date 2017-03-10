import command_mode

class NormalMode:

    def __init__(self):
        self.mapping = dict()
        self.mapping["j"] = "editor.screen.cursor.row += 1"
        self.mapping["k"] = "editor.screen.cursor.row -= 1"
        self.mapping["l"] = "editor.screen.cursor.col += 1"
        self.mapping["h"] = "editor.screen.cursor.col -= 1"
        self.mapping[":"] = "editor.enter_command_mode()"

    def enter(self, editor):
        pass

    def handle(self, editor, key):
        entry = chr(key)
        if entry in self.mapping:
            editor.execute(self.mapping[entry])
