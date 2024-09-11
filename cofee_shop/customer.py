from order import Order
from coffee import Coffee

class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) > 15 or len(name) < 1:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders  

    def coffees(self):
        return list(set(order.coffee for order in self._orders)) 

    @classmethod
    def most_aficionado(cls, coffee):
        # Get all customers who ordered this coffee
        customers = coffee.customers()
        
        if not customers:
            return None

        # Find the customer who spent the most on this coffee
        return max(customers, key=lambda customer: sum(order.price for order in customer.orders() if order.coffee == coffee)) 

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("Expected coffee to be an instance of Coffee")
        
        new_order = Order(self, coffee, price)
        
        self._orders.append(new_order)
        
        coffee.add_order(new_order)

        return new_order
