import screen

class Editor:

    def run(self):
        try:
            self.screen = screen.Screen()
            while True:
                key = self.screen.stdscr.getkey()
                if key == "\x03": break
        finally:
            self.screen.release()

    def open(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            print(content)
