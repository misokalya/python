kWh = int(input("Enter units in kWh: "))

cost_below = 100
cost_above = 200

if kWh <= 50:
    print("The cost is: ", kWh*cost_below, "Tzs")
elif kWh>50:
    print("The cost is: ", kWh*cost_above, "Tzs")