from editor import *
import os

@given("an instance of editor")
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
