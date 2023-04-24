import random
from math import gcd


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# является ли число простым
def is_prime(num):
    if len(gcd(num)) == 2:
        return num


# Функция вычислений, правильного вопроса и ответа
def get_game():
    rand_num_one = 1
    rand_num_two = 10
    random_number = random.randint(rand_num_one, rand_num_two)
    question = random_number
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
