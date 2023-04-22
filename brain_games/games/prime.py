import random


def promo_question():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


# функция для создания списка делителей числа
def is_finding_the_divisor(n):
    divisor = []
    for i in range(1, int(n) + 1):
        if n % i == 0:
            divisor += [i]
    return divisor


# является ли число простым
def is_prime(num):
    if len(is_finding_the_divisor(num)) == 2:
        return num


# Функция вычислений, правильного вопроса и ответа
def get_game():
    RAND_NUM_ONE = 1
    RAND_NUM_TWO = 10
    random_number = random.randint(RAND_NUM_ONE, RAND_NUM_TWO)
    question = random_number
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
