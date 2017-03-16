import input_buffer
import normal_mode
import weakref

class CommandMode:

    def __init__(self, editor):
        self.editor = weakref.ref(editor)

    def enter(self, editor):

        self.buffer = str()
        self.cursor = 0
        last_row = editor.screen.rows - 1
        editor.screen.write(":", (last_row, 0))

    def handle(self, editor, key):
        # update command line buffer
        if key >= 32 and key <= 126:
            self.buffer += chr(key)
            self.cursor += 1
        elif key == input_buffer.KEY_BACKSPACE:
            first = self.buffer[0:self.cursor-1]
            second = self.buffer[self.cursor:-1]
            self.buffer = first + second
            if self.cursor > 0: self.cursor -= 1
        elif key == input_buffer.KEY_ENTER:
            exec(self.buffer)
            editor.set_mode(editor.modes[normal_mode.NormalMode])
            return

    def flush(self):
        screen = self.editor().screen
        last_row = screen.rows - 1
        begin = (last_row, 1)

        # clear command line and write command buffer
        clear = " " * (screen.cols - 1)
        screen.write(clear, begin)
        screen.write(self.buffer, begin)
