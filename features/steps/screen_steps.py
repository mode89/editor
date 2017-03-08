from screen import *

@given("a screen")
def create_screen(context):
    context.screen = Screen()

@when("write \"{text}\" to screen")
def write_to_screen(context, text):
    context.screen.write(text)

@then("content of screen is \"{text}\"")
def content_of_screen_is(context, text):
    assert context.screen.content() == text
