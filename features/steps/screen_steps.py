from screen import *

@given("a screen")
def create_screen(context):
    context.screen = Screen(25, 80)

@when("write \"{text}\" to screen")
def write_to_screen(context, text):
    context.screen.write(text)

@then("write screen to file \"{filename}\"")
def screen_dump(context, filename):
    with open(filename, "wb") as f:
        for row in context.screen.buffer:
            for char in row:
                f.write(chr(char).encode())
            f.write('\n'.encode())

@then("screen is identical to file \"{filename}\"")
def screen_compare(context, filename):
    with open(filename, "rb") as f:
        for row in context.screen.buffer:
            for char in row:
                assert f.read(1) == chr(char).encode()
            assert f.read(1) == '\n'.encode()
