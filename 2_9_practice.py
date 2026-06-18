# Домашнее задание №1

# Условный оператор: Возраст

# * Попросить пользователя ввести возраст при помощи input и положить 
#   результат в переменную
# * Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
#   учиться в детском саду, школе, ВУЗе или работать
# * Вызвать функцию, передав ей возраст пользователя и положить результат 
#   работы функции в переменную
# * Вывести содержимое переменной на экран

def career(age):
    if type(age) != int and type(age) != float:
        raise TypeError ('Введите  число!')
    if age < 0:
        raise ValueError ('возраст не может быть отрицательным')
    elif age < 2 :
        career = ('еще малыш')
    elif age < 7:
        career = ('детсадовец')
    elif age < 18:
        career = ('школьник')
    elif age  < 25:
        career = ('студент')
    elif age < 65:
        career = ('работник')
    else: career = ('на пенсии')
    return career

try:
    age = input('Введите возраст: ')
    whoami = career(float(age))
    print(whoami)
except ValueError:
    print('Это не число!')    


# Домашнее задание №2

# Условный оператор: Сравнение строк

# * Написать функцию, которая принимает на вход две строки
# * Проверить, является ли то, что передано функции, строками. 
#   Если нет - вернуть 0
# * Если строки одинаковые, вернуть 1
# * Если строки разные и первая длиннее, вернуть 2
# * Если строки разные и вторая строка 'learn', возвращает 3
# * Вызвать функцию несколько раз, передавая ей разные праметры 
#   и выводя на экран результаты

def check_string(string_1, string_2):
    if type(string_1)!= str or type(string_1)!= str:
        return 0
    elif string_1 == string_2:
        return 1
    elif len(string_1) > len(string_2):
        return 2
    elif string_2.strip() == 'learn':
        return 3
    else: return 'Такой случай не предусматривает вывода'

a = check_string(0, 'aa')
b = check_string('00', 'a')
c = check_string('00', '00')
d = check_string('0', 'learn')
e = check_string('0', 'learn  ')
f = check_string('0', 'aa')
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

    
     