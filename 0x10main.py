# Simple Unit Converter Program (Improved Version)

print("Welcome to the Simple Unit Converter!")

while True:
    # Show conversion options
    print("\nChoose a conversion type:")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Grams to Pounds")
    print("4. Exit")

    # Get user choice
    choice = input("\nEnter your choice (1/2/3/4): ")

    if choice == "1":
        kilometers = float(input("Enter distance in kilometers: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} km is equal to {round(miles, 2)} miles.")

    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {round(fahrenheit, 2)}°F")

    elif choice == "3":
        grams = float(input("Enter weight in grams: "))
        pounds = grams * 0.00220462
        print(f"{grams} g is equal to {round(pounds, 2)} lbs.")

    elif choice == "4":
        print("Thank you for using the converter. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

    print("\n--------")
