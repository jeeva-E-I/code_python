#BMI calculation

height = float(input("Enter the height:"))
weight = int(input("Enter the weight:"))
result = weight / (height ** 2)
result = int(result)
print(result)

#Leap year
year = int(input("enter the year:"))
if (year %400 == 0) and (year %100 ==0):
    print("leap year")
elif (year %4 ==0) and (year %100 !=0):
    print("leap year")
else:
    print("Not a leap year")