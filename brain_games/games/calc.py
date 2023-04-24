import random


GAME_RULE = 'What is the result of the expression?'


def calc_expression(random_oper, rand_num_one, rand_num_two):
    if random_oper == ' + ':
        correct_answer = rand_num_one + rand_num_two
        return correct_answer
    elif random_oper == ' - ':
        correct_answer = rand_num_one - rand_num_two
        return correct_answer
    else:
        correct_answer = rand_num_one * rand_num_two
        return correct_answer


# Функция вычислений, правильного вопроса и ответа
def get_game():
    rand_num_one = random.randint(1, 10)
    rand_num_two = random.randint(1, 10)
    math_oper = [' + ', ' - ', ' * ']
    random_oper = random.choice(math_oper)
    question = str(rand_num_one) + random_oper + str(rand_num_two)
    correct_answer = calc_expression(random_oper, rand_num_one, rand_num_two)
    return question, correct_answer
