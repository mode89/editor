KEY_BACKSPACE = 0x107

class InputBuffer:

    def __init__(self):
        self.buffer = []

    def put(self, key):
        assert type(key) is int
        self.buffer.append(key)

    def get(self):
        return self.buffer.pop(0)

    def empty(self):
        return len(self.buffer) == 0
