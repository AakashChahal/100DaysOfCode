print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tot_tip = tip / 100 * bill
tot_bill = bill + tot_tip
per_head = tot_bill / people
final_bill = "{:.2f}".format(per_head)
print(f"Each person should pay: ${final_bill}")