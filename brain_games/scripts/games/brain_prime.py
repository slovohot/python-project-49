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


# # создаем список всех делителей числа
def is_finding_the_divisor(n):
    divisor = []
    for i in range(1, int(n) + 1):
        if n % i == 0:
            divisor += [i]
    # print(divisor)
    return divisor


def brain_prime():
    # Создаем фун-цию, которая будет отвечать за саму игру, создаем
    # глобальные переменные для других фун-ций
    global range_num
    global attempt
    attempt = 0  # количество попыток
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    # Цикл для определения трех правильных попыток
    while attempt < 3:
        range_num = random.randint(1, 20)
        print(f'Question: {range_num}')
        answer = input('Your answer: ')
        if answer == 'yes':
            answer_yes()
        elif answer == 'no':
            answer_no()
        else:
            attempt = 0
            print(f'Answer "yes" if the number is even, '
                  f'otherwise answer "no"\nLet\'s try again, {name}!\'')
        # print(result)
    print(f'Congratulations, {name}!')


# Функция, если игрок ответил yes
def answer_yes():
    global attempt
    # выносим длину списка делителей в отдельную переменную
    div = len(is_finding_the_divisor(range_num))
    # ответ правильный, если делителей
    # всего два - это один и само число
    if div == 2:
        print('Correct!')
        attempt += 1
    else:
        print(f"'yes' is wrong answer ;(. Correct answer was "
              f"'no'. \nLet's try again, {name}!")
        attempt = 0


# Функция, если игрок ответил no
def answer_no():
    global attempt
    div = len(is_finding_the_divisor(range_num))
    if div != 2:
        print('Correct!')
        attempt += 1
    else:
        print(f"'no' is wrong answer ;(. Correct answer was "
              f"'yes'. \nLet's try again, {name}!")
        attempt = 0


def greet():
    print("Welcome to the Brain Games!")
    welcome_user()
    brain_prime()


def main():
    greet()


if __name__ == '__main__':
    main()
