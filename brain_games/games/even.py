import random


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


# является ли число четным
def is_even(number):
    return number % 2 == 0


# Функция вычислений, правильного вопроса и ответа
def get_game():
    rand_num_one = 1
    rand_num_two = 10
    random_number = random.randint(rand_num_one, rand_num_two)

    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = str(random_number)
    return question, correct_answer
