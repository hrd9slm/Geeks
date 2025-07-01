from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n--- MENU ---")
        print("A: Add an Item")
        print("D: Delete an Item")
        print("U: Update an Item")
        print("V: View an Item")
        print("S: Show Full Menu")
        print("Q: Quit")

        choice = input("Choose an option: ").strip().upper()

        if choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'V':
            view_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'Q':
            print("\nFinal Restaurant Menu:")
            show_restaurant_menu()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def add_item_to_menu():
    name = input("Enter the name of the item: ").strip()
    try:
        price = int(input("Enter the price of the item: "))
        item = MenuItem(name, price)
        item.save()
        print(f"'{name}' was added successfully.")
    except Exception as e:
        print("Error adding item:", e)

def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ").strip()
    item_data = MenuManager.get_by_name(name)
    if item_data:
        item = MenuItem(item_data["item_name"], item_data["item_price"])
        item.delete()
        print(f"'{name}' was deleted successfully.")
    else:
        print(f"Item '{name}' not found.")

def update_item_from_menu():
    current_name = input("Enter the current name of the item: ").strip()
    item_data = MenuManager.get_by_name(current_name)
    if not item_data:
        print(f"Item '{current_name}' not found.")
        return

    try:
        new_name = input("Enter the new name: ").strip()
        new_price = int(input("Enter the new price: "))
        item = MenuItem(item_data["item_name"], item_data["item_price"])
        item.update(new_name, new_price)
        print(f"'{current_name}' was updated successfully to '{new_name}' with price {new_price}.")
    except Exception as e:
        print("Error updating item:", e)

def view_item_from_menu():
    name = input("Enter the name of the item to view: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item: {item['item_name']} | Price: {item['item_price']}")
    else:
        print(f"Item '{name}' not found.")

def show_restaurant_menu():
    items = MenuManager.all()
    if not items:
        print("The menu is currently empty.")
        return
    print("\n--- Restaurant Menu ---")
    for item in items:
        print(f"{item['item_name']} - {item['item_price']} MAD")
        
if __name__ == "__main__":
    show_user_menu()
