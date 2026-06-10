#A simple Patient Billing System

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 60:
    print(f"Dear {name}, you are eligible for free treatment.")
else:
    print("Select the services you need (enter numbers separated by commas):")
    print("1. General Consultation – TZS 10,000")
    print("2. Lab Test – TZS 15,000")
    print("3. X-Ray – TZS 25,000")
    print("4. Surgery – TZS 120,000")

    selected = input("You Selected: ").split(",")
    
    total = 0
    print("\nCost Breakdown:")

    for choice in selected:
        choice = choice.strip()
        if choice == "1":
            print("- General Consultation: TZS 10,000")
            total += 10000
        elif choice == "2":
            print("- Lab Test: TZS 15,000")
            total += 15000
        elif choice == "3":
            print("- X-Ray: TZS 25,000")
            total += 25000
        elif choice == "4":
            print("- Surgery: TZS 120,000")
            total += 120000
        else:
            print(f"- Invalid Choice!: {choice}")

    if total > 100000:
        discount = total * 0.10
        total -= discount
        print(f"Discount applied (10%): TZS {discount: }")

    print(f"Total Bill: TZS {total: }")
