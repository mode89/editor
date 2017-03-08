from editor import *

@given("an editor")
def instance_of_editor(context):
    context.editor = Editor()

@when("open {file_name}")
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

@when("pressed '\\x{code}'")
def pressed_key_hex(context, code):
    context.editor.input_buffer.put(int(code, 16))

@when("pressed '{char}'")
def pressed_key_char(context, char):
    context.editor.input_buffer.put(ord(char))

@when("refresh editor")
def refresh_editor(context):
    context.editor.refresh()

@then("editor is exiting")
def editor_is_exiting(context):
    assert context.editor.exiting == True
