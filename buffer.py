class Buffer:

    def __init__(self, file_name=None):
        if file_name is None:
            self.lines = [ "\n" ]
        else:
            self.file_name = file_name
            with open(file_name, "r") as f:
                self.lines = []
                for line in f:
                    self.lines.append(line)
