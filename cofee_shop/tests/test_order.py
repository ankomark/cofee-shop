import sys
import os

# Add the parent directory (the project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation():
    customer = Customer("Mark")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 4.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.0

def test_order_price_invalid():
    customer = Customer("Mark")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)

def test_order_customer_invalid():
    coffee = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("Mark", coffee, 4.0)

def test_order_coffee_invalid():
    customer = Customer("Mark")
    with pytest.raises(TypeError):
        Order(customer, "Latte", 4.0)
