# shop management system

list_item = {}
balance = 0

def shop_management_system():
    global balance
    while True:
        print("\n=== SHOP MENU ===")
        print("1. View items")
        print("2. Add item")
        print("3. Sell item")
        print("4. Show balance")
        print("5. Exit")

        try:
            choice = int(input("Choose (1-5): "))
            if choice == 1:
                open_lst_item()
            elif choice == 2:
                add_item()
            elif choice == 3:
                sell_item()
            elif choice == 4:
                print(f"Current balance: {balance}")
            elif choice == 5:
                print("Exiting shop...")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a number (1-5).")

def open_lst_item():
    if list_item:
        print("\nItems in shop:")
        for item, price in list_item.items():
            print(f"- {item}: {price}")
    else:
        print("No items available.")

def add_item():
    global list_item
    try:
        item = input("Enter item name: ")
        price = float(input("Enter price: "))
        list_item[item] = price
        print(f"Added {item} for {price}.")
    except ValueError:
        print("Price must be a number.")

def sell_item():
    global list_item, balance
    item = input("Enter item to sell: ")
    if item in list_item:
        price = list_item.pop(item)
        balance += price
        print(f"Sold {item} for {price}. New balance: {balance}")
    else:
        print(f"{item} not found in shop.")

if __name__ == "__main__":
    shop_management_system()
