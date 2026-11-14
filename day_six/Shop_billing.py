# “Simple Shop Billing System” 


# Product details are stored as tuples
product_details = (
    ("Pen", 10, "Stationery"),
    ("Notebook", 50, "Stationery"),
    ("Pencil", 5, "Stationery")
)

# Product names and prices are stored in a dictionary
products = {}
categories = set()

for name, price, category in product_details:
    products[name] = price
    categories.add(category)

# Cart items are stored in a list
# Each cart item is a tuple: (product name, price, quantity)
cart = []


def display_products():
    print("Available Products:")
    for name, price in products.items():
        print(name, ":", price)


def add_to_cart():
    name = input("Enter product name: ")

    try:
        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        price = products[name]
        cart.append((name, price, quantity))
        print("Item added to cart successfully.")

    except NameError:
        print("Product not found in store.")
    except ValueError:
        print("Invalid quantity! Please enter a number.")


def recursive_total(items):
    if not isinstance(items, list):
        raise TypeError

    if len(items) == 0:
        return 0

    item = items[0]

    if not isinstance(item, tuple):
        raise TypeError

    name, price, quantity = item
    item_total = price * quantity

    return item_total + recursive_total(items[1:])


def view_total_bill():
    if not cart:
        print("Cart is empty.")
        return

    print("Items in Cart:")
    for name, price, quantity in cart:
        print(name, "x", quantity)

    try:
        total = recursive_total(cart)
        print("Total Bill:", total)
    except TypeError:
        print("Cart data type error.")
    except ZeroDivisionError:
        print("Calculation error: division by zero.")


while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_total_bill()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
