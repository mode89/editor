class Screen:

    def write(self, text):
        self.buffer = text

    def content(self):
        return self.buffer
