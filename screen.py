class Screen:

    def __init__(self):
        self.buffer = str()

    def write(self, text):
        self.buffer += text

    def content(self):
        return self.buffer
