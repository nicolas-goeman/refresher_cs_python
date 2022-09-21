from dev.checkio import *

def test_mult_two() -> None:
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0

def test_first_word() -> None:
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("greeting from CheckiO Planet") == "greeting"
    assert first_word("hi") == "hi"

def test_is_acceptable_password() -> None:
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False

def test_number_length() -> None:
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2

def test_most_frequent() -> None:
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

def test_backward_string() -> None:
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
