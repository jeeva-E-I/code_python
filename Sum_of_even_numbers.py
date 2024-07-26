target = int(input("Enter the maximum of number of value to be added")) 
sum = 0
for x in range(1,target+1):
  if x%2 == 0:
    sum += x
print(sum)
