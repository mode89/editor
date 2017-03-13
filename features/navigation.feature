Feature: Navigation

    Scenario: Move cursor to the beginning when open file
        Given an editor
        When open file "lipsum.txt"
        And refresh editor
        Then view cursor position is (0, 0)
        And screen cursor position is (0, 0)

    Scenario: Move cursor down
        Given an editor
        When open file "lipsum.txt"
        And input "j" 5 times
        And refresh editor
        Then view cursor position is (5, 0)
        And screen cursor position is (5, 0)

    Scenario: Move cursor up
        Given an editor
        When open file "lipsum.txt"
        And set view cursor (5, 0)
        And input "k" 3 times
        And refresh editor
        Then view cursor position is (2, 0)
        And screen cursor position is (2, 0)
