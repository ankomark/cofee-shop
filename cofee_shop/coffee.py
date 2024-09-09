from order import Order

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders  

    def customers(self):
        return list(set(order.customer for order in self._orders))  

    def num_orders(self):
        return len(self._orders)  

    def average_price(self):
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders) if self._orders else 0.0  

    def add_order(self, order):
        
        if isinstance(order, Order) and order.coffee == self:
            self._orders.append(order)
