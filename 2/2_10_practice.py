# Домашнее задание №1

# Цикл while: hello_user

# * Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
#   пользователя “Как дела?”, пока он не ответит “Хорошо”
   
# """

def hello_user():
    reply = input('Как дела? \n')
    while reply.strip().lower() != 'хорошо':
        reply = input('Как дела? \n')

if __name__ == "__main__":
    hello_user()


# """

# Домашнее задание №2

# Цикл while: ask_user со словарём

# * Создайте словарь типа "вопрос": "ответ", например:
#   {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
# * Напишите функцию ask_user() которая с помощью функции input()
#   просит пользователя ввести вопрос, а затем, если вопрос есть
#   в словаре, программа давала ему соотвествующий ответ. Например:

#     Пользователь: Что делаешь?
#     Программа: Программирую
    
# """

questions_and_answers = {'Привет': 'И тебе привет',
                         'Как дела?': 'Хорошо',
                         'Что делаешь?': 'Программирую'}

def ask_user():
    question = input('Пользователь: ')
    question = question.strip().lower().capitalize()
    while question in questions_and_answers:
        answer = questions_and_answers.get(question)
        print(f'Программа: {answer}')
        question = input('Пользователь: ')
        question = question.strip().lower().capitalize()
        
    else: print('Программа: я не знаю ответ')
if __name__ == "__main__":
    ask_user()
    
    
def ask_user_2(questions_and_answers):
    while True:
        question = input('Пользователь: ')
        question = question.strip().lower().capitalize()
        
        if question == 'Пока':
            break
        
        elif question in questions_and_answers:
            answer = questions_and_answers.get(question)
            print (f'Программа: {answer}')
        
        else: print('Программа: я не знаю ответ')
     
if __name__ == "__main__":
    ask_user_2(questions_and_answers)