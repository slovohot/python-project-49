import random


def promo_question():
    return 'What is the result of the expression?'


# Функция вычислений, правильного вопроса и ответа
def get_game():
    RAND_NUM_ONE = random.randint(1, 10)
    RAND_NUM_TWO = random.randint(1, 10)
    math_oper = [' + ', ' - ', ' * ']
    random_oper = random.choice(math_oper)
    question = str(RAND_NUM_ONE) + random_oper + str(RAND_NUM_TWO)

    if random_oper == ' + ':
        correct_answer = RAND_NUM_ONE + RAND_NUM_TWO
        return question, correct_answer
    elif random_oper == ' - ':
        correct_answer = RAND_NUM_ONE - RAND_NUM_TWO
        return question, correct_answer
    else:
        correct_answer = RAND_NUM_ONE * RAND_NUM_TWO
        return question, correct_answer


"""
был еще вариант использовать - correct_answer = eval(question)
но я прочитал, что ее использование не желательно, поэтому оставил
if-elif-else
"""
