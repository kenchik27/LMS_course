# print(check_weather(-1)) # На улице холодно
# print(check_weather(8)) # На улице прохладно
# print(check_weather(21)) # На улице тепло
# print(check_weather(32)) # На улице жарко

def check_weather(temperature):
    if temperature < 0: 
        message = 'На улице холодно'
    elif temperature >= 0 and temperature < 10: 
        message = 'На улице прохладно'
    elif temperature >= 10 and temperature < 25: 
        message = 'На улице тепло'
    else:
        message = 'На улице жарко'
    return message

print(check_weather(25))

# На айфон нет скидки
def discounted(price, discount, max_discount = 30, phone_name = ''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    
    if phone_name.strip().lower() == 'iphone':
        return price
           
    if discount >= max_discount:
        return price
    
    else:
        return price - (price * discount / 100)

new_price = discounted(60000, 15, phone_name = 'IpHone ')
print(new_price)
