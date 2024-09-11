

Coffee Shop Domain Model

Overview

This project is a domain model for managing a coffee shop, including customers, coffees, and orders. It demonstrates the use of object-oriented programming principles in Python.

Project Structure

customer.py: Defines the Customer class.
coffee.py: Defines the Coffee class.
order.py: Defines the Order class.
debug.py: Contains the main function to test and demonstrate the functionality of the classes.
Classes
Customer
Attributes:

_name: Name of the customer.
_orders: List of orders placed by the customer.
Methods:

__init__(self, name): Initializes a customer with a name.
name: Property to get the customer's name.
orders(): Returns the list of orders made by the customer.
coffees(): Returns a list of unique coffees ordered by the customer.
most_aficionado(coffee): Class method to find the customer who has ordered the most of a particular coffee.
create_order(coffee, price): Creates an order for the customer and adds it to the coffee.
Coffee
Attributes:

_name: Name of the coffee.
_orders: List of orders associated with this coffee.
Methods:

__init__(self, name): Initializes a coffee with a name.
name: Property to get the coffee's name.
orders(): Returns the list of orders for this coffee.
customers(): Returns a list of unique customers who ordered this coffee.
num_orders(): Returns the number of orders for this coffee.
average_price(): Returns the average price of the coffee.
add_order(order): Adds an order to the list of orders for this coffee.
Order
Attributes:

_customer: Customer who placed the order.
_coffee: Coffee ordered.
_price: Price of the order.
Methods:

__init__(self, customer, coffee, price): Initializes an order with a customer, coffee, and price.
customer: Property to get the customer who placed the order.
coffee: Property to get the coffee ordered.
price: Property to get the price of the order.
all_orders(): Class method to get a list of all orders.
Usage
Setup: Ensure you have Python installed on your system.

Running the Debug Script:

Open a terminal or command prompt.
Navigate to the directory containing the project files.
Run the script with the command:
bash
Copy code
python debug.py
Testing: The debug.py script creates sample customers, coffees, and orders to demonstrate the functionality of the classes. It prints out various details such as the orders placed by each customer, the coffees ordered, and statistics like the number of orders and average prices.

Dependencies
This project does not have any external dependencies beyond Python's standard library.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Mark Silas
