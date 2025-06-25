mb = int(input("Enter Data Size in MB: "))

cost_below = 50
cost_above = 100

if mb <= 500:
    print("The cost is: ", mb*cost_below, "Tzs")
elif mb>500:
    print("The cost is: ", mb*cost_above, "Tzs")