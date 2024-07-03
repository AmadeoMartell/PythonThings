class RetailItem:
    def __init__(self, description, units_inventory=0, price=0.0):
        self.description = description
        self.units_inventory = units_inventory
        self.price = price

class CashRegister:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        return sum(item.price for item in self.items)

    def show_items(self):
        for item in self.items:
            print(f"{item.description}: {item.units_inventory} at ${item.price}")

    def clear(self):
        self.items = []

items = [RetailItem("Jacket", 12, 59.95),
         RetailItem("Designer Jeans", 40, 34.95),
         RetailItem("Shirt", 20, 24.95)]

cash_register = CashRegister()

print("Available commands: shop, total, cart, clear, quit")
while True:
    command = input("Enter command: ").lower()
    if command == "shop":
        for index, item in enumerate(items, 1):
            print(f"{index}. {item.description} - {item.units_inventory} units at ${item.price} each")
        choice = int(input("Enter item number to add to cart: ")) - 1
        if 0 <= choice < len(items):
            cash_register.add_item(items[choice])
            print(f"Added {items[choice].description} to cart.")
        else:
            print("Invalid item.")
    elif command == "total":
        print(f"Total price: ${cash_register.get_total()}")
    elif command == "cart":
        cash_register.show_items()
    elif command == "clear":
        cash_register.clear()
        print("Cart cleared.")
    elif command == "quit":
        break
    else:
        print("Unknown command.")
