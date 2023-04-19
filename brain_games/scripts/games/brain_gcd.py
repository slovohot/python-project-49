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


def is_finding_the_divisor(n):
    divisor = []
    for i in range(1, int(n) + 1):
        if n % i == 0:
            divisor += [i]
    # print(divisor)
    return divisor


# Определяем функцию игры и делаем глобальными
# нужные нам пермененные из deductions_gcd()
def brain_gcd():
    global max_divisors
    global num_one
    global num_two
    print('Find the greatest common divisor of given numbers.')
    attempt = 0  # сумма правильных попыток
    while attempt < 3:  # запускаем цикл, для высчитывания кол-ва попыток
        # вызываем функцию логики, чтобы она высчитала нам цифры
        deductions_gcd()
        print('Question: ' + str(num_one) + " " + str(num_two))
        answer = int(input('Your answer: '))
        if answer == max_divisors:
            print('Correct!')
            attempt += 1  # запоминаем правильную попытку
        else:
            print(f"'{answer}' is wrong answer ;(. Correct "
                  f"answer was '{max_divisors}'.\nLet's try again, {name}!")
            exit()  # выходим из программы
    if attempt == 3:  # при наличии трех правильных попыток - win
        print(f'Congratulations, {name}!')


# Функция для вычисления нужных нам значений для brain_gcd()
def deductions_gcd():
    global max_divisors
    global num_one
    global num_two
    num_one = random.randint(1, 10)  # генерируем цифры
    num_two = random.randint(1, 10)
    # print(num_one)
    # print(num_two)
    list_num_one = is_finding_the_divisor(num_one)  # выбираем рандомные цифры
    list_num_two = is_finding_the_divisor(num_two)
    # print(list_num_one)
    # print(list_num_two)
    # собираем в список делители
    identical_divisors = list(set(list_num_one) & set(list_num_two))
    # print(identical_divisors)
    # и выбираем максимальный из делителей
    max_divisors = max(identical_divisors)
    # print(max_divisors)


def greet():
    print("Welcome to the Brain Games!")
    welcome_user()


def main():
    greet()
    brain_gcd()


if __name__ == '__main__':
    main()
