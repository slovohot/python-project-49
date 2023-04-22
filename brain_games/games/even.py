import random


def promo_question():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


# является ли число четным
def is_even(number):
    return number % 2 == 0


# Функция вычислений, правильного вопроса и ответа
def get_game():
    RAND_NUM_ONE = 1
    RAND_NUM_TWO = 10
    random_number = random.randint(RAND_NUM_ONE, RAND_NUM_TWO)

    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = str(random_number)
    return question, correct_answer
