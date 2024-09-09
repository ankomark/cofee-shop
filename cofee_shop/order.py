class Order:
    all_orders_list = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of the Customer class")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of the Coffee class")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders_list.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all_orders(cls):
        return cls.all_orders_list
