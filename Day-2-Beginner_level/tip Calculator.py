print("Welcome to the tip calculator")

bill=float(input("what is the total amount? \n "))
tip_percentage=int(input("what is the tip would you like to give? 10,15 or 20 \n"))
people=int(input("how many are there to share the amount? \n"))

total_amount= bill * (tip_percentage/100)
total_bill= bill + total_amount
bill_per_person = total_bill/people

final_amount="{:.2f}".format(bill_per_person)

print(f"the total amount is: \n ₹{final_amount}")
