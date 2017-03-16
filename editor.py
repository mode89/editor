from buffer import *
from input_buffer import *
from screen import *
from view import *
import command_mode
import normal_mode

class Editor:

    def __init__(self):
        self.view = View(self)
        self.buffers = dict()
        self.input_buffer = InputBuffer()
        self.exiting = False

        self.modes = dict()
        self.modes[normal_mode.NormalMode] = \
            normal_mode.NormalMode(self)
        self.modes[command_mode.CommandMode] = command_mode.CommandMode()
        self.set_mode(self.modes[normal_mode.NormalMode])

    def set_mode(self, mode):
        self.mode = mode
        self.mode.enter(self)

    def execute(self, command):
        scope = { "editor": self }
        exec(command, scope)

    def refresh(self):
        while not self.input_buffer.empty():
            key = self.input_buffer.get()
            if key == 3:
                self.exiting = True
            self.mode.handle(self, key)
        self.mode.flush()

    def open(self, file_name):
        new_buffer = Buffer(file_name)
        self.buffers[file_name] = new_buffer
        self.view.buffer = new_buffer
        self.view.flush()

    def enter_command_mode(self):
        self.set_mode(self.modes[command_mode.CommandMode])
