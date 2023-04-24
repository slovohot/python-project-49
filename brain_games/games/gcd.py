import random
from math import gcd


GAME_RULE = 'Find the greatest common divisor of given numbers.'


# Функция вычислений, правильного вопроса и ответа
def get_game():
    rand_num_one = random.randint(1, 10)
    rand_num_two = random.randint(1, 20)
    # ищем НОД
    correct_answer = gcd(rand_num_one, rand_num_two)
    question = str(rand_num_one) + " " + str(rand_num_two)
    return question, correct_answer
