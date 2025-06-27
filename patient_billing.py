services = {
    "1": ("General Consultation", 10000),
    "2": ("Lab Test", 15000),
    "3": ("X-Ray", 25000),
    "4": ("Surgery", 120000)
}

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 60:
    print(f"Dear {name}, you are eligible for free treatment.")
else:
    print("Select the services you need (enter numbers separated by commas):")
    for key, (service, price) in services.items():
        print(f"{key}. {service} – TZS {price:,}")

    selected = input("You Selected: ").split(",")
    
    total = 0
    print("\nCost Breakdown:")
    for choice in selected:
        choice = choice.strip()
        if choice in services:
            service_name, service_price = services[choice]
            print(f"- {service_name}: TZS {service_price:,}")
            total += service_price
        else:
            print(f"- Invalid Choice!: {choice}")

    if total > 100000:
        discount = total * 0.10
        total -= discount
        print(f"Discount applied (10%): TZS {discount:,}")

    print(f"Total Bill: TZS {total:,}")
