from editor import *
import input_buffer
from screen import *

@given("an editor")
def instance_of_editor(context):
    context.screen = Screen(25, 80)
    context.editor = Editor()
    context.editor.screen = context.screen

@given("editor is in command mode")
def step_impl(context):
    context.editor.mode = Editor.CommandMode(context.editor.screen)

@when("open file \"{file_name}\"")
def open_file(context, file_name):
    context.editor.open(file_name)

@then("see file content")
def see_file_content(context):
    pass

@then("editor is in normal mode")
def mode_of_editor_is(context):
    assert context.editor.mode.__class__ == Editor.NormalMode

@then("editor is in command mode")
def editor_in_command_mode(context):
    assert context.editor.mode.__class__ == Editor.CommandMode

@when("press key {name}")
def step_impl(context, name):
    key = input_buffer.__dict__[name]
    context.editor.input_buffer.put(key)

@when("press {n:d} times key {name}")
def step_impl(context, n, name):
    key = input_buffer.__dict__[name]
    for i in range(n):
        context.editor.input_buffer.put(key)

@when("input \"{text}\"")
def step_impl(context, text):
    text = bytes(text, "utf-8").decode("unicode_escape")
    for char in text:
        context.editor.input_buffer.put(ord(char))

@when("input \"{text}\" {n:d} times")
def step_impl(context, text, n):
    text = bytes(text, "utf-8").decode("unicode_escape")
    for i in range(n):
        for char in text:
            context.editor.input_buffer.put(ord(char))

@when("refresh editor")
def refresh_editor(context):
    context.editor.refresh()

@then("editor is exiting")
def editor_is_exiting(context):
    assert context.editor.exiting == True

@then("command buffer is \"{text}\"")
def step_impl(context, text):
    assert context.editor.mode.buffer == text

@then("command line is \"{text}\"")
def step_impl(context, text):

    screen = context.screen
    row = screen.rows - 1

    # skip trailing spaces
    lastcol = screen.cols - 1
    while screen[row,lastcol] == ord(' '):
        lastcol -= 1

    cmdline = str()
    for col in range(lastcol + 1):
        cmdline += chr(screen[row,col])

    assert cmdline == text

@then("refreshing raises {type_name}(\"{text}\")")
def step_impl(context, type_name, text):
    raised = False
    try:
        context.editor.refresh()
    except eval(type_name) as e:
        raised = True
        assert str(e) == text
    assert raised

@then("cursor position is ({row:d}, {col:d})")
def step_impl(context, row, col):
    assert context.screen.cursor.row == row
    assert context.screen.cursor.col == col

@then("editor has buffer \"{text}\"")
def step_impl(context, text):
    assert text in context.editor.buffers

@then("current buffer is \"{text}\"")
def step_impl(context, text):
    assert context.editor.current_buffer is context.editor.buffers[text]
