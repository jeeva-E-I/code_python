#Typechecking

val=124
print(type(val))

#Type conversion

str1=str(val)
print(type(str1))

#Write a program that adds the digits in a 2 digit number.
two_digit_number = input()
str(two_digit_number)
val1 =two_digit_number[0]
val1 =int(val1)
val2 =two_digit_number[1]
val2 =int(val2)
print(val1+val2)

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
