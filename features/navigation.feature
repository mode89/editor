Feature: Navigation

    Scenario: Move cursor to the beginning when open file
        Given an editor
        When open file "hello.txt"
        And refresh editor
        Then view cursor position is (0, 0)

    Scenario: Move cursor down
        Given an editor
        And buffer is "aaaaa\nbbbbb\nccccc\nddddd\n"
        When input "j" 3 times
        And refresh editor
        Then view cursor position is (3, 0)
        And screen cursor position is (3, 0)

    Scenario: Move cursor up
        Given an editor
        And buffer is "aaaaa\nbbbbb\nccccc\nddddd\n"
        And set view cursor (3, 0)
        When input "k" 2 times
        And refresh editor
        Then view cursor position is (1, 0)
        And screen cursor position is (1, 0)

    Scenario: Move cursor left
        Given an editor
        And buffer is "aaaaa\nbbbbbbbbbbbbbbb\n"
        And set view cursor (1, 10)
        When input "h" 5 times
        And refresh editor
        Then view cursor position is (1, 5)
        And screen cursor position is (1, 5)

    Scenario: Move cursor right
        Given an editor
        And buffer is "aaaaa\nbbbbbbbbbbbbbbb\n"
        And set view cursor (1, 3)
        When input "l" 7 times
        And refresh editor
        Then view cursor position is (1, 10)
        And screen cursor position is (1, 10)

    Scenario: Move cursor right in a long line
        Given screen of size (10, 5)
        And an editor
        And buffer is "aaaaaaaaaaaaaa\n"
        When input "l" 12 times
        And refresh editor
        Then view cursor position is (0, 12)
        And screen cursor position is (2, 2)

    Scenario: Stop at the end of line when move right
        Given an editor
        And buffer is "aaaaaaaaaa\n"
        When input "l" 20 times
        And refresh editor
        Then view cursor position is (0, 9)
        And screen cursor position is (0, 9)

    Scenario: Stop at the beginning of line when move left
        Given an editor
        And buffer is "aaaaa\nbbbbbbbbbb\n"
        And set view cursor (1, 7)
        When input "h" 30 times
        And refresh editor
        Then view cursor position is (1, 0)
        And screen cursor position is (1, 0)

    Scenario: Stop at the first line when move up
        Given an editor
        And buffer is "aaaaa\nbbbbb\nccccc\nddddd\n"
        And set view cursor (3, 3)
        When input "k" 10 times
        And refresh editor
        Then view cursor position is (0, 3)
        And screen cursor position is (0, 3)

    Scenario: Keep view's column when move down
        Given an editor
        And buffer is "aaaaa\nbbbbbbbbbb\nccccccc\nddd\n"
        And set view cursor (1, 8)
        When input "j" 2 times
        And refresh editor
        Then view cursor position is (3, 8)

    Scenario: Bound screen cursor position by the lenght of line
        Given an editor
        And buffer is "aaaaa\nbbbbbbbbbb\nccccccc\nddd\n"
        And set view cursor (1, 8)
        When input "j" 2 times
        And refresh editor
        Then screen cursor position is (3, 2)

    Scenario: When lenght of line is equal to width of screen
        Given screen of size (10, 5)
        And an editor
        And buffer is "aaaaa\nbbbb\n"
        And set view cursor (1, 0)
        When refresh editor
        Then screen cursor position is (1, 0)

    Scenario: When line is empty
        Given screen of size (10, 5)
        And an editor
        And buffer is "\naaa\n"
        And set view cursor (1, 0)
        When refresh editor
        Then screen cursor position is (1, 0)

    Scenario: Constrain view cursor by line lenght when move left
        Given an editor
        And buffer is "aaaaa\n"
        And set view cursor (0, 10)
        When input "h"
        And refresh editor
        Then view cursor position is (0, 3)

    Scenario: Move down by half screen
        Given an editor
        When input CTRL-D
        Then moved down by half screen

    Scenario: Move up by half screen
        Given an editor
        When input CTRL-U
        Then moved up by half screen
