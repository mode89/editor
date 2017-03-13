Feature: Core functionality

    Scenario: Open file
        Given an editor
        When open file "hello.txt"
        Then editor has buffer "hello.txt"
        And current buffer is "hello.txt"
        And screen is identical to file "hello.screen"

    Scenario: Start editor in normal mode
        Given an editor
        Then editor is in normal mode

    Scenario: Execute some code
        Given an editor
        Then editor is running
        When execute "editor.exiting = True"
        Then editor is exiting

    Scenario: Mapping
        Given an editor
        When map 'q' to "editor.exiting = True"
        And input "q"
        And refresh editor
        Then editor is exiting
        When map 'q' to "editor.enter_command_mode()"
        And input "q"
        And refresh editor
        Then editor is in command mode

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
        Then screen is identical to file "open_hello.screen"

    Scenario: Display long file
        Given an editor
        When open file "lipsum.txt"
        And refresh editor
        Then screen is identical to file "long_file.screen"

    Scenario: Display wide file
        Given screen of size (25, 74)
        And an editor
        When open file "lipsum.txt"
        And refresh editor
        Then screen is identical to file "wide_file.screen"

    Scenario: Resize screen
        Given an editor
        When screen change size
        Then refresh editor

    Scenario: Print standard output
        Given an editor
        And editor is in command mode
        When execute command "print(\"Hello, World!\")"
        Then observe "Hello, World!"
