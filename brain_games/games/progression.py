import random


TASK = "What number is missing in the progression?"


def generate_progression() -> list:
    """Return random arithmetic progression."""
    number = random.randint(1, 20)
    step = random.randint(1, 10)
    count = random.randint(6, 11)
    result = []
    while count != 0:
        result.append(number)
        number += step
        count -= 1
    return result


def generate_round() -> tuple[str, str]:
    """
    Return arithmetic progression with a missing number
    and return the missing number.
    """
    progression = generate_progression()
    missing_number = random.choice(progression)
    progression[progression.index(missing_number)] = ".."
    progression = list(map(str, progression))
    question = ' '.join(progression)
    solution = str(missing_number)
    return question, solution
