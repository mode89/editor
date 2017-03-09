from screen import *

@given("a screen")
def create_screen(context):
    context.screen = Screen(25, 80)

@when("write \"{text}\" to screen")
def write_to_screen(context, text):
    context.screen.write(text)

@then("content of screen is \"{text}\"")
def content_of_screen_is(context, text):
    text = bytes(text, "utf-8").decode("unicode_escape")
    row = 0
    col = 0
    for char in text:
        if char == '\n':
            row += 1
            col = 0
        else:
            assert char == chr(context.screen[row, col])
            col += 1
