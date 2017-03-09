Feature: Core functionality

    Scenario: Open file
        Given an editor
        When open file "hello.txt"
        Then content of screen is "Hello, World!\n"

    Scenario: Start editor in normal mode
        Given an editor
        Then editor is in normal mode

    Scenario: Exiting
        Given an editor
        When input "\x03"
        And refresh editor
        Then editor is exiting

    Scenario: Switching to command mode
        Given an editor
        When input ":"
        And refresh editor
        Then editor is in command mode
        Then command line is ":"

    Scenario: Input command
        Given an editor
        And editor is in command mode
        When input "some command"
        And refresh editor
        Then command buffer is "some command"
        And command line is ":some command"

    Scenario: Backspace input command
        Given an editor
        And editor is in command mode
        When input "some command"
        And press 5 times key KEY_BACKSPACE
        And refresh editor
        Then command buffer is "some co"
        Then command line is ":some co"

    Scenario: Execute command
        Given an editor
        And editor is in command mode
        When input "raise RuntimeError(\"Hello, World!\")"
        And press key KEY_ENTER
        Then refreshing raises RuntimeError("Hello, World!")

    Scenario: Open file from command mode
        Given an editor
        And editor is in command mode
        When input "editor.open(\"hello.txt\")"
        And press key KEY_ENTER
        And refresh editor
        Then content of screen is "Hello, World!"
