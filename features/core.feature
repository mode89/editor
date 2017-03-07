Feature: Core functionality

    Scenario: Open file
        Given an instance of editor
        When open lipsum.txt
        Then see file content
