class ClothingItem:
    def __init__(self, item_id, name, category, quantity, price, days_in_stock):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.days_in_stock = days_in_stock
        self.sale_flag = False  # Default not for sale

    def __str__(self):
        return f"ID: {self.item_id} | {self.name} ({self.category}) | Qty: {self.quantity} | Price: ${self.price} | Days in Stock: {self.days_in_stock} | Sale Flag: {self.sale_flag}"


# Inventory control class
class InventoryControl:
    def __init__(self):
        self.inventory = []  # List to store clothing items
        self.next_id = 1  # Unique item ID counter

    def add_item(self, name, category, quantity, price, days_in_stock):
        item = ClothingItem(self.next_id, name, category, quantity, price, days_in_stock)
        self.inventory.append(item)
        self.next_id += 1
        print(f"Added: {item}")

    def edit_item(self, item_id, name=None, category=None, quantity=None, price=None, days_in_stock=None):
        item = self.get_item_by_id(item_id)
        if item:
            if name:
                item.name = name
            if category:
                item.category = category
            if quantity is not None:
                item.quantity = quantity
            if price is not None:
                item.price = price
            if days_in_stock is not None:
                item.days_in_stock = days_in_stock
            print(f"Updated: {item}")
        else:
            print(f"Item with ID {item_id} not found.")

    def delete_item(self, item_id):
        item = self.get_item_by_id(item_id)
        if item:
            self.inventory.remove(item)
            print(f"Deleted: {item}")
        else:
            print(f"Item with ID {item_id} not found.")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for item in self.inventory:
                print(item)

    def flag_items_for_sale(self):
        for item in self.inventory:
            if item.quantity < 5 or item.days_in_stock > 180:  # Conditions to flag for sale
                item.sale_flag = True
                print(f"Flagged for sale: {item}")

    def display_sale_items(self):
        flagged_items = [item for item in self.inventory if item.sale_flag]
        if not flagged_items:
            print("No items flagged for sale.")
        else:
            print("\nItems flagged for sale:")
            for item in flagged_items:
                print(item)

    def get_item_by_id(self, item_id):
        for item in self.inventory:
            if item.item_id == item_id:
                return item
        return None


# Menu-driven interaction
def inventory_menu():
    inv_control = InventoryControl()

    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Item")
        print("2. Edit Item")
        print("3. Delete Item")
        print("4. Display Inventory")
        print("5. Flag Items for Sale")
        print("6. Display Sale Items")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter item name: ")
            category = input("Enter item category: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            days_in_stock = int(input("Enter days in stock: "))
            inv_control.add_item(name, category, quantity, price, days_in_stock)

        elif choice == '2':
            item_id = int(input("Enter item ID to edit: "))
            name = input("Enter new name (or leave blank to keep current): ") or None
            category = input("Enter new category (or leave blank to keep current): ") or None
            quantity = input("Enter new quantity (or leave blank to keep current): ")
            quantity = int(quantity) if quantity else None
            price = input("Enter new price (or leave blank to keep current): ")
            price = float(price) if price else None
            days_in_stock = input("Enter new days in stock (or leave blank to keep current): ")
            days_in_stock = int(days_in_stock) if days_in_stock else None
            inv_control.edit_item(item_id, name, category, quantity, price, days_in_stock)

        elif choice == '3':
            item_id = int(input("Enter item ID to delete: "))
            inv_control.delete_item(item_id)

        elif choice == '4':
            print("\n--- Inventory List ---")
            inv_control.display_inventory()

        elif choice == '5':
            inv_control.flag_items_for_sale()

        elif choice == '6':
            inv_control.display_sale_items()

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")


# Main execution
if __name__ == "__main__":
    inventory_menu()