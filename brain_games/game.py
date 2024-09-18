import prompt
from .welcome import welcome_user
from .generate import generate_expression


def is_correct(answer, correct, name):
    if answer == correct:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False


def game(game_name, task):
    user_name = welcome_user()
    print(task)
    tries = 3
    while tries != 0:
        expression, result = generate_expression(game_name)
        print(f"Question: {expression}")
        user_answer = prompt.string("Your answer: ")
        if is_correct(user_answer, result, user_name):
            tries -= 1
        else:
            break
    else:
        print(f"Congratulations, {user_name}!")
