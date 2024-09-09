import sys
import os

# Add the parent directory (the project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order


import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_valid():
    customer = Customer("Mark")
    assert customer.name == "Mark"

def test_customer_name_invalid():
    with pytest.raises(ValueError):
        Customer("")

def test_customer_create_order():
    customer = Customer("Mark")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    assert len(customer.orders()) == 1

def test_customer_orders():
    customer = Customer("Mark")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 4.0)
    customer.create_order(coffee2, 5.0)
    assert len(customer.orders()) == 2

def test_customer_coffees():
    customer = Customer("Mark")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 4.0)
    customer.create_order(coffee2, 5.0)
    assert set(customer.coffees()) == {coffee1, coffee2}

def test_most_aficionado():
    customer1 = Customer("Mark")
    customer2 = Customer("John")
    coffee = Coffee("Cappuccino")
    
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 7.0)
    
    assert Customer.most_aficionado(coffee) == customer2
