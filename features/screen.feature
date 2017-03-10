Feature: Abstraction of screen

    Scenario: Write to screen
        Given a screen
        When write "Hello, World!" to screen
        Then screen is identical to file "write_to_screen.screen"
