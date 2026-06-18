#1
# Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра,
# приводит их к строке и отдает объединенными через разделитель delimiter

def get_summ(one, two, delim = '&'):
    one = str(one)
    two = str(two)
    string = one + delim + two
    string = string.upper()
    return string
# Вызовите функцию, передав в нее два аргумента "Learn" и "python", 
# положите результат в переменную и выведите ее значение на экран
result = get_summ("Learn", "python")
print(result)
# Сделайте так, чтобы результирующая строка выводилась заглавными буквами

#2
# Создайте в редакторе файл price.py
# Создайте функцию format_price, которая принимает один аргумент price
# Приведите price к целому числу (тип int)
# Верните строку "Цена: ЧИСЛО руб."
# Вызовите функцию, передав на вход 56.24 и положите результат в переменную
# Выведите значение переменной с результатом на экран

def format_price(price):
    price = int(price)
    string_2 = f'Цена: {price} руб.'
    return string_2

show_price = format_price(56.24)
print(show_price)