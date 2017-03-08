Feature: Abstraction of screen

    Scenario: Write to screen
        Given a screen
        When write "Hello, World!" to screen
        Then content of screen is "Hello, World!"
