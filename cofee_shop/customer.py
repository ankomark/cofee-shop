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
        from order import Order
        return [order for order in self._orders if isinstance(order, Order)]

    def coffees(self):
        from order import Order
        return list(set(order.coffee for order in self._orders if isinstance(order, Order)))

    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee.add_order(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of the Coffee class")

        customer_spending = {}
        for order in Order.all_orders():
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price

        if not customer_spending:
            return None

        max_spender = max(customer_spending, key=customer_spending.get)
        return max_spender
