# # 1
# # Перепишите функцию hello_user() из задания про while, 
# # чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!"
# # и завершала работу при помощи оператора break

# questions_and_answers = {'Привет': 'И тебе привет',
#                          'Как дела?': 'Хорошо',
#                          'Что делаешь?': 'Программирую'}

# def ask_user_2(questions_and_answers):
#     while True:
#         try:
#             question = input('Пользователь: ')
#             question = question.strip().lower().capitalize()
            
#             if question in questions_and_answers:
#                 answer = questions_and_answers.get(question)
#                 print (f'Программа: {answer}')
                
#             elif question not in questions_and_answers:
#                 print('Программа: я не знаю ответ')
                
#         except KeyboardInterrupt:
#             print ('Пока!')
#             break
# if __name__ == "__main__":
#     ask_user_2(questions_and_answers)
    
# 2    
# Перепишите функцию discounted(price, discount, max_discount=20) 
# из урока про функции так, чтобы она перехватывала исключения, 
# когда переданы некорректные аргументы.
# Первые два нужно приводить к вещественному числу при помощи float(), 
# а третий - к целому при помощи int() и перехватывать исключения 
# ValueError и TypeError, если приведение типов не сработало.

def discounted(price, discount, max_discount = 20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
         
        price = abs(price)
        discount = abs(discount)
        max_discount = abs(max_discount)
        
    except TypeError: 
        print('неверные  вводные')
        return None
    except ValueError: 
        print('неверные  вводные')
        return None
        
    if discount > max_discount:
        discount = max_discount
        
    if discount >= 100:
        return price
        
    else: price_with_discount = price - (price * discount / 100)
    
    return price_with_discount
    
price_discounted = discounted('abs',20)
print(price_discounted)

price_discounted = discounted('2000',20)
print(price_discounted)