import command_mode

class NormalMode:

    def __init__(self):
        self.mapping = dict()
        self.mapping["j"] = "editor.view.move_down()"
        self.mapping["k"] = "editor.view.move_up()"
        self.mapping["l"] = "editor.view.move_right()"
        self.mapping["h"] = "editor.view.move_left()"
        self.mapping[":"] = "editor.enter_command_mode()"

    def enter(self, editor):
        pass

    def handle(self, editor, key):
        entry = chr(key)
        if entry in self.mapping:
            editor.execute(self.mapping[entry])
