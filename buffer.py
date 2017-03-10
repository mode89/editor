class Buffer:

    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name, "r") as f:
            self.lines = []
            for line in f:
                self.lines.append(line)
