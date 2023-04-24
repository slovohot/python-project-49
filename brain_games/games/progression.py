import random


GAME_RULE = 'What number is missing in the progression?'


def generate_progression():
    # рандомный интервал между числами
    interval_num = random.randint(1, 5)
    # список чисел
    list_of_number = [x for x in range(1, 100, interval_num)]
    # создаем два индекса для итогого списка в вопрос
    gen_index_one = random.randint(0, 10)
    gen_index_two = gen_index_one + 10
    # конечный список чисел
    end_list_num = list_of_number[gen_index_one:gen_index_two]
    # определяем рандомный индекс для end_list_num
    random_index = random.randint(0, 5)

    return end_list_num, random_index

# Функция вычислений, правильного вопроса и ответа
def get_game():
    end_list_num, random_index = generate_progression()
    # определяем число = парвильный ответ
    correct_answer = end_list_num[random_index]
    # заменяем правильный ответ на точки
    end_list_num[random_index] = '..'
    question = " ".join(map(str, (end_list_num)))
    return question, correct_answer
