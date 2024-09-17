import prompt
from .generate import generate_expression


def is_correct(answer, correct, name):
    if answer == correct:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False


def game(name, game_name):
    tries = 3
    while tries != 0:
        expression, result = generate_expression(game_name)
        print(f"Question: {expression}")
        user_answer = prompt.string("Your answer: ")
        if is_correct(user_answer, result, name):
            tries -= 1
        else:
            break
    else:
        print(f"Congratulations, {name}!")
