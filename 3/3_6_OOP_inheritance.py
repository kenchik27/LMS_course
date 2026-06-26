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
    

class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
    
    def __repr__(self):
        return f'ТТ Товар: {self.name}, цена: {self.price}, кол-во на складе: {self.stock} '
    


class Sofa(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture
    
    def __repr__(self):
        return f'ТТ Товар: {self.name}, цена: {self.price}, кол-во на складе: {self.stock} '


my_phone = Phone('Iphone', 60000, 'black')
print(my_phone)
print(my_phone.color)

sofa_1 = Sofa('big sofa', 23455, 'red', 'leather')
print(sofa_1)



