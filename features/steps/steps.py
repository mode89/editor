from screen import *
import command_mode
import editor
import input_buffer
import normal_mode

@given("screen of size ({rows:d}, {cols:d})")
def step_impl(context, rows, cols):
    context.screen = Screen(rows, cols)

@given("an editor")
def instance_of_editor(context):
    if not hasattr(context, "screen"):
        context.screen = Screen(25, 80)
    context.editor = editor.Editor()
    context.editor.screen = context.screen

@given("editor is in command mode")
def step_impl(context):
    context.editor.set_mode(context.editor.modes[command_mode.CommandMode])

@given("open file \"{file_name}\"")
def step_impl(context, file_name):
    context.editor.open(file_name)

@when("open file \"{file_name}\"")
def open_file(context, file_name):
    context.editor.open(file_name)

@then("see file content")
def see_file_content(context):
    pass

@then("editor is in normal mode")
def mode_of_editor_is(context):
    assert context.editor.mode is \
        context.editor.modes[normal_mode.NormalMode]

@then("editor is in command mode")
def editor_in_command_mode(context):
    assert context.editor.mode is \
        context.editor.modes[command_mode.CommandMode]

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

@then("editor is running")
def step_impl(context):
    assert context.editor.exiting == False

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

@then("screen cursor position is ({row:d}, {col:d})")
def step_impl(context, row, col):
    assert context.screen.cursor.row == row
    assert context.screen.cursor.col == col

@then("view cursor position is ({line:d}, {col:d})")
def step_impl(context, line, col):
    assert context.editor.view.cursor.line == line
    assert context.editor.view.cursor.col == col

@given("set view cursor ({line:d}, {col:d})")
def step_impl(context, line, col):
    context.editor.view.cursor.line = line
    context.editor.view.cursor.col = col

@then("editor has buffer \"{text}\"")
def step_impl(context, text):
    assert text in context.editor.buffers

@then("current buffer is \"{text}\"")
def step_impl(context, text):
    assert context.editor.view.buffer is context.editor.buffers[text]

@when("map '{text}' to \"{code}\"")
def step_impl(context, text, code):
    context.editor.modes[normal_mode.NormalMode].mapping[text] = code

@when("execute \"{command}\"")
def step_impl(context, command):
    context.editor.execute(command)

@given("buffer is \"{text}\"")
def step_impl(context, text):
    text = bytes(text, "utf-8").decode("unicode_escape")
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] += '\n'
    context.editor.view.buffer.lines = lines

@given("a screen")
def create_screen(context):
    context.screen = Screen(25, 80)

@when("clear screen")
def step_impl(context):
    context.screen.clear()

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

@then("screen text at ({row:d}, {col:d}) is \"{text}\"")
def step_impl(context, row, col, text):
    for i in range(len(text)):
        assert context.screen[row, col+i] == ord(text[i])
