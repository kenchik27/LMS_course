# from collections import Counter

# phones = ['iphone', 'huawei', 'samsung', 'lg', 'iphone', 'lg', 'lg']
# count = Counter(phones)
# print(count)

# text = 'проводит ночи 31-я весна и без сомнения ревнует ко всему'
# text = text.lower().replace(' ', '')
# count_2 = Counter(text)
# print(count_2)

# pip3 install ephem

import ephem

mars = ephem.Mars('2020/01/01')
const = ephem.constellation(mars)
print(const)


# import sys
# print(sys.executable)   # путь к интерпретатору
# print(sys.version)   