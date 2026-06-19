
with open('referat.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    lenght = len(text)
    words = text.split()
    words_counter = len(words)

new_text = text.replace('.', '!')    
    
with open ('referat_2.txt', 'w', encoding = 'utf-8') as f:
    f.write(new_text)    

with open ('referat_2.txt', 'a', encoding='utf-8') as f:
    f.write(f'\nСводка:\nДлина:\t{lenght}\nЧисло слов:\t{words_counter}')