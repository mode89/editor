Feature: Abstraction of screen

    Scenario: Write to screen
        Given a screen
        When write "Hello, World!" to screen
        Then screen is identical to file "write_to_screen.screen"

    Scenario: Clear screen
        Given a screen
        When write "Hello, World!" to screen
        And clear screen
        Then screen is identical to file "clear.screen"
