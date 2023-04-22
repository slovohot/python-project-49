import random


def promo_question():
    return 'What number is missing in the progression?'


# Функция вычислений, правильного вопроса и ответа
def get_game():
    # рандомный интервал чисел
    interval_num = random.randint(1, 3)
    # список чисел
    list_of_number = [x for x in range(1, 100, interval_num)]
    # создаем два индекса для итогого списка в вопрос
    gen_index_one = random.randint(0, 25)
    gen_index_two = gen_index_one + 10
    # конечный список чисел
    end_list_num = list_of_number[gen_index_one:gen_index_two]
    # определяем рандомный индекс для end_list_num
    random_index = random.randint(0, 9)
    # определяем число = парвильный ответ
    correct_answer = end_list_num[random_index]
    # заменяем правильный ответ на точки
    end_list_num[random_index] = '..'
    question = " ".join(map(str, (end_list_num)))
    return question, correct_answer
