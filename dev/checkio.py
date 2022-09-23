"""
This is a module that contains multiple simple functions.
"""

def mult_two(int_a: int, int_b: int) -> int:
    """Multiply two integers

    Args:
        int_a (int): first integer
        int_b (int): second integer

    Returns:
        int: result of the multiplication
    """
    return int_a*int_b


def first_word(text: str) -> str:
    """_summary_

    Args:
        text (str): _description_

    Returns:
        str: _description_
    """
    return text.split(" ")[0]


def is_acceptable_password(password: str) -> bool:
    """_summary_

    Args:
        password (str): _description_

    Returns:
        bool: _description_
    """
    return len(password) > 6


def number_length(a: int) -> int: #pylint: disable=invalid-name
    """_summary_

    Args:
        a (int): _description_

    Returns:
        int: _description_
    """
    return len(str(a))


def most_frequent(data: list[str]) -> str:
    """_summary_

    Args:
        data (list[str]): _description_

    Returns:
        str: _description_
    """
    new = dict.fromkeys(set(data), 0)
    for element in data:
        new[element] += 1
    return max(new, key=new.get)


def backward_string(val: str) -> str:
    """_summary_

    Args:
        val (str): _description_

    Returns:
        str: _description_
    """
    return val[::-1]

def check_coverage() -> None:
    """Checks if the GitHub coverage badge works
    """
