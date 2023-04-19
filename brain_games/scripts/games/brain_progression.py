# import prompt
import random


# Приветствие игрока
def welcome_user():
    global name
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f"Hello, {name}!")


# функция подсчета правильных ответов и
# выбор рандомной функции с разным шагом
def brain_progression():
    global attempt
    attempt = 0  # Количество правильных попыток
    print('What number is missing in the progression?')
    # три версии с разным шагом
    range_version = [1, 2, 3]
    while attempt < 3:
        # рандомный выбор трех версий
        random_version = random.choice(range_version)
        # выполнение функции в зависимости от выбранной версии выше
        if random_version == 1:
            generation_version_one()

        elif random_version == 2:
            generation_version_two()

        elif random_version == 3:
            generation_version_three()

    print(f'Congratulations, {name}!')


def generation_version_one():
    global attempt
    # генерация списка случайных чисел
    gen_list = [x for x in range(1, 100)]
    # генерация случайного индекса для списка выше
    gen_index_one = random.randint(0, 89)
    # print(gen_index_one)  # принты ниже созданы для отладки
    # устанавливаем второй индекс и определяем длину
    # выводимого списка для вывода игроку
    gen_index_two = gen_index_one + 10  # 10 - длина списка для игрока
    # print(gen_index_two)
    # итоговый список чисел для игрока
    result_list_one = gen_list[gen_index_one:gen_index_two]
    # print(result_list_one)
    # генерируем рандомный индекс, чтобы его скрыть
    random_index = random.randint(0, 9)
    # запоминаем число под индексом, который сгенерировали выше
    result_num_one = result_list_one[random_index]
    # print(result_num_one)
    # заменяем индекс на ".."
    result_list_one[random_index] = '..'
    quest = 'Question:'
    # выводим вопрос и список чисел с ".."
    print(quest, *result_list_one)
    answer = int(input('Your answer: '))  # ответ игрока
    if answer == result_num_one:
        print('Correct!')
        attempt += 1  # попытка засчитана
    else:
        print(f"'{answer}' is wrong answer ;(. Correct "
              f"answer was '{result_num_one}'.\nLet's try again, {name}!")
        exit()


# остальные функции работают аналогично generation_version_one()
# за исключением разницы шага чисел в списке
def generation_version_two():
    global attempt
    gen_list = [x for x in range(1, 200, 2)]
    # print(gen_list)
    gen_index_one = random.randint(0, 60)
    # print(gen_index_one)
    gen_index_two = gen_index_one + 10
    # print(gen_index_two)
    result_list_two = gen_list[gen_index_one:gen_index_two]
    # print(result_list_two)
    random_index = random.randint(0, 9)
    result_num_two = result_list_two[random_index]
    # print(result_num_two)
    result_list_two[random_index] = '..'
    quest = 'Question:'
    print(quest, *result_list_two)
    answer = int(input('Your answer: '))
    if answer == result_num_two:
        print('Correct!')
        attempt += 1  # попытка засчитана
    else:
        print(f"'{answer}' is wrong answer ;(. Correct "
              f"answer was '{result_num_two}'.\nLet's try again, {name}!")
        exit()


# остальные функции работают аналогично generation_version_one()
# за исключением разницы шага чисел в списке
def generation_version_three():
    global attempt
    gen_list = [x for x in range(1, 300, 3)]
    gen_index_one = random.randint(0, 89)
    # print(gen_index_one)
    gen_index_two = gen_index_one + 10
    # print(gen_index_two)
    result_list_three = gen_list[gen_index_one:gen_index_two]
    # print(result_list_three)
    random_index = random.randint(0, 9)
    result_num_three = result_list_three[random_index]
    # print(result_num_three)
    result_list_three[random_index] = '..'
    quest = 'Question:'
    print(quest, *result_list_three)
    answer = int(input('Your answer: '))
    if answer == result_num_three:
        print('Correct!')
        attempt += 1  # попытка засчитана
    else:
        print(f"'{answer}' is wrong answer ;(. Correct "
              f"answer was '{result_num_three}'.\nLet's try again, {name}!")
        exit()


# приветствие игрока
def greet():
    print("Welcome to the Brain Games!")
    welcome_user()


def main():
    greet()
    brain_progression()


if __name__ == '__main__':
    main()
