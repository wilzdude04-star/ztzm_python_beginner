# MiniMart CLI Shopping Cart

# Store cart items in a dictionary
cart = {}

print("Welcome to MiniMart!")

while True:
    print("\n1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")

    choice = input("\nChoose an option: ")

    # Add item
    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))

        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

        print(f"{item} added to cart.")

    # Remove item
    elif choice == "2":
        item = input("Enter item name to remove: ")

        if item in cart:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")

    # View cart
    elif choice == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            print(cart)

    # Checkout
    elif choice == "4":
        print("\nThank you for shopping! You bought:")

        if not cart:
            print("Nothing (your cart was empty).")
        else:
            print(cart)

        break

    # Invalid option
    else:
        print("Invalid choice. Please select 1-4.")
