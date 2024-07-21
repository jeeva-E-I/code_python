#Day 2 project: Tip calculator

print("welcome to the tip calculator!")
print("what was the total bill?")
bill = float(input())
tip = int(input("how much tip would you like to give in percent..?"))
print("How many people to spilt the bill?")
spilt_people = int(input())
final_bill = tip / 100 * bill + bill
final_bill = round(final_bill,2) / spilt_people
print(f"Each person should pay:{final_bill}")
