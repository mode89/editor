Feature: Navigation

    Scenario: Move cursor to the beginning when open file
        Given an editor
        When open file "lipsum.txt"
        And refresh editor
        Then view cursor position is (0, 0)
        And screen cursor position is (0, 0)
