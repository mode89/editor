Feature: Core functionality

    Scenario: Open file
        Given an instance of editor
        When open lipsum.txt
        Then see file content

    Scenario: Start editor in normal mode
        Given an instance of editor
        Then editor is in normal mode
