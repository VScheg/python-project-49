import random


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


def get_progression_and_missing_number() -> tuple[str]:
    """
    Return arithmetic progression with a missing number
    and return the missing number.
    """
    progression = generate_progression()
    key = random.choice(progression)
    progression[progression.index(key)] = ".."
    progression = [str(i) for i in progression]
    return ' '.join(progression), str(key)
