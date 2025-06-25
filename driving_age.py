age = int(input("Enter your Age: "))

if age >= 21 and age <= 75:
    print("Eligible for a driving license.")
elif age < 21:
    print("You must be atleast 21 years to apply!")
else:
    print("You are too old to drive!") 