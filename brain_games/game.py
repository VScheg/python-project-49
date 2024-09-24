import prompt
from types import ModuleType


ROUNDS = 3


def is_correct(answer: str, solution: str) -> bool:
    """Check if answer is correct."""
    return answer == solution


def play_game(game_module: ModuleType) -> None:
    """Start game process."""
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(game_module.TASK)
    count = ROUNDS
    while count != 0:
        question, solution = game_module.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if not is_correct(answer, solution):
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{solution}'."
            )
            print(f"Let's try again, {user_name}!")
            return
        print("Correct!")
        count -= 1
    print(f"Congratulations, {user_name}!")
