#!/usr/bin/env python3
from ..welcome import welcome_user 
from ..game import game


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(user_name, 'even')


if __name__ == "__main__":
    main()
