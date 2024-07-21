# Built in functions of list

name1 = ["arun","akash","charran"]
name2 = ["akshaya","abinaya","banu","bhuva"]

name1.append("denver") #append function
print(name1)

name3 = name2.copy() # copy function
print(name3)

print(name1.count('charran')) # Count function

name1.extend(name2) #Extend function
print(name1)

print(name1.index("akshaya")) #index function

print(name1.pop(5)) #pop function

name1.insert(6, "chithra") # insert function
print(name1)

name2.remove("bhuva")#remove function
print(name2)

name1.reverse() #Reverse function
print(name1)

name1.sort() #Sort function
print(name1)