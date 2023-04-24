import random
from math import gcd


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def find_greatest_divisor(n):
    divisor = []
    for i in range(1, int(n) + 1):
        if n % i == 0:
            divisor += [i]
    return divisor


# Функция вычислений, правильного вопроса и ответа
def get_game():
    random_number = random.randint(1, 20)
    question = random_number
    divisor = find_greatest_divisor(random_number)
    if len(divisor) == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
