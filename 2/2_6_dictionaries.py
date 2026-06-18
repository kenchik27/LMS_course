
# Списки и словари можно складывать друг в друга, 
# получая структуры данных, которые отражают вашу предметную область:

from pprint import pprint  # визуально форматирует вывод

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}

phones = ["Samsung Galaxy S21", "iPhone 12"]
product["recomended"] = phones
pprint(product)
{'name': 'iPhone 12 Plus',
 'price': 65432.1,
 'recomended': ['Samsung Galaxy S21', 'iPhone 12'], 'stock': 24}

# С помощью .get() можно задать значение, которое мы получим, если ключа в словаре нет.

print(product.get("discount", 0))
# 0
print(product.get("country", "CN"))
# 'CN'


# С помощью ключевого слова del можно удалить элемент по названию ключа. 
# Если такого элемента нет - будет ошибка

del product["stock"]
print(product)
{'name': 'iPhone 12', 'price': 65432.1}
del product["discount"]
# Traceback (most recent call last):
#     ...
# KeyError: 'discount'

# Вложенные списки ничем не отличаются от обычных
print(product["recomended"])
['Samsung Galaxy S21', 'iPhone 12']
product["recomended"].append("Xiaomi Mi11")
print(len(product["recomended"]))
3
print(product["recomended"][0])
# 'Samsung Galaxy S21'


# Список словарей часто используется в разработке, 
# например это может быть список товаров:

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
       'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]

# Обращаемся к ключам/индексам соответствующих словарей:

stock = [
    {"name": "iPhone 12 Plus", "stock": 24, "price": 65432.1,
        "recomended": ["Samsung Galaxy S21", "iPhone 12"]},
    {"name": "Samsung Galaxy S21", "stock": 8,
        "price": 50000.0, "discount": 5000},
    {"name": "Xiaomi Mi11", "stock": 42, "price": 38000.5}]
print(stock[2])
{'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
stock[2]["price"] = stock[2]["price"] - 8000
print(stock[2]["price"])
# 30000.5
print(stock[0]["recomended"][1])
# iPhone 12