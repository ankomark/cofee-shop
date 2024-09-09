import sys
import os

# Add the parent directory (the project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order

import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_valid():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_invalid():
    with pytest.raises(ValueError):
        Coffee("")

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer1 = Customer("Mark")
    customer2 = Customer("John")
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 5.0)
    assert len(coffee.orders()) == 2

def test_coffee_customers():
    coffee = Coffee("Latte")
    customer1 = Customer("Mark")
    customer2 = Customer("John")
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 5.0)
    assert set(coffee.customers()) == {customer1, customer2}

def test_coffee_num_orders():
    coffee = Coffee("Latte")
    customer1 = Customer("Mark")
    customer1.create_order(coffee, 4.0)
    assert coffee.num_orders() == 1

def test_coffee_average_price():
    coffee = Coffee("Latte")
    customer1 = Customer("Mark")
    customer2 = Customer("John")
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 6.0)
    assert coffee.average_price() == 5.0
