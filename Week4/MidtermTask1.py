print((lambda x: f"You're tax for meal: {x * 0.12:.2f}$ \nYour tip for meal {x*0.18:.2f}$ \nTotal cost: {x + (x*0.12) + (x*0.18):.2f}$")(int(input("Enter a cost of meal: "))))