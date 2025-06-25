serv1 = "1. General Consultation - TZS. 10000"
price1 = 10000
serv2 = "2. Lab Test - TZS. 15000"
price2 = 15000
serv3 = "3. X-Ray - TZS. 25000"
price3 = 25000
serv4 = "4. Surgery - TZS. 120000"
price4 = 120000

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))

if age < 60:
    print("***Our Services***")
    print(serv1)
    print(serv2)
    print(serv3)
    print(serv4)
    choice = int(input("Enter your selection: "))
    if choice == 1:
        print(f"You have selected: {serv1}")
    elif choice == 2:
        print(f"You have selected: {serv2}")
    elif choice == 3:
        print(f"You have selected: {serv3}")
    elif choice == 4:
        print(f"You have selected: {serv4}")
    else:
        print("Invalid Selection!")
else:
    print(f"Dear {name}, You are eligible for free treatment")