import random


def promo_question():
    return 'Find the greatest common divisor of given numbers.'


# функция для создания списка делителей числа
def is_finding_the_divisor(n):
    divisor = []
    for i in range(1, int(n) + 1):
        if n % i == 0:
            divisor += [i]
    return divisor


# Функция вычислений, правильного вопроса и ответа
def get_game():
    RAND_NUM_ONE = random.randint(1, 10)
    RAND_NUM_TWO = random.randint(1, 20)
    # создаем 2 списка делителей
    list_num_one = is_finding_the_divisor(RAND_NUM_ONE)
    list_num_two = is_finding_the_divisor(RAND_NUM_TWO)
    # создаем один общий список делителей
    identical_divisors = list(set(list_num_one) & set(list_num_two))
    # ищем максимальный делитель
    correct_answer = max(identical_divisors)
    question = str(RAND_NUM_ONE) + " " + str(RAND_NUM_TWO)
    return question, correct_answer
