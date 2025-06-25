name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age <=12:
    print(f"Dear,{name} you qualify for a free school lunch.")
else:
    print("You do NOT qualify for a free school lunch.")
    print("***Enter your selection (1,2 or 3)***")
    print("1. Small Meal - TZS 500")
    print("2. Medium Meal - TZS 800")
    print("3. Large Meal - TZS 1200")
    selection = int(input("Selection: "))
    if selection == 1:
        print("You selected: Small Meal. Price: TZS500")
    elif selection == 2:
        print("You selected: Medium Meal. Price: TZS 800")
    elif selection == 3:
        print("You selected: Large Meal. Price: TZS 1200")
    else:
        print("Wrong Selection!")