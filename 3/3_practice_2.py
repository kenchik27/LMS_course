# Задание 1
# Дан список учеников, нужно посчитать количество повторений 
# каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

from collections import Counter

list_of_names = []
for name in students:
    person = name.get('first_name')
    list_of_names.append(person)

# способ 1
count = Counter(list_of_names)
print(count)

# способ 2
for name in count:
    value = count.get(name)
    print(f'{name}: {value}')
    
    
# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
all_people = []
for name in students:
    person = name.get('first_name')
    all_people.append(person)

count = Counter(all_people)

max_value = 0
for c in count:
    if count.get(c) > max_value:
        max_value = count.get(c)
        max_name = c
print(f'Самое частое имя среди учеников: {max_name} ({max_value})')    

# Задание 3
# Есть список учеников в нескольких классах, 
# нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for class_ in school_students:
    max_ = 0
    names_list = []
    i = 0
    for dict in class_:
        name = dict.get('first_name')
        names_list.append(name)
    
    count = Counter(names_list)
    for name in count:
        if count.get(name) > max_:
            max_ = count.get(name)
            max__name = name
    
    index = school_students[i]
    i += 1
    
    print(f'Самое частое имя в классе {i}: {max__name}')
        

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_ in school:
    students = class_.get('students')
    students_in_class = []
    
    classik = class_.get('class')
    
    for student in students:
        for item in student:
            item = student.get('first_name')
            students_in_class.append(item)
    girls = []
    boys = []
    for name in students_in_class:
        if is_male.get(name) == True:
            boys.append(is_male.get(name))
        elif is_male.get(name) == False:
            girls.append(is_male.get(name))
                
    print(f'Класс {classik}: девочки {len(girls)}, мальчики {len(boys)} ')
    # print(students_in_class)
    
    
# Задание 5
# По информации о учениках разных классов нужно найти класс, 
# в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '5d', 'students': [{'first_name': 'Олег'},{'first_name': 'Олег'}, {'first_name': 'Миша'}]}
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for class_ in school:
    students = class_.get('students')
    students_in_class = []
    
    classik = class_.get('class')
    
    for student in students:
        for item in student:
            item = student.get('first_name')
            students_in_class.append(item)
    
    class_['boys'] = []
    class_['girls'] = []
    for name in students_in_class:
        if is_male.get(name) == True:
            class_['boys'].append(name)   
        elif is_male.get(name) == False:
            class_['girls'].append(name) 
    
    girls_counter = len(class_['girls'])
    boys_counter = len(class_['boys'])
        
    max_girls = 0
    max_boys = 0
    
    if girls_counter > max_girls:
        max_girls = girls_counter
        max_girls_class = class_.get('class')
    if boys_counter > max_boys:
        max_boys = boys_counter
        max_boys_class = class_.get('class')
    # print(students_in_class)

print (f'Больше всего мальчиков в классе {max_boys_class}')
print (f'Больше всего девочек в классе {max_girls_class}')