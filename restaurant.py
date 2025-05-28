class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class Beverage(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price
    
    def set_price(self,price):
        self.price = price

class Appetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price
    
    def set_price(self,price):
        self.price = price

class MainCourse(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price
    
    def set_price(self,price):
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        main = False
        for item in self.items:  #detectar si hay un plato fuerte
            if item.__class__.__name__ == "MainCourse":
                main = True

        for item in self.items:
            if main and item.__class__.__name__ == "Beverage": #si hay plato fuerte hay 20% de descuento en las bebidas
                total += (80*item.get_price())/100
            else:
                total += item.get_price()
        return total

class Payment:
    def __init__(self):
        pass

    def pay(self, amount):
        pass

class Card(Payment):
    def __init__(self, number, cvv):
        super().__init__()
        self.number = number
        self.cvv = cvv

    def pay(self, amount):
        print(f"Pagando {amount} con tarjeta {self.number[-4:]}")
    
class Cash(Payment):
    def __init__(self, amount_received):
        super().__init__()
        self.amount_received = amount_received

    def pagar(self, amount):
        if self.amount_received >= amount:
            print(f"Pago realizado en efectivo. Cambio: {self.amount_received - amount}")
        else:
            print(f"Fondos insuficientes. Faltan {amount - self.amount_received} para completar el pago")