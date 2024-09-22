import prompt
from typing import Union
from .games import calc, gcd, even, prime, progression


ROUNDS = 3
TASKS = {
    "even": 'Answer "yes" if the number is even, otherwise answer "no".',
    "prime": 'Answer "yes" if given number is prime. Otherwise answer "no".',
    "calc": "What is the result of the expression?",
    "gcd": "Find the greatest common divisor of given numbers.",
    "progression": "What number is missing in the progression?"}


def get_question_and_solution(game_name: str) -> tuple[Union[int, str]]:
    """Return question and solution."""
    match game_name:
        case "even":
            return even.get_number_and_solution(even.is_even)
        case "calc":
            return calc.get_expression_and_solution()
        case "gcd":
            return gcd.get_numbers_and_gcd()
        case "progression":
            return progression.get_progression_and_missing_number()
        case "prime":
            return even.get_number_and_solution(prime.is_prime)


def is_correct(answer: str, solution: str) -> bool:
    """Check if answer is correct."""
    return True if answer == solution else False


def play_game(game_name: str) -> None:
    """Start game process."""
    global ROUNDS
    global TASKS
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(TASKS[game_name])
    while ROUNDS != 0:
        question, solution = get_question_and_solution(game_name)
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if is_correct(answer, solution):
            print("Correct!")
            ROUNDS -= 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{solution}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
