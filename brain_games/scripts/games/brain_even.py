# import prompt
import random


def welcome_user():
    global name
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    print(f"Hello, {name}!")


# Создаем фун-цию, которая будет отвечать за саму игру, создаем
# глобальные переменные для других фун-ций
def brain_even():
    global range_num
    global answer
    global result
    result = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # Цикл для определения трех правильных попыток
    while result < 3:
        range_num = random.randint(1, 100)
        print(f'Question: {range_num}')
        answer = input('Your answer: ')
        if answer == 'yes':
            answer_yes()
        elif answer == 'no':
            answer_no()
        else:
            result = 0
            print(f'Answer "yes" if the number is even, '
                  f'otherwise answer "no"\nLet\'s try again, {name}!\'')
        # print(result)
    print(f'Congratulations, {name}!')


# Функция, если игрок ответил yes
def answer_yes():
    global result
    if range_num % 2 == 0:
        print('Correct!')
        result += 1
    else:
        print(f"'yes' is wrong answer ;(. Correct answer was "
              f"'no'. \nLet's try again, {name}!")
        result = 0


# Функция, если игрок ответил no
def answer_no():
    global result
    if range_num % 2 != 0:
        print('Correct!')
        result += 1
    else:
        print(f"'no' is wrong answer ;(. Correct answer was "
              f"'yes'. \nLet's try again, {name}!")
        result = 0


def greet():
    print("Welcome to the Brain Games!")
    welcome_user()
    brain_even()


def main():
    greet()


if __name__ == '__main__':
    main()
