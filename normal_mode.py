import command_mode

class NormalMode:

    def enter(self, editor):
        pass

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
            editor.set_mode(editor.modes[command_mode.CommandMode])
