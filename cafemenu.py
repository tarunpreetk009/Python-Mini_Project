# Malkin Cafe - Menu Ordering System

menu = {
    "cappuccino": 350,
    "latte": 300,
    "espresso": 200,
    "mocha": 360,
    "tea": 200,
    "hot chocolate": 360
}

def display_menu():
    print("\nWelcome to Malkin Cafe ☕")
    print("Here's our menu:\n")
    for item, price in menu.items():
        print(f"{item.title():<15} - ₹{price:.2f}")
    print("\nType 'done' when you're finished ordering.\n")

def take_order():
    order = []
    total = 0.0

    while True:
        item = input("Enter item name to order (or type 'done'): ").strip().lower()
        if item == "done":
            break
        elif item in menu:
            order.append(item)
            total += menu[item]
            print(f"✅ Added {item.title()} - ₹{menu[item]:.2f}")
        else:
            print("❌ Item not on menu. Please try again.")

    return order, total

def display_summary(order, total):
    print("\n🧾 Order Summary:")
    if order:
        for item in order:
            print(f"- {item.title()} - ₹{menu[item]:.2f}")
        print(f"\nTotal Bill: ₹{total:.2f}")
        print("Thank you for visiting Malkin Cafe! 🌟\n")
    else:
        print("No items ordered.\n")

def main():
    display_menu()
    order, total = take_order()
    display_summary(order, total)

if __name__ == "__main__":
    main()
