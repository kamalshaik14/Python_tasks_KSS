#3. Shopping Cart System
#Scenario: A user adds items to a shopping cart.
#Task:
#● Store items in a list
#● Convert to set to remove duplicates
#● Use loop + condition to calculate total cost
#● Handle invalid input using try-excep


items = ["apple", "bread", "apple", "milk"]

# Remove duplicate items
cart = set(items)

prices = {
    "apple": 2.0,
    "bread": 3.5,
    "milk": 4.0
}

total = 0

# Calculate total cost
for item in cart:
    try:
        if item in prices:
            total += prices[item]
        else:
            raise ValueError(f"Price not found for {item}")
    except ValueError as error:
        print("Invalid item:", error)

print("Cart:", cart)
print("Total cost:", total)
