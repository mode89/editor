class InputBuffer:

    def __init__(self):
        self.buffer = []

    def put(self, key):
        assert type(key) is int
        self.buffer.append(key)

    def get(self):
        return self.buffer.pop(0)
