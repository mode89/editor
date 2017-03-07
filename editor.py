class Editor:

    def open(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            print(content)
