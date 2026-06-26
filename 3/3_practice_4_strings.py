# Вывести последнюю букву в слове
word = 'Архангельск'
# ???

print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
a_counter = 0
for w in word:
    if w.lower() == 'а':
        a_counter += 1
print(f'\nКол-во букв А в слове {word}: \n{a_counter} букв\n')

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???

glasnye = ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я']
counta = 0

for letter in word:
    if letter.lower() in glasnye:
        counta += 1
print(f'Кол-во гласных в слове {word}: \n{counta} гласных\n')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
counta_words = 1
for s in sentence:
    if s == ' ':
        counta_words += 1
print(f'Кол-во слов в стрроке {sentence}: \n{counta_words} слова\n')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
print(sentence[0])
for i in range(len(sentence)):
    if sentence[i-1] == ' ':
        print (f'{sentence[i]}')

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
list_of_lens = []
for i in range(len(sentence)):
    if sentence[i] == ' ':
        word = sentence[:i]
        len_word = len(word)
        list_of_lens.append(len_word)


sum = sum(list_of_lens)
av = sum / len(list_of_lens)
print(list_of_lens)
print(av)