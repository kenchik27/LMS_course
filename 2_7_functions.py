price = 100
discount = 5

price_with_discoount = price - (price * discount / 100)
print(price_with_discoount)

def discounted(price, discount):
    price = abs(price)
    discount = abs(discount)
    if discount >= 100:
        price_with_discount = price
    else: price_with_discount = price - (price * discount / 100)
    return price_with_discount


price_discounted = discounted(200,20)
print(price_discounted)

product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['with_discount'] = (discounted(product['price'], product['discount']))
print(product)

