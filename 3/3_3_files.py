with open('3_3.txt', 'w', encoding ='utf-8') as f:
    f.write ('ПРИВЕТ!!')
    
# w - запись (содержимое перезаписывается)
# r - чтение 
# a - добавление (содержиое в конец файла)

# \t - табуляция
# \n - новая строка

with open('3_3.txt', 'a', encoding = 'utf-8') as f:
    f.write('как дела что делаешь \tвсе ок')

# with open('3_3.txt', 'r', encoding = 'utf-8') as f:
#     content = f.read()
#     print(content)
    
with open('3_3.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.upper()
        print(line)