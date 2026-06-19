class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def coordinates(self):
        print(f'Координаты: {self.x}, {self.y}')

# метод корректного вывода        
    def __repr__(self):
        return f'Координаты: {self.x}, {self.y}'

# point_1 = Point(3,7)
# point_1.coordinates()

# print(point_1)

class Product:
    
    def __init__(self, name, price, stock = 0, discount = 0, max_discount = 20):
        self.name = name.strip()
        if len(self.name) < 1:
            raise ValueError ('Слишком короткое название')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        
        if self.max_discount > 99:
            raise ValueError ('Cлишком большая максимальная скидка')
        if self.discount > self.max_discount:
            self.discount = max_discount
    
    def discounted(self):
        return self.price * self.discount / 100
    
    def sell(self, items = 1):
        if items > self.stock:
            raise ValueError('Недостаточно товара на складе')
        self.stock -= items
    
    def __repr__(self):
        return f'Товар: {self.name}, цена: {self.price}, кол-во на складе: {self.stock} '
    
product_1 = Product('item', 100, stock = 6)
print(product_1)
product_1.sell(5)
print(product_1)