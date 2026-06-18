from pprint import pprint

cities = {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
pprint(cities.get("city"))
# Уменьшите значение "temperature" на 5
cities["temperature"] = (int(cities["temperature"]))-5
pprint(cities.get("temperature"))
# Выведите на экран весь словарь
pprint(cities)

# Проверьте, есть ли в словаре ключ country
pprint(cities.get("country"))
# Выведите значение по-умолчанию "Россия" для ключа country
pprint(cities.get("country", "Russia"))
# Добавьте в словарь элемент date со значением "27.05.2019"
cities["date"] = "27.05.2019"
pprint(cities)
# Выведите на экран длину словаря
print(len(cities))