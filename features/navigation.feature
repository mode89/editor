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

    Scenario: Move cursor left
        Given an editor
        When open file "lipsum.txt"
        And set view cursor (5, 10)
        And input "h" 5 times
        And refresh editor
        Then view cursor position is (5, 5)
        And screen cursor position is (5, 5)

    Scenario: Move cursor right
        Given an editor
        When open file "lipsum.txt"
        And input "l" 10 times
        And refresh editor
        Then view cursor position is (0, 10)
        And screen cursor position is (0, 10)

    Scenario: Move cursor right in a long line
        Given screen of size (43, 25)
        And an editor
        When open file "lipsum.txt"
        And input "l" 28 times
        And refresh editor
        Then view cursor position is (0, 28)
        And screen cursor position is (1, 3)

    Scenario: Stop at the end of line when move right
        Given screen of size (43, 25)
        And an editor
        When open file "lipsum.txt"
        And input "l" 80 times
        And refresh editor
        Then view cursor position is (0, 67)
        And screen cursor position is (2, 17)

    Scenario: Stop at the beginning of line when move left
        Given screen of size (43, 25)
        And an editor
        When open file "lipsum.txt"
        And set view cursor (3, 60)
        And input "h" 100 times
        And refresh editor
        Then view cursor position is (3, 0)
        And screen cursor position is (9, 0)

    Scenario: Stop at the first line when move up
        Given screen of size (43, 25)
        And an editor
        When open file "lipsum.txt"
        And set view cursor (5, 55)
        And input "k" 100 times
        And refresh editor
        Then view cursor position is (0, 55)
        And screen cursor position is (2, 5)

    Scenario: Keep view's column when move down
        Given screen of size (43, 25)
        And an editor
        When open file "lipsum.txt"
        And set view cursor (0, 60)
        And input "j"
        And refresh editor
        Then view cursor position is (1, 60)
        And screen cursor position is (5, 10)

    Scenario: Bound screen cursor position by the lenght of line
        Given screen of size (43, 25)
        And an editor
        When open file "lipsum.txt"
        And set view cursor (2, 100)
        And refresh editor
        Then view cursor position is (2, 100)
        And screen cursor position is (8, 20)

    Scenario: When lenght of line is equal to width of screen
        Given screen of size (10, 5)
        And an editor
        And buffer is "aaaaa\nbbbb\n"
        When set view cursor (1, 0)
        And refresh editor
        Then screen cursor position is (1, 0)

    Scenario: When line is empty
        Given screen of size (10, 5)
        And an editor
        And buffer is "\naaa\n"
        When set view cursor (1, 0)
        And refresh editor
        Then screen cursor position is (1, 0)
