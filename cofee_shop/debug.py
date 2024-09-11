from customer import Customer
from coffee import Coffee
from order import Order

def debug():
    # Create some customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")

    # Create some coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")

    # Create some orders
    order1 = alice.create_order(espresso, 4.5)
    order2 = bob.create_order(latte, 5.0)
    order3 = alice.create_order(latte, 6.0)
    order4 = charlie.create_order(cappuccino, 3.0)

    # Check customers' orders
    print(f"Alice's Orders: {[order.coffee.name for order in alice.orders()]}")
    print(f"Bob's Orders: {[order.coffee.name for order in bob.orders()]}")
    print(f"Charlie's Orders: {[order.coffee.name for order in charlie.orders()]}")

    # Check coffees ordered by customers
    print(f"Alice's Coffees: {[coffee.name for coffee in alice.coffees()]}")
    print(f"Bob's Coffees: {[coffee.name for coffee in bob.coffees()]}")
    print(f"Charlie's Coffees: {[coffee.name for coffee in charlie.coffees()]}")

    # Check the total number of orders for each coffee
    print(f"Espresso Orders: {espresso.num_orders()}")
    print(f"Latte Orders: {latte.num_orders()}")
    print(f"Cappuccino Orders: {cappuccino.num_orders()}")

    # Check average price of each coffee
    print(f"Espresso Average Price: {espresso.average_price()}")
    print(f"Latte Average Price: {latte.average_price()}")
    print(f"Cappuccino Average Price: {cappuccino.average_price()}")

    # Bonus: Find the most aficionado of a particular coffee
    most_espresso = Customer.most_aficionado(espresso)
    if most_espresso:
        print(f"Most Aficionado of Espresso: {most_espresso.name}")
    else:
        print("No orders for Espresso yet")

if __name__ == "__main__":
    debug()
