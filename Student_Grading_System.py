score = float(input("Enter your marks: "))
if score>=80 and score<=100:
    print("Excellent")
elif score>=50 and score<=79:
    print("Good")
elif score<50:
    print("Fail")
elif score>100:
    print("invalid marks")