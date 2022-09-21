#!/usr/bin/env python3

def mult_two(a: int, b: int) -> int:
    return a*b


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")


def first_word(text: str) -> str:
    return text.split(" ")[0]


print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6

print("Example:")
print(is_acceptable_password("short"))

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")


def number_length(a: int) -> int:
    return len(str(a))

print('Example:')
print(number_length(10))

assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")


def most_frequent(data: list[str]) -> str:
    new = dict.fromkeys(set(data), 0)
    for element in data:
        new[element] += 1 
    return max(new, key=new.get)

print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")


def backward_string(val: str) -> str:
    return val[::-1]

print('Example:')
print(backward_string('val'))

assert backward_string('val') == 'lav'
assert backward_string('') == ''
assert backward_string('ohho') == 'ohho'
assert backward_string('123456789') == '987654321'

print("The mission is done! Click 'Check Solution' to earn rewards!")