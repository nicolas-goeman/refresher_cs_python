#!/usr/bin/env python3

def mult_two(a: int, b: int) -> int:
    return a*b


def first_word(text: str) -> str:
    return text.split(" ")[0]


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


def number_length(a: int) -> int:
    return len(str(a))


def most_frequent(data: list[str]) -> str:
    new = dict.fromkeys(set(data), 0)
    for element in data:
        new[element] += 1 
    return max(new, key=new.get)


def backward_string(val: str) -> str:
    return val[::-1]

def check_coverage() -> None:
    pass