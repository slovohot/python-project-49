# import prompt
import random


# Приветствие игорока
def welcome_user():
    global name
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f"Hello, {name}!")


# Создаем фун-цию, которая будет отвечать за игру
def brain_calc():
    # Определяем глобальную переменную для суммы правильных
    # попыток из функций с операциями
    global num_one
    global num_two
    global attempt
    attempt = 0  # Количество правильных попыток
    print('What is the result of the expression?')
    while attempt < 3:
        num_one = random.randint(1, 20)  # Создаем рандомные цифры
        num_two = random.randint(1, 20)
        math_oper = [' + ', ' - ', ' * ']  # Создаем список операций
        randow_oper = random.choice(math_oper)  # и выбираем рандомную
        print('Question: ' + str(num_one) + randow_oper + str(num_two))
        # Далее сравниваем какая операция выбралась и делаем
        # вычисление и сравнение для всех видов операций
        if randow_oper == ' + ':
            sum_num()

        elif randow_oper == ' - ':
            diff_num()

        elif randow_oper == ' * ':
            multiply_num()

    if attempt == 3:  # при наличии трех правильных попыток - win
        print(f'Congratulations, {name}!')


# Функция если операция выпала - сумма
def sum_num():
    global attempt  # задаем глобальную переменную с попытками
    result_sample = num_one + num_two
    # print(result)
    answer = int(input('Your answer: '))
    if result_sample == answer:
        print('Correct!')
        attempt += 1  # попытка засчитана
    else:
        print(f"'{answer}' is wrong answer ;(. Correct "
              f"answer was '{result_sample}'.\nLet's try again, {name}!")
        exit()  # выходим из программы по условию задачи


# Функция если операция выпала - вычитание
def diff_num():
    global attempt
    result_sample = num_one - num_two
    # print(result)
    answer = int(input('Your answer: '))
    if result_sample == answer:
        print('Correct!')
        attempt += 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct "
              f"answer was '{result_sample}'.\nLet's try again, {name}!")
        exit()


# Функция если операция выпала - умножение
def multiply_num():
    global attempt
    result_sample = num_one * num_two
    # print(result)
    answer = int(input('Your answer: '))
    if result_sample == answer:
        print('Correct!')
        attempt += 1
    else:
        print(f"'{answer}' is wrong answer ;(. Correct "
              f"answer was '{result_sample}'.\nLet's try again, {name}!")
        exit()


def greet():
    print("Welcome to the Brain Games!")
    welcome_user()
    brain_calc()


def main():
    greet()


if __name__ == '__main__':
    main()
