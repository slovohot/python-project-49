import random
from math import gcd


GAME_RULE = 'Find the greatest common divisor of given numbers.'


# Функция вычислений, правильного вопроса и ответа
def get_game():
    rand_num_one = random.randint(1, 10)
    rand_num_two = random.randint(1, 20)
    # создаем 2 списка делителей
    list_num_one = gcd(rand_num_one)
    list_num_two = gcd(rand_num_two)
    # создаем один общий список делителей
    identical_divisors = list(set(list_num_one) & set(list_num_two))
    # ищем максимальный делитель
    correct_answer = max(identical_divisors)
    question = str(rand_num_one) + " " + str(rand_num_two)
    return question, correct_answer
