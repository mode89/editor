Feature: Core functionality

    Scenario: Open file
        Given an editor
        When open lipsum.txt
        Then see file content

    Scenario: Start editor in normal mode
        Given an editor
        Then editor is in normal mode

    Scenario: Exiting
        Given an editor
        When pressed '\x03'
        Then editor is exiting
