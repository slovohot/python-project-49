import prompt


# создае движек, который принимает вопрос условия
# игры для юсера, вопрос и ответ
def engine_games(promo_question, get_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(promo_question())
    attempt = 0
    while attempt < 3:
        question, correct_answer = get_game()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
            attempt += 1

        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'. \nLet's try again, {name}!")
            exit()

    print(f'Congratulations, {name}!')
